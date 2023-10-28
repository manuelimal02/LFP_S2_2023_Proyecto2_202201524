## Business Data Analysis - Análizador Léxico y Sintáctico

## Interfaz Gráfica 

Al momento de ejecutar la aplicación, se abrirá la siguiente ventana que contiene los botones de archivo, analizar archivo y menú reporte. La función de cada botón de describirá a continuación. Además la ventana contiene una caja de texto del lado izquierdo y una consola del lado derecho.

<image src="https://i.ibb.co/vsBT8kL/INTERFAZ-GRAFICA.png">


## Archivo

Este botón abrirá un pequeño menú con las opciones de abrir, guardar, guardar como y salir.

- Abrir: Se abrirá un seleccionador de archivos en donde se puede seleccionar el archivo a cargar en la caja de texto. La única extensión de archivos permitida es BIZDATA. Al momento de seleccionar el archivo se cargará todo su contenido de forma automática en la caja de texto.

- Guardar: Permite guardar los cambios realizados en el archivo por medio del editor de texto. Si no se realizaron cambios, el archivo se guardará de igual forma. 

- Guardar Como: Permite guardar los cambios realizados en el archivo por medio del editor de texto, abriendo un seleccionador de archivos que permite cambiar el nombre y la ubicación del archivo.

- Salir: Al seleccionar esta opción se cerrará de forma automática la ventana y se detendrá la ejecución de la aplicación.

<image src="https://i.ibb.co/4g3f1rk/ARCHIVO.png">


## Analizar Archivo

Al momento de presionar el botón “analizar archivo” se realizará el análisis automáticamente del archivo BIZDATA cargado al cuadro de texto y se mostrarán los resultados del análisis en la consola. 

<image src="https://i.ibb.co/JkcL2BK/ANALIZAR.png">


## Menú Reportes

Cuando se ha analizado el archivo de entrada, se podrán exportar los reportes de tokens, errores léxicos, errores sintácticos y árbol de derivación. 

<image src="https://i.ibb.co/0KTgWWB/MENU-REPORTE.png">


## Reporte De Tokens

Cuando se presiona el botón “reporte de tokens”, se creará un archivo .html con un reporte de tokens analizados en el archivo de entrada y se abrirá automáticamente en el navegador.

<image src="https://i.ibb.co/vL7Y3Dv/REPORTE-TOKENS.png">


## Reporte De Errores Léxicos 

Cuando se presiona el botón “reporte de errores léxicos”, se creará un archivo .html con un reporte de errores léxicos analizados en el archivo de entrada y se abrirá automáticamente en el navegador. 

<image src="https://i.ibb.co/KmJ9pTC/ERRORES-L-XICOS.png">


## Reporte De Errores Sintácticos 

Cuando se presiona el botón “reporte de errores sintácticos”, se creará un archivo .html con un reporte de errores sintácticos analizados en el archivo de entrada y se abrirá automáticamente en el navegador. 

<image src="https://i.ibb.co/PgRJVx0/ERRORES-SINT-CTICOS.png">


## Árbol De Derivación 

Cuando se presiona el botón “árbol de derivación”, se creará un archivo .pdf con una gráfica de un árbol de derivación con los tokens analizados en el archivo de entrada y se abrirá automáticamente en el navegador.

<image src="https://i.ibb.co/1fFyfqG/ARBOL-DERIVACION.png">