```mermaid
graph LR
    subgraph Client ["Client Tier (PySide6 Desktop)"]
        direction TB
        UI["GUI (QStackedWidget, Timer)"]
        Cache[("Local Cache<br>(.json files)")]
        API["API Client<br>(backend_client.py)"]
        
        UI <-->|"User Interaction"| API
        UI <-->|"Save/Load State"| Cache
    end

    subgraph Server ["Server Tier (Flask)"]
        direction TB
        Flask["Flask REST API<br>(Routing & Logic)"]
        Storage[("File System<br>(uploads/routines/)")]
        
        Flask -->|"Save Files"| Storage
    end

    subgraph Database ["Data Tier"]
        SQLite[("SQLite3 Database<br>(Users, Syllabus, Marks)")]
    end

    %% Network Connections
    API <-->|"HTTP POST/GET<br>(JSON / Multipart)"| Flask
    
    %% Database Connections
    Flask <-->|"SQL Queries<br>(CRUD Operations)"| SQLite

    %% Styling
    classDef client fill:#005f73,stroke:#fff,stroke-width:2px,color:#fff;
    classDef server fill:#0a9396,stroke:#fff,stroke-width:2px,color:#fff;
    classDef db fill:#94d2bd,stroke:#fff,stroke-width:2px,color:#000;
    
    class UI,API,Cache client;
    class Flask,Storage server;
    class SQLite db;
```