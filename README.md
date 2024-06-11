# Sincronizar Stock

Este proyecto automatiza la sincronización de stock entre una tienda PrestaShop y varios proveedores utilizando FTP o URLs para descargar archivos Excel. Esto permite gestionar de manera eficiente el stock y la disponibilidad de productos en la tienda.

## Características

- **Descarga Automática**: Capacidad de descargar ficheros Excel directamente desde URLs o servidores FTP configurados.
- **Procesamiento de Datos**: Lee y procesa los datos de stock y precios de los archivos descargados.
- **Sincronización con PrestaShop**: Actualiza el stock y el estado de los productos en la tienda PrestaShop basado en la información procesada.
- **Gestión de Etiquetas**: Etiqueta los productos según su disponibilidad y la fecha de entrega esperada del proveedor.
- **Notificaciones por Correo**: Envía resúmenes automáticos por correo electrónico sobre los cambios y el estado actual del stock.

## Tecnologías Utilizadas

- Python
- Librerías Python como Pandas para el procesamiento de datos.
- FTP para la transferencia de archivos.

## Instalación

1. Clona este repositorio:
   ```bash
   git clone URL_DEL_REPOSITORIO
