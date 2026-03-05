// =============================================
// map.js — THIR D3 Threat Map
// Renders the live SVG world map with animated
// attack trajectories and pulsing threat points.
// Depends on: data.js, d3, topojson (CDN)
// =============================================

const MAP_COLOR = {
  brute:    '#ff3d71',
  c2:       '#ffaa00',
  scan:     '#00aacc',
  exploit:  '#ff3d71',
  defender: '#39ff14',
};

// --------------------------------------------------
// Init: build the SVG, projection, and world paths
// --------------------------------------------------
function initThreatMap() {
  const container = document.querySelector('.hero-map') || document.querySelector('.hero-right');
  if (!container) return;

  // Remove any existing SVG to allow re-init with live points
  const existing = document.getElementById('threat-map');
  if (existing) existing.innerHTML = '';

  const w = container.clientWidth  || 800;
  const h = container.clientHeight || 420;

  const svg = d3.select('#threat-map')
    .attr('width',  w)
    .attr('height', h);

  const projection = d3.geoNaturalEarth1()
    .scale(w / 6.3)
    .translate([w / 2, h / 2]);

  const path = d3.geoPath().projection(projection);
  const g    = svg.append('g');

  // Graticule (grid lines)
  const graticule = d3.geoGraticule();
  g.append('path')
    .datum(graticule())
    .attr('d', path)
    .attr('fill', 'none')
    .attr('stroke', 'rgba(26,45,61,0.5)')
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
        .attr('fill',         'rgba(15,25,35,0.9)')
        .attr('stroke',       'rgba(26,45,61,0.8)')
        .attr('stroke-width', 0.5);

      addThreatPoints(g, projection);
    })
    .catch(() => {
      // Graceful fallback: render points without base map
      addThreatPoints(g, projection);
      g.append('text')
        .attr('x', w / 2).attr('y', h / 2)
        .attr('text-anchor', 'middle')
        .attr('fill',        'rgba(90,122,138,0.3)')
        .attr('font-size',   11)
        .attr('font-family', 'Share Tech Mono, monospace')
        .text('// connect to CDN for full map render');
    });
}

// --------------------------------------------------
// Draw: threat points and animated attack lines
// --------------------------------------------------
function addThreatPoints(g, projection) {
  const points   = liveMapPoints || THREAT_LOCS;
  const mumbai   = [72.87, 19.07];

  // Animated packet lines from attackers → honeypot
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
      .attr('r',       2)
      .attr('fill',    MAP_COLOR[loc.type])
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

    // Label for the honeypot marker
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
