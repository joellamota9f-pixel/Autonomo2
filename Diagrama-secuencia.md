```mermaid
%% Diagrama de Secuencia - Generar Contraseña
sequenceDiagram
    participant U as Usuario
    participant UI as InterfazUsuario
    participant C as Controlador
    participant G as Generador
    participant E as Evaluador
    participant S as Almacenamiento

    U ->> UI: Solicita generar contraseña
    UI ->> C: Enviar parámetros
    C ->> G: Generar contraseña con CSPRNG
    G -->> C: Retornar contraseña
    C ->> E: Calcular fortaleza
    E -->> C: Nivel de seguridad
    C ->> UI: Mostrar contraseña y nivel
    U ->> UI: Guardar contraseña
    UI ->> C: Solicitud de guardado
    C ->> S: Guardar cifrado
    S -->> C: Confirmación
    C -->> UI: Confirmar guardado
