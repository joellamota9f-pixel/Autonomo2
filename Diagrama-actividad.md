```mermaid
%% Diagrama de Actividad - Generador Seguro de Contraseñas
flowchart TD
    A[Inicio] --> B[Usuario ingresa parámetros de generación]
    B --> C{¿Parámetros válidos?}
    C -- Sí --> D[Generar contraseña segura]
    C -- No --> E[Aplicar parámetros por defecto]
    E --> D
    D --> F[Evaluar fortaleza de la contraseña]
    F --> G[Mostrar contraseña y nivel de fortaleza]
    G --> H{¿Usuario quiere copiar o guardar?}
    H -- Copiar --> I[Copiar al portapapeles]
    H -- Guardar --> J[Guardar en gestor local encriptado]
    H -- Ninguna acción --> K[Fin]
    I --> K
    J --> K
