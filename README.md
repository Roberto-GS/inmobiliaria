**ERP Inmobiliaria (módulo de Odoo)**

Es un módulo personalizado de Odoo para la gestión de una inmobiliaria
Para ver la Documentación Técnico: [Documentación PDF](<docs/Documentación ERP-Odoo Inmobiliaria.pdf>)

EL PROBLEMA QUE RESUELVE
Una inmobiliaria necesitaba centralizar en un único sistema la gestión de inmuebles, propietarios, clientes, visitas y operaciones (ventas/alquileres), con reglas de negocio propias que evitaran datos inconsistentes (precios fuera de rango, formatos de DNI incorrectos, inmuebles mal configurados).

FUNCIONALIDADES
- Gestión de inmuebles (casas, pisos y oficinas) con vistas de tabla, Kanban y gráficas.
- Gestión de propietarios y clientes (compradores/arrendatarios).
- Gestión de ubicaciones, agrupadas por provincia.
- Gestión de operaciones (venta/alquiler) y visitas, con una vista de calendario.
- Generación de una ficha PDF descriptiva de cada inmueble.
- Validaciones de negocio personalizadas.

<img width="1000" height="400" alt="{EE4F6263-194E-49FF-B00A-B8B781CE57B7}" src="https://github.com/user-attachments/assets/cce19cf8-aef8-4453-8640-6e649d860aee" />

<img width="1000" height="400" alt="{7627C644-44BC-4E7D-8C4A-F2E2B0276298}" src="https://github.com/user-attachments/assets/d010bdf2-d3c2-4257-a697-841e4586aa8c" />


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
