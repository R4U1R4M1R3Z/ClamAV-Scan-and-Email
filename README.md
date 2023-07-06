# Script de Escaneo y Envío de Correo con ClamAV

Este script Python ejecuta un escaneo utilizando ClamAV en un directorio  y luego envía el resultado del escaneo por correo electrónico. Puedes programar la ejecución automática del script utilizando el crontab.

## Requisitos

- ClamAV instalado en tu sistema.
- Python 3 instalado.

## Configuración

Antes de utilizar el script, asegúrate de realizar los siguientes pasos de configuración:

1. Abre el archivo `exClamscan.py` en un editor de texto.
2. Actualiza las variables de configuración de correo electrónico en el encabezado del script:
   - `smtp_server`: Dirección del servidor SMTP.
   - `smtp_port`: Puerto del servidor SMTP.
   - `smtp_username`: Nombre de usuario para autenticación SMTP.
   - `smtp_password`: Contraseña para autenticación SMTP.
   - `sender_email`: Dirección de correo electrónico del remitente.
   - `recipient_email`: Dirección de correo electrónico del destinatario.
3. Guarda los cambios realizados en el archivo.

## Ejecución manual

Puedes ejecutar manualmente el script `exClamscan.py` utilizando el siguiente comando:

```
python3 exClamscan.py
```

Esto ejecutará el escaneo utilizando ClamAV en el directorio especificado y enviará el resultado por correo electrónico.

## Programación en crontab

Para programar la ejecución automática del script utilizando el crontab, sigue estos pasos:

1. Abre una terminal o consola de comandos.
2. Ejecuta el siguiente comando para editar el crontab:
   ```
   crontab -e
   ```
3. Si se te solicita, elige el editor de texto que prefieras (como nano o vim).
4. Añade la siguiente línea al final del archivo crontab para ejecutar el script por ejemplo todos los días a las 14:30:
   ```
   30 14 * * * python3 /ruta/al/script/exClamscan.py
   ```
   Asegúrate de reemplazar `/ruta/al/script` con la ubicación real del archivo `exClamscan.py` en tu sistema.
5. Guarda y cierra el archivo.
6. El script ahora se ejecutará automáticamente todos los días a las 14:30 según la programación establecida en el crontab.
