```mermaid
%% Diagrama de Despliegue - Arquitectura Física
flowchart LR
    %% Nodos
    Navegador["Aplicación Web / Escritorio"]
    API["API Backend - Python"]
    BD["Base de Datos cifrada"]

    %% Clases de colores
    classDef cliente fill:#DDEEFF,stroke:#333,stroke-width:1px;
    classDef servidor fill:#FFEEDD,stroke:#333,stroke-width:1px;

    class Navegador cliente;
    class API,BD servidor;

    %% Relaciones
    Navegador --> API
    API --> BD
