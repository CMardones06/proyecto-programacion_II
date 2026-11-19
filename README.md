# Proyecto programación II

"Una empresa necesita una aplicación de escritorio que permita administrar el ingreso y la salida de
vehículos de un estacionamiento, calcular sus cobros y consultar los ingresos obtenidos. La empresa
ofrece tres modalidades de pago: por minuto, diaria y mensual.Una empresa necesita una aplicación de escritorio que permita administrar el ingreso y la salida de
vehículos de un estacionamiento, calcular sus cobros y consultar los ingresos obtenidos. La empresa
ofrece tres modalidades de pago: por minuto, diaria y mensual."

## Instrucciones de ejecución e instalación:

Aún no hay programa así que aún no hay instrucciones :b 

## Intrgrantes y usuarios de GitHub:

- Camila Mardones | CMardones06
- Catalina Ojeda | c-ojeda

## Distribución de tareas:

| Área | Catalina Ojeda: Operaciones y cobros | Camila Mardones: Persistencia, consultas y reportes |
|---|---|---|
| Lógica en Python | Implementa la clase abstracta y las tres modalidades de cobro, con atributos privados, getters, setters y cálculo polimórfico. Programa el registro de vehículos, los ingresos, las salidas y la contratación mensual. Valida ingresos duplicados, vigencia y superposición de suscripciones. | Implementa los modelos de vehículo, estadía, suscripción y pago en SQLAlchemy, con sus relaciones y restricciones. Configura SQLite, la creación de tablas y el manejo de commit() y rollback(). Implementa las consultas de vehículos presentes, historial y pagos. |
| Tkinter | Implementa los formularios para registrar vehículos, ingresos, salidas y suscripciones. Muestra el monto al cerrar una estadía y agrega mensajes de confirmación y error. | Implementa las tablas de vehículos presentes e historial de estadías y pagos, los filtros por patente, fecha y modalidad, y la vista de recaudación total y por modalidad. | 
| Programación Funcional | Revisar junto a Camila que el reporte coincida con los cobros que generan las operaciones. | Implementa filter, map, reduce y lambda en las consultas y reportes. Dos funciones puras pueden ser filtrar pagos por período y modalidad y sumar los montos de los pagos recibidos. El reporte usa la fecha de registro del pago. |
| Entregables | Prepara el README con tarifas, ejemplo de uso, nombres, usuarios de GitHub y distribución de tareas. Dibuja la jerarquía de cobro en el UML y redacta la sección de POO del informe. Arma en ZIP | Prepara requirements.txt y los datos de ejemplo con fechas predefinidas. Completa las instrucciones de instalación y ejecución, las relaciones del ORM en el UML y las secciones de persistencia y programación funcional del informe. Descomprime y ejecuta el ZIP y el programa siguiendo las instrucciones del README.|
| Pruebas | Comprueba el ingreso y la salida, que 1 min 10 s se cobre como 2 minutos, que 24 h se cobren como 1 día y 24 h 1 min como 2 días. Verifica también el rechazo de un segundo ingreso activo, de las suscripciones superpuestas y de una salida anterior al ingreso. | Comprueba que los datos sobrevivan a un reinicio, que los filtros funcionen, que el pago mensual aparezca una sola vez en la recaudación y que un fallo al guardar un pago revierta toda la operación. | 

### Tareas en conjunto:

- Crear el repositorio compartido, verificar el acceso del docente y acordar las tarifas, la estructura de módulos y los nombres y parámetros de las operaciones que unen Tkinter, negocio y persistencia.
- Durante el desarrollo, hacer commits progresivos desde sus propias cuentas y revisar mutuamente los cambios que conectan sus módulos.
- Después de la primera integración, ejecutar desde Tkinter un registro, un ingreso y una salida por minuto, y comprobar que el pago aparezca en el reporte.
- Demostrar que una suscripción vigente cubre una estadía aunque venza antes de la salida, y que un ingreso exactamente a la hora del vencimiento ya no recibe cobertura. Confirmar que la estadía cubierta no genera un segundo pago y que los errores de entrada permiten seguir usando la aplicación.
- Cerrar el informe y el UML comprobando que coincidan con el código final.
- Para cada prueba, anotar los datos de entrada, el resultado esperado, el obtenido y la evidencia.
- Indicar las limitaciones que hayan identificado.
- Probar desde Tkinter que una estadía iniciada con suscripción vigente quede cubierta aunque venza antes de la salida, y que un ingreso justo al vencer la suscripción ya no tenga cobertura.
- Comprobar que las entradas inválidas muestren un mensaje y permitan seguir usando la aplicación. Cada persona registra en el informe el resultado esperado, el obtenido y la evidencia de sus pruebas.

## Programa:

### Valores de tarifas:

No definidas

### Ejemplos de uso:

No hechos ni definidos
