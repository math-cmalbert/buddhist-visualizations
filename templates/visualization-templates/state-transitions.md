# {name} - State Transitions View

## Overview
This visualization presents {name} ({tibetan} / {sanskrit} / {pali}) as transformational states.

## Visualization
```mermaid
stateDiagram-v2
    direction TB
    
    [*] --> State1
    note right of State1
        Sanskrit
        Pali
        Tibetan
    end note

    State1 --> State2: Transition 1
    note right of State2
        Sanskrit
        Pali
        Tibetan
    end note
    
    State2 --> State3: Transition 2
    note right of State3
        Sanskrit
        Pali
        Tibetan
    end note

    State3 --> [*]: Completion

    state State1 {
        [*] --> sub1: Initial
        sub1 --> sub2: Development
        sub2 --> [*]: Completion
    }

    state State2 {
        [*] --> sub3: Beginning
        sub3 --> [*]: Fulfillment
    }
```

## Description
[Add description of state transformations]

## Notes
- Transition points
- Requirements for progression
- Common obstacles
- Signs of attainment