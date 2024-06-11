# Sincronizar Stock

Este proyecto automatiza la sincronización de stock entre una tienda PrestaShop y varios proveedores utilizando FTP o URLs para descargar archivos Excel. Esto permite gestionar de manera eficiente el stock y la disponibilidad de productos en la tienda.

## Características

- **Descarga Automática**: Capacidad para descargar ficheros Excel directamente desde URLs o servidores FTP configurados.
- **Procesamiento de Datos**: Lee y procesa los datos de referencias, stock, fechas y otros detalles importantes de los archivos descargados.
- **Sincronización con PrestaShop**: Actualiza el stock y el estado de los productos en la tienda PrestaShop basado en la información procesada.
- **Gestión de Etiquetas**: Etiqueta los productos según su disponibilidad y la fecha de entrega esperada del proveedor.
- **Notificaciones por Correo**: Envía resúmenes automáticos por correo electrónico sobre los cambios y el estado actual del stock.

## Bases de Datos Utilizadas

- **Base de Datos de Proveedores**: Almacena toda la configuración de los archivos Excel, incluyendo cómo descargar los ficheros y actualizar las referencias con detalles como el stock, fecha, EAN, etc.
- **Base de Datos de PrestaShop**: Utilizada para realizar acciones dentro de la tienda como activar productos, denegar pedidos, etiquetar productos según la disponibilidad, y más.

## Tecnologías Utilizadas

- **Python**: Lenguaje principal para la lógica del proyecto.
- **Pandas**: Librería de Python usada para el procesamiento y análisis de datos complejos.
- **FTP**: Protocolo usado para la transferencia segura de archivos entre el servidor de proveedores y el sistema local.
- **logging**: Utilizado para registrar la actividad del programa, lo que ayuda en la depuración y el mantenimiento del software.
- **tqdm**: Biblioteca que se utiliza para mostrar barras de progreso en la consola durante la ejecución de bucles largos.
- **smtplib**: Permite enviar correos electrónicos directamente desde Python, usado para las notificaciones de correo electrónico.
- **PyMySQL**: Librería utilizada para manejar la conexión y las operaciones con la base de datos MySQL de PrestaShop.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone [URL_DEL_REPOSITORIO](https://github.com/OscarAdrian98/Sincronizar-Stock)
