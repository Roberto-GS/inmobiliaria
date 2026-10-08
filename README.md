**ERP Inmobiliaria (módulo de Odoo)**

Es un módulo personalizado de Odoo para la gestión integral de una inmobiliaria

EL PROBLEMA QUE RESUELVE
Una inmobiliaria necesitaba centralizar en un único sistema la gestión de inmuebles, propietarios, clientes, visitas y operaciones (ventas/alquileres), con reglas de negocio propias que evitaran datos inconsistentes (precios fuera de rango, formatos de DNI incorrectos, inmuebles mal configurados).

FUNCIONALIDADES
- Gestión de inmuebles (casas, pisos y oficinas) con vistas de tabla, Kanban y gráficas.
- Gestión de propietarios y clientes (compradores/arrendatarios).
- Gestión de ubicaciones, agrupadas por provincia.
- Gestión de operaciones (venta/alquiler) y visitas, con una vista de calendario.
- Generación de una ficha PDF descriptiva de cada inmueble.
- Validaciones de negocio personalizadas.

COMO INSTALARLO
1. Clona el repositorio dentro del directorio de addons de tu instancia de Odoo (ej. /mnt/extra-addons/), indicando que la carpeta se llame inmobiliaria (Odoo usa el nombre de la carpeta como nombre técnico del módulo):
Si descargas el ZIP en vez de clonar, renombra la carpeta resultante a inmobiliaria
2. Reinicia el servicio de Odoo
3. Activa el modo desarrollador y ve a Aplicaciones → Actualizar lista de aplicaciones
4. Busca "Inmobiliaria" e instálalo.

QUÉ APRENDÍ
- A modelar relaciones de negocio reales (1:N, N:M) en un ERP y traducirlas a restricciones de datos efectivas.
- A implementar validaciones personalizadas en Odoo más allá de los campos required por defecto.
- A trabajar con Odoo desde una máquina virtual Linux con Docker, separando el entorno de ejecución del código fuente propio.
