
# JavaFormatChecker

Este proyecto es un verificador de formato de código Java, que se encarga de revisar si el código Java cumple con las reglas de formato establecidas en el archivo de configuración, que por defecto es: google-checks.xml.

## Requisitos

Deberá tener instalado en su máquina: java 8 o superior, maven y git. Se asumirá que ya se tiene instalado java y git. Para la instalación de maven debe dirigirse a la página oficial de maven y seguir las instrucciones de instalación. 
- Deberá instalar maven usando el siguiente enlace: [https://maven.apache.org/download.cgi](https://maven.apache.org/download.cgi), en la sección "Files" deberá buscar "Binary zip archive" y descargar la última versión.
- Lo anterior le deberá descargar un archivo zip, el cual deberá descomprimir en la carpeta que desee. En mi caso, lo descomprimí en la carpeta "C:\Program Files\Maven\apache-maven-x.x.x".
- Luego, copian la ruta de la carpeta "bin" de maven, en mi caso sería "C:\Program Files\Maven\apache-maven-x.x.x\bin" y la agregan a las variables de entorno del sistema.
- Para agregar la ruta a las variables de entorno, deberán buscar "Variables de entorno" en la barra de búsqueda de Windows y dar clic en "Editar las variables de entorno del sistema".
- Luego, en la ventana que se abre, dar clic en "Variables de entorno".
- En la sección "Variables del sistema", dar clic en "Path" y luego en "Editar".
- Dar clic en "Nuevo" y pegar la ruta que copiaron anteriormente.
- Dar clic en "Aceptar" en todas las ventanas que se abrieron.
- Para verificar que maven se instaló correctamente, deberán abrir una terminal y escribir "mvn -v". Si se instaló correctamente, deberán ver la versión de maven que instalaron.
- Si no ven la versión de maven, deberán reiniciar la terminal.
- Luego simplemente deberán clonar este repositorio

## Uso
Una vez clonado este repositorio podrá ejecutar el verificador de formato de código Java. Para ello primero deberán incluir todos sus paquetes/clases dentro de /demo/src/main/java y luego digirgirse a la carpeta /demo y ejecutar el siguiente comando:

```bash
mvn site
```

Esto generará un reporte en la carpeta /demo/target/site, el cual podrán abrir en su navegador usando el archivo index.html. O opcionalmente podrán abrir el archivo /demo/target/checkstyle-result.xml para ver los errores en formato XML, en un navegador o en un editor de texto de preferencia.

Este archivo XML va a contener los errores de formato de código Java que no cumplan con las reglas establecidas en el archivo de configuración google-checks.xml, 