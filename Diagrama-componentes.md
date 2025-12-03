```mermaid
%% Diagrama de Componentes - Arquitectura Lógica (compatible GitHub)
flowchart TD
    IU[InterfazUsuario]
    C[Controlador]
    G[Generador]
    E[Evaluador]
    A[Almacenamiento]

    %% Relaciones
    IU <--> C
    C --> G
    C --> E
    C --> A
