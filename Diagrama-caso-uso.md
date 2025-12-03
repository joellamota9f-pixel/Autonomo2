```mermaid
flowchart TD
    %% Actores
    U[Usuario]
    A[Administrador]

    %% Casos de uso
    CP[Configurar parámetros de generación]
    SG[Solicitar generación de contraseña]
    EF[Evaluar fortaleza de contraseña]
    CC[Copiar contraseña al portapapeles]
    GC[Guardar contraseña en gestor local]
    DP[Definir políticas globales de seguridad]

    %% Relaciones Usuario
    U --> CP
    U --> SG
    U --> EF
    U --> CC
    U --> GC

    %% Relaciones Administrador
    A --> DP
    CP --> DP
