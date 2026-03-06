// =============================================
// map.js — THIR D3 Threat Map
// Renders the live SVG world map with animated
// attack trajectories and pulsing threat points.
// Depends on: data.js, d3, topojson (CDN)
// =============================================

const MAP_COLOR = {
  brute:    '#FB592E',
  c2:       '#ffaa00',
  scan:     '#0B67C3',
  exploit:  '#FB592E',
  defender: '#009A83',
};

// Cache world topology — avoids re-fetching on every resize
let _worldCache = null;

// --------------------------------------------------
// Measure: get map dimensions from container WIDTH only.
// Height is fixed per breakpoint to match CSS exactly.
// Never reads clientHeight — the absolutely-positioned
// overlay makes that unreliable on mobile.
// --------------------------------------------------
function getMapDimensions() {
  const container = document.querySelector('.hero-map') || document.querySelector('.hero-right');
  const w = container ? (container.clientWidth || 800) : 800;
  const h = w <= 768 ? 380 : w <= 1024 ? 300 : 420;
  return { w, h };
}

// --------------------------------------------------
// Init: build the SVG, projection, and world paths
// --------------------------------------------------
function initThreatMap() {
  const container = document.querySelector('.hero-map') || document.querySelector('.hero-right');
  if (!container) return;

  // Measure BEFORE clearing — always valid
  const { w, h } = getMapDimensions();

  // Clear existing SVG content
  const existing = document.getElementById('threat-map');
  if (existing) existing.innerHTML = '';

  // Set SVG to exact pixel dimensions — both attribute and style
  const svg = d3.select('#threat-map')
    .attr('width',  w)
    .attr('height', h)
    .style('width',  w + 'px')
    .style('height', h + 'px');

  // Scale proportional to width, capped for wide screens
  const scale = Math.min(w / 6.3, 165);

  const projection = d3.geoNaturalEarth1()
    .scale(scale)
    .translate([w / 2, h / 2]);

  const path = d3.geoPath().projection(projection);
  const g    = svg.append('g');

  // Graticule
  const graticule = d3.geoGraticule();
  g.append('path')
    .datum(graticule())
    .attr('d', path)
    .attr('fill', 'none')
    .attr('stroke', 'rgba(26,45,61,0.5)')
    .attr('stroke-width', 0.5);

  if (_worldCache) {
    _drawWorld(g, path, projection, _worldCache);
  } else {
    fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json')
      .then(r => r.json())
      .then(world => {
        _worldCache = world;
        _drawWorld(g, path, projection, world);
      })
      .catch(() => {
        addThreatPoints(g, projection);
        g.append('text')
          .attr('x', w / 2).attr('y', h / 2)
          .attr('text-anchor', 'middle')
          .attr('fill', 'rgba(90,122,138,0.3)')
          .attr('font-size', 11)
          .attr('font-family', 'Share Tech Mono, monospace')
          .text('// connect to CDN for full map render');
      });
  }
}

function _drawWorld(g, path, projection, world) {
  const countries = topojson.feature(world, world.objects.countries);
  g.selectAll('.country')
    .data(countries.features)
    .enter().append('path')
    .attr('class', 'country')
    .attr('d', path)
    .attr('fill',         'rgba(15,25,35,0.9)')
    .attr('stroke',       'rgba(26,45,61,0.8)')
    .attr('stroke-width', 0.5);
  addThreatPoints(g, projection);
}

// --------------------------------------------------
// Draw: threat points and animated attack lines
// --------------------------------------------------
function addThreatPoints(g, projection) {
  const points = liveMapPoints || THREAT_LOCS;
  const mumbai = [72.87, 19.07];

  points.filter(l => l.type !== 'defender').forEach(loc => {
    const start = projection(loc.coords);
    const end   = projection(mumbai);
    if (!start || !end) return;

    g.append('line')
      .attr('x1', start[0]).attr('y1', start[1])
      .attr('x2', end[0]).attr('y2', end[1])
      .attr('stroke',         MAP_COLOR[loc.type])
      .attr('stroke-width',   0.5)
      .attr('stroke-opacity', 0.15)
      .attr('stroke-dasharray', '3,3');

    const dot = g.append('circle')
      .attr('r', 2)
      .attr('fill', MAP_COLOR[loc.type])
      .attr('opacity', 0.7);

    (function animatePacket() {
      dot.attr('cx', start[0]).attr('cy', start[1])
        .transition()
        .duration(2000 + Math.random() * 3000)
        .ease(d3.easeLinear)
        .attr('cx', end[0]).attr('cy', end[1])
        .on('end', () => {
          dot.attr('cx', start[0]).attr('cy', start[1]);
          setTimeout(animatePacket, Math.random() * 2000);
        });
    })();
  });

  points.forEach(loc => {
    const pt = projection(loc.coords);
    if (!pt) return;

    const color      = MAP_COLOR[loc.type];
    const isDefender = loc.type === 'defender';
    const r          = isDefender ? 6 : 4;

    g.append('circle')
      .attr('cx', pt[0]).attr('cy', pt[1])
      .attr('r',  r)
      .attr('fill', 'none')
      .attr('stroke', color)
      .attr('stroke-width', 1)
      .attr('stroke-opacity', 0.5)
      .call(sel => {
        (function pulse() {
          sel.attr('r', r).attr('stroke-opacity', 0.6)
            .transition().duration(1500 + Math.random() * 1000)
            .attr('r', r + 8)
            .attr('stroke-opacity', 0)
            .on('end', pulse);
        })();
      });

    g.append('circle')
      .attr('cx', pt[0]).attr('cy', pt[1])
      .attr('r',       isDefender ? 5 : 3)
      .attr('fill',    color)
      .attr('opacity', isDefender ? 1 : 0.85);

    if (isDefender) {
      g.append('text')
        .attr('x', pt[0] + 8).attr('y', pt[1] + 4)
        .attr('fill',        color)
        .attr('font-size',   9)
        .attr('font-family', 'Share Tech Mono, monospace')
        .text(loc.label);
    }
  });
}

// --------------------------------------------------
// Resize: redraw only when width changes by > 5px.
// Tracks lastDrawnW so pointless redraws are skipped.
// Debounced 200ms. Falls back to window resize event.
// --------------------------------------------------
(function initMapResize() {
  let resizeTimer = null;
  let lastDrawnW  = 0;

  function maybeRedraw() {
    const { w } = getMapDimensions();
    if (Math.abs(w - lastDrawnW) < 5) return;
    lastDrawnW = w;
    initThreatMap();
  }

  // Track width after every draw
  const _origInit = window.initThreatMap || initThreatMap;
  const _patched  = function() {
    _origInit();
    lastDrawnW = getMapDimensions().w;
  };
  window.initThreatMap = _patched;

  const scheduleRedraw = () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(maybeRedraw, 200);
  };

  if (window.ResizeObserver) {
    const ro = new ResizeObserver(scheduleRedraw);
    document.addEventListener('DOMContentLoaded', () => {
      const c = document.querySelector('.hero-map');
      if (c) ro.observe(c);
    });
  }

  window.addEventListener('resize', scheduleRedraw);
})();
