// =============================================
// map.js — THIR D3 Threat Map
// Renders the live SVG world map with animated
// attack trajectories and pulsing threat points.
// Depends on: data.js, d3, topojson (CDN)
//
// PATCHES:
//   FIX-4: MAP_COLOR updated to match new cyberpunk CSS palette
//          (thir.css v1.5). Old values were the pre-v1.5 colours
//          and no longer matched --accent2/3/4 CSS variables.
//          brute:    #FB592E → #ff2d78  (hot magenta, --accent2)
//          c2:       #ffaa00 → #ffcc00  (amber,       --warn)
//          scan:     #0B67C3 → #a259ff  (vivid purple, --accent4)
//          exploit:  #FB592E → #ff2d78  (hot magenta, --accent2)
//          defender: #009A83 → #00ffe5  (electric teal, --accent)
// =============================================

const MAP_COLOR = {
  brute:    '#ff2d78',   // hot magenta  — matches --accent2
  c2:       '#ffcc00',   // amber        — matches --warn
  scan:     '#a259ff',   // vivid purple — matches --accent4
  exploit:  '#ff2d78',   // hot magenta  — matches --accent2
  defender: '#00ffe5',   // electric teal — matches --accent
};

// --------------------------------------------------
// Init: build the SVG, projection, and world paths
// --------------------------------------------------
function initThreatMap() {
  const container = document.querySelector('.hero-map-panel') || document.querySelector('.hero-map') || document.querySelector('.hero-right');
  if (!container) return;

  // Remove any existing SVG content to allow re-init with live points
  const existing = document.getElementById('threat-map');
  if (existing) existing.innerHTML = '';

  // Use getBoundingClientRect for accurate post-layout dimensions
  const rect = container.getBoundingClientRect();
  const w = rect.width  || container.offsetWidth  || 800;
  const h = rect.height || container.offsetHeight || 420;

  if (w < 10 || h < 10) {
    // Layout hasn't painted yet — defer one animation frame and retry
    requestAnimationFrame(() => initThreatMap());
    return;
  }

  // Set SVG to exact panel pixel dimensions
  const svg = d3.select('#threat-map')
    .attr('width',  w)
    .attr('height', h)
    .style('width',  w + 'px')
    .style('height', h + 'px');

  // NaturalEarth1 default renders at 960×500 with scale 153.5.
  // Compute scale that fits both axes — take the smaller so no edge clips.
  const scaleByWidth  = (w / 960) * 153.5;
  const scaleByHeight = (h / 500) * 153.5;
  const scale         = Math.min(scaleByWidth, scaleByHeight);

  const projection = d3.geoNaturalEarth1()
    .scale(scale)
    .translate([w / 2, h / 2]);

  const path = d3.geoPath().projection(projection);
  const g    = svg.append('g');

  // Graticule (grid lines)
  const graticule = d3.geoGraticule();
  g.append('path')
    .datum(graticule())
    .attr('d', path)
    .attr('fill', 'none')
    .attr('stroke', 'rgba(30,48,69,0.6)')
    .attr('stroke-width', 0.5);

  // Load world topology from CDN
  fetch('https://cdn.jsdelivr.net/npm/world-atlas@2/countries-110m.json')
    .then(r => r.json())
    .then(world => {
      const countries = topojson.feature(world, world.objects.countries);
      g.selectAll('.country')
        .data(countries.features)
        .enter().append('path')
        .attr('class', 'country')
        .attr('d', path)
        .attr('fill',         'rgba(12,18,32,0.9)')
        .attr('stroke',       'rgba(30,48,69,0.8)')
        .attr('stroke-width', 0.5);

      addThreatPoints(g, projection);
    })
    .catch(() => {
      // Graceful fallback: render points without base map
      addThreatPoints(g, projection);
      g.append('text')
        .attr('x', w / 2).attr('y', h / 2)
        .attr('text-anchor', 'middle')
        .attr('fill',        'rgba(74,104,128,0.4)')
        .attr('font-size',   11)
        .attr('font-family', 'Share Tech Mono, monospace')
        .text('// connect to CDN for full map render');
    });
}

// --------------------------------------------------
// Draw: threat points and animated attack lines
// --------------------------------------------------
function addThreatPoints(g, projection) {
  const points = liveMapPoints || THREAT_LOCS;
  const mumbai = [72.87, 19.07];

  // Animated packet lines from attackers → honeypot
  points.filter(l => l.type !== 'defender').forEach(loc => {
    const start = projection(loc.coords);
    const end   = projection(mumbai);
    if (!start || !end) return;

    g.append('line')
      .attr('x1', start[0]).attr('y1', start[1])
      .attr('x2', end[0]).attr('y2', end[1])
      .attr('stroke',           MAP_COLOR[loc.type])
      .attr('stroke-width',     0.5)
      .attr('stroke-opacity',   0.18)
      .attr('stroke-dasharray', '3,3');

    const dot = g.append('circle')
      .attr('r',       2)
      .attr('fill',    MAP_COLOR[loc.type])
      .attr('opacity', 0.75);

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

  // Pulsing dot for each threat location
  points.forEach(loc => {
    const pt = projection(loc.coords);
    if (!pt) return;

    const color      = MAP_COLOR[loc.type];
    const isDefender = loc.type === 'defender';
    const r          = isDefender ? 6 : 4;

    // Expanding pulse ring
    g.append('circle')
      .attr('cx', pt[0]).attr('cy', pt[1])
      .attr('r',  r)
      .attr('fill',           'none')
      .attr('stroke',         color)
      .attr('stroke-width',   1)
      .attr('stroke-opacity', 0.5)
      .call(sel => {
        (function pulse() {
          sel.attr('r', r).attr('stroke-opacity', 0.6)
            .transition().duration(1500 + Math.random() * 1000)
            .attr('r',              r + 8)
            .attr('stroke-opacity', 0)
            .on('end', pulse);
        })();
      });

    // Solid centre dot
    g.append('circle')
      .attr('cx', pt[0]).attr('cy', pt[1])
      .attr('r',       isDefender ? 5 : 3)
      .attr('fill',    color)
      .attr('opacity', isDefender ? 1 : 0.85);

    // Label for the honeypot marker only
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
