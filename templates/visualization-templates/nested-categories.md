# {name} - Nested Categories View

## Overview
This visualization presents {name} ({tibetan} / {sanskrit} / {pali}) showing hierarchical relationships between categories.

## Visualization
```mermaid
%%{init: {'theme':'neutral', 'themeVariables': {'primaryColor': '#ffd700'}}}%%
graph TD
    subgraph Main_Category["Main Category"]
        A[Primary Element<br>Sanskrit<br>Pali<br>Tibetan]
    end

    subgraph Sub_Category_1["First Level"]
        B[Sub-element 1<br>Sanskrit<br>Pali<br>Tibetan]
        C[Sub-element 2<br>Sanskrit<br>Pali<br>Tibetan]
    end

    subgraph Sub_Category_2["Second Level"]
        D[Detail 1<br>Sanskrit<br>Pali<br>Tibetan]
        E[Detail 2<br>Sanskrit<br>Pali<br>Tibetan]
        F[Detail 3<br>Sanskrit<br>Pali<br>Tibetan]
    end

    A --> B
    A --> C
    B --> D
    B --> E
    C --> F

    style A fill:#ffd700
    style B fill:#ffebcd
    style C fill:#ffebcd
    style D fill:#f0f0f0
    style E fill:#f0f0f0
    style F fill:#f0f0f0
```

## Description
[Add description of categorical relationships]

## Notes
- Category definitions
- Relationships between levels
- Traditional classifications
- Applications in study and practice