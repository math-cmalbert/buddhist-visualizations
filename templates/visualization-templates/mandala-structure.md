# {name} - Mandala Structure View

## Overview
This visualization presents {name} ({tibetan} / {sanskrit} / {pali}) in traditional mandala format.

## Visualization
```mermaid
%%{init: {'theme':'neutral', 'themeVariables': {
    'primaryColor': '#ffd700',
    'secondaryColor': '#ff0000',
    'tertiaryColor': '#0000ff',
    'quaternaryColor': '#00ff00',
    'quinaryColor': '#ffffff'
}}}%%
graph TD
    subgraph Mandala
        C[Center<br>Sanskrit<br>Pali<br>Tibetan]
        
        subgraph East
            E[East Gate<br>Sanskrit<br>Pali<br>Tibetan]
        end
        
        subgraph South
            S[South Gate<br>Sanskrit<br>Pali<br>Tibetan]
        end
        
        subgraph West
            W[West Gate<br>Sanskrit<br>Pali<br>Tibetan]
        end
        
        subgraph North
            N[North Gate<br>Sanskrit<br>Pali<br>Tibetan]
        end

        C --> E
        C --> S
        C --> W
        C --> N
    end

    style C fill:#ffd700
    style E fill:#ff0000
    style S fill:#0000ff
    style W fill:#00ff00
    style N fill:#ffffff
```

## Description
[Add mandala structure description]

## Notes
- Directional significance
- Color symbolism
- Center-periphery relationships
- Traditional applications
- Meditation instructions