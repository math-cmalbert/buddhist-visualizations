<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <!-- Past Life Section -->
  <g transform="translate(0, 0)">
    <rect x="100" y="20" width="600" height="160" fill="#f0f0f0" stroke="#333" stroke-width="2"/>
    <text x="120" y="50" font-size="18" fill="#333">Past Life (pūrvabhava / pubbabhava)</text>
    
    <!-- Past Causes -->
    <g transform="translate(150, 70)">
      <rect x="0" y="0" width="200" height="90" fill="#e1e1e1" stroke="#666"/>
      <text x="10" y="20" font-size="14">1. Ignorance</text>
      <text x="10" y="40" font-size="12">(avidyā / avijjā)</text>
      <text x="10" y="60" font-size="14">2. Formations</text>
      <text x="10" y="80" font-size="12">(saṃskāra / saṅkhāra)</text>
    </g>
  </g>

  <!-- Present Life Section -->
  <g transform="translate(0, 180)">
    <rect x="100" y="0" width="600" height="240" fill="#e6e6ff" stroke="#333" stroke-width="2"/>
    <text x="120" y="30" font-size="18" fill="#333">Present Life (vartamānabhava / paccuppannabhava)</text>
    
    <!-- Present Effects -->
    <g transform="translate(150, 50)">
      <rect x="0" y="0" width="200" height="160" fill="#d4d4ff" stroke="#666"/>
      <text x="10" y="20" font-size="14">3. Consciousness</text>
      <text x="10" y="40" font-size="12">(vijñāna / viññāṇa)</text>
      <text x="10" y="65" font-size="14">4. Name-Form</text>
      <text x="10" y="85" font-size="12">(nāmarūpa / nāmarūpa)</text>
      <text x="10" y="110" font-size="14">5. Six Senses</text>
      <text x="10" y="130" font-size="12">(ṣaḍāyatana / saḷāyatana)</text>
    </g>
    
    <!-- Present Causes -->
    <g transform="translate(400, 50)">
      <rect x="0" y="0" width="200" height="160" fill="#d4d4ff" stroke="#666"/>
      <text x="10" y="20" font-size="14">6. Contact</text>
      <text x="10" y="40" font-size="12">(sparśa / phassa)</text>
      <text x="10" y="65" font-size="14">7. Feeling</text>
      <text x="10" y="85" font-size="12">(vedanā / vedanā)</text>
      <text x="10" y="110" font-size="14">8. Craving</text>
      <text x="10" y="130" font-size="12">(tṛṣṇā / taṇhā)</text>
    </g>
  </g>

  <!-- Future Life Section -->
  <g transform="translate(0, 420)">
    <rect x="100" y="0" width="600" height="160" fill="#ffe6e6" stroke="#333" stroke-width="2"/>
    <text x="120" y="30" font-size="18" fill="#333">Future Life (āgāmibhava / anāgatabhava)</text>
    
    <!-- Future Effects -->
    <g transform="translate(150, 50)">
      <rect x="0" y="0" width="200" height="90" fill="#ffd4d4" stroke="#666"/>
      <text x="10" y="20" font-size="14">9. Clinging</text>
      <text x="10" y="40" font-size="12">(upādāna / upādāna)</text>
      <text x="10" y="65" font-size="14">10. Becoming</text>
      <text x="10" y="85" font-size="12">(bhava / bhava)</text>
    </g>

    <g transform="translate(400, 50)">
      <rect x="0" y="0" width="200" height="90" fill="#ffd4d4" stroke="#666"/>
      <text x="10" y="20" font-size="14">11. Birth</text>
      <text x="10" y="40" font-size="12">(jāti / jāti)</text>
      <text x="10" y="65" font-size="14">12. Aging-Death</text>
      <text x="10" y="85" font-size="12">(jarāmaraṇa / jarāmaraṇa)</text>
    </g>
  </g>

  <!-- Connecting Arrows -->
  <g stroke="#333" stroke-width="2" fill="none">
    <!-- Past to Present -->
    <path d="M 250,160 C 250,180 250,180 250,200" marker-end="url(#arrowhead)"/>
    <!-- Present Effects to Causes -->
    <path d="M 350,280 C 370,280 380,280 400,280" marker-end="url(#arrowhead)"/>
    <!-- Present to Future -->
    <path d="M 500,340 C 500,360 500,380 500,420" marker-end="url(#arrowhead)"/>
  </g>

  <!-- Arrow Marker Definition -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#333"/>
    </marker>
  </defs>
</svg>