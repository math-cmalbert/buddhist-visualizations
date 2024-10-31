# {name} - Traditional Wheel View

## Overview
This visualization presents {name} ({tibetan} / {sanskrit} / {pali}) in the traditional wheel format.

## Visualization
```mermaid
%%{init: {'theme':'neutral', 'themeVariables': {'primaryColor': '#ffd700'}}}%%
graph TD
    subgraph Wheel["Wheel of {name}"]
        Center[Central Hub<br>Sanskrit<br>Pali<br>Tibetan]
        
        subgraph Outer_Rim
            R1[Element 1<br>Sanskrit<br>Pali<br>Tibetan]
            R2[Element 2<br>Sanskrit<br>Pali<br>Tibetan]
            R3[Element 3<br>Sanskrit<br>Pali<br>Tibetan]
            R4[Element 4<br>Sanskrit<br>Pali<br>Tibetan]
        end
        
        %% Hub to rim connections
        Center --> R1
        Center --> R2
        Center --> R3
        Center --> R4
        
        %% Rim connections
        R1 --> R2
        R2 --> R3
        R3 --> R4
        R4 --> R1
    end

    style Center fill:#ffd700
    style R1 fill:#ffebcd
    style R2 fill:#ffebcd
    style R3 fill:#ffebcd
    style R4 fill:#ffebcd
```

## Description
[Add wheel structure description]

## Notes
- Hub significance
- Rim elements relationships
- Traditional symbolism
- Meditation applications