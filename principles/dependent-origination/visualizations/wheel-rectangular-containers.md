# Wheel of Dependent Origination - Rectangular Containers

A circular representation of the twelve links of dependent origination arranged in a wheel, with rectangular containers and clockwise flow indicators.

## Visualization

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 800">
  <!-- Outer circle -->
  <circle cx="400" cy="400" r="340" fill="white" stroke="#333" stroke-width="3"/>
  
  <!-- Arrowhead definition -->
  <defs>
    <marker id="arrowhead" markerWidth="13" markerHeight="9" refX="0" refY="4.5" orient="auto">
      <polygon points="0 0, 13 4.5, 0 9" fill="#8B0000"/>
    </marker>
  </defs>

  <!-- Flow arrows - centered between containers -->
  <g fill="none" stroke="#8B0000" stroke-width="2">
    <!-- 12 arrowheads at midpoints -->
    <path d="M 400,60 L 400,60" transform="rotate(0, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(30, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(60, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(90, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(120, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(150, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(180, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(210, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(240, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(270, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(300, 400, 400)" marker-end="url(#arrowhead)"/>
    <path d="M 400,60 L 400,60" transform="rotate(330, 400, 400)" marker-end="url(#arrowhead)"/>
  </g>

  <!-- All 12 Containers -->
  <!-- Container 1: Ignorance (at 15 degrees) -->
  <g transform="translate(400,400) rotate(15) translate(0,-340) rotate(-15)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#E6F3FF" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">1. Ignorance</text>
  </g>

  <!-- Container 2: Contaminated Karma (at 45 degrees) -->
  <g transform="translate(400,400) rotate(45) translate(0,-340) rotate(-45)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#F3E6FF" stroke="#333" stroke-width="2"/>
    <text y="-10" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">2. Contaminated</text>
    <text y="10" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">Karma</text>
  </g>

  <!-- Container 3: Consciousness (at 75 degrees) -->
  <g transform="translate(400,400) rotate(75) translate(0,-340) rotate(-75)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#FFE6E6" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">3. Consciousness</text>
  </g>

  <!-- Container 4: Name & Form (at 105 degrees) -->
  <g transform="translate(400,400) rotate(105) translate(0,-340) rotate(-105)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#E6FFE6" stroke="#333" stroke-width="2"/>
    <text y="-10" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">4. Name</text>
    <text y="10" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">& Form</text>
  </g>

  <!-- Container 5: Six Senses (at 135 degrees) -->
  <g transform="translate(400,400) rotate(135) translate(0,-340) rotate(-135)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#FFF6E6" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">5. Six Senses</text>
  </g>

  <!-- Container 6: Contact (at 165 degrees) -->
  <g transform="translate(400,400) rotate(165) translate(0,-340) rotate(-165)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#E6FFF3" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">6. Contact</text>
  </g>

  <!-- Container 7: Feeling (at 195 degrees) -->
  <g transform="translate(400,400) rotate(195) translate(0,-340) rotate(-195)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#FFE6F3" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">7. Feeling</text>
  </g>

  <!-- Container 8: Craving (at 225 degrees) -->
  <g transform="translate(400,400) rotate(225) translate(0,-340) rotate(-225)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#F3FFE6" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">8. Craving</text>
  </g>

  <!-- Container 9: Clinging (at 255 degrees) -->
  <g transform="translate(400,400) rotate(255) translate(0,-340) rotate(-255)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#E6F3FF" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">9. Clinging</text>
  </g>

  <!-- Container 10: Becoming (at 285 degrees) -->
  <g transform="translate(400,400) rotate(285) translate(0,-340) rotate(-285)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#FFE6E6" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">10. Becoming</text>
  </g>

  <!-- Container 11: Birth (at 315 degrees) -->
  <g transform="translate(400,400) rotate(315) translate(0,-340) rotate(-315)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#E6FFE6" stroke="#333" stroke-width="2"/>
    <text y="0" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">11. Birth</text>
  </g>

  <!-- Container 12: Ageing & Death (at 345 degrees) -->
  <g transform="translate(400,400) rotate(345) translate(0,-340) rotate(-345)">
    <rect x="-70" y="-25" width="140" height="50" rx="10" fill="#FFF6E6" stroke="#333" stroke-width="2"/>
    <text y="-10" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">12. Ageing</text>
    <text y="10" text-anchor="middle" dominant-baseline="middle" font-size="16" font-weight="bold">& Death</text>
  </g>

  <!-- Center design -->
  <circle cx="400" cy="400" r="50" fill="white" stroke="#333" stroke-width="2"/>
  <text x="400" y="395" text-anchor="middle" font-size="14" font-weight="bold">Dependent</text>
  <text x="400" y="415" text-anchor="middle" font-size="14" font-weight="bold">Origination</text>
</svg>

## Description

This visualization represents the twelve links of dependent origination in a wheel format, featuring:
- Rectangular containers with rounded corners for each link
- Clockwise flow indicators showing the continuous cycle
- Two-line text for complex terms ("Contaminated Karma", "Name & Form", "Ageing & Death")
- Centered text alignment in each container
- Consistent 30-degree spacing between elements
- Dark red directional arrows indicating the wheel's rotation

## Notes
- Containers are sized to accommodate the largest single-line text ("Consciousness")
- Multi-line text is used to maintain consistent container dimensions
- Arrowheads indicate the clockwise flow between links

## References
- Mūlamadhyamakakārikā (Chapter 26)
- Visuddhimagga (Chapter XVII)
- Abhidharmakośa (Chapter III)