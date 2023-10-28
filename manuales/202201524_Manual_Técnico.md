## Aplicación Numérica Con Análisis Léxico

## lexema.py

La clase "Lexema" es una estructura de datos en Python diseñada para representar información sobre lexemas en el contexto de análisis léxico. Los lexemas son componentes individuales en el código fuente, como palabras clave, identificadores, operadores, números, etc. Cada objeto de esta clase representa un lexema específico y contiene detalles como su contenido, ubicación en el código fuente y tipo.


## error.py

La clase "Error" se utiliza para representar y gestionar errores relacionados con el análisis léxico y sintáctico del programa. Estos errores pueden ocurrir durante la fase de procesamiento del código fuente, lo que dificulta la comprensión y ejecución adecuada del programa. Los objetos de esta clase almacenan información como la descripción del error, su tipo, y su ubicación exacta en el código fuente (fila y columna), lo que facilita la identificación y corrección de errores en el programa.


## main.py

Este programa, escrito en Python utilizando la biblioteca Tkinter, tiene como objetivo realizar el análisis léxico y sintáctico de un código fuente. Además, proporciona la funcionalidad de generar informes y reportes basados en los resultados del análisis.

1. **Clase "ventana_principal":**
Esta clase representa la interfaz gráfica principal del programa. La ventana se crea con botones y áreas de texto para cargar, analizar y generar informes sobre un código fuente. Las funciones dentro de esta clase gestionan las operaciones principales del programa.

2. **Función cargar_archivo:**
Permite al usuario cargar un archivo de código fuente desde el sistema de archivos. El contenido del archivo se muestra en un área de texto para su posterior análisis.

3. **Función guardar_archivo:**
Guarda el contenido del archivo en la ruta seleccionada previamente, sobrescribiendo el archivo original.

4. **Función guardar_como:**
Permite al usuario seleccionar una ubicación y nombre para guardar el archivo de código fuente. Guarda el contenido del archivo en la ubicación especificada.

5. **Función salir:**
Cierra la aplicación y muestra un mensaje de despedida al usuario.

6. **Funciones reporte_tokens, reporte_errores_lexicos, reporte_errores_sintacticos, reporte_arbol_derivacion:**
Estas funciones generan informes específicos (tokens, errores léxicos, errores sintácticos, árbol de derivación) basados en el análisis previo del código fuente. Los informes se muestran al usuario en archivos html y en el caso del árbol de derivación, se genera en archivo pdf.

7. **Función analizar:**
Realiza el análisis léxico y sintáctico del código fuente que se encuentra en el área de texto. Llama a los analizadores léxicos y sintácticos para realizar estas tareas. Muestra el resultado del análisis en un área de texto separada.


8. **Inicialización y Ejecución:**
La última parte del programa crea una instancia de la clase "ventana_principal" y ejecuta la aplicación de GUI con la función root.mainloop().

## analizador_léxico.py
El código se trata de una implementación del analizador léxico de un lenguaje de programación. Este analizador léxico escanea un código fuente y divide el texto en "lexemas", que son unidades de significado en el código. Además, al encontrar errores léxicos, los registra en una lista de errores.


1. **analizador_l:** Esta es la clase principal que contiene todo el análisis léxico. En su constructor inicializa listas para almacenar lexemas y errores, y las variables de seguimiento de línea y columna.

2. **analizador_lexico:** Este método realiza el análisis léxico del código fuente. Recorre el código caracter por caracter, identifica lexemas y los clasifica en diferentes categorías, como comillas, números, palabras clave, etc. Los lexemas y errores detectados se almacenan en listas.

3. **armar_lexema:** Esta función se utiliza para armar un lexema de una cadena dada. Toma una cadena como entrada y recopila caracteres hasta encontrar un carácter que indique el final del lexema, como comillas, salto de línea o espacio. Retorna el lexema y la cadena restante.

4. **armar_cadena:** Similar a la función anterior, esta se utiliza para armar una cadena entre comillas.

5. **armar_comentario:** Esta función se utiliza para armar un comentario entre comillas simples.

6. **armar_numero:** Esta función se utiliza para armar un número, ya sea entero o decimal, de una cadena dada.

7. **reporte_tokens:** Esta función genera un informe en formato HTML que muestra los lexemas identificados en el código fuente, junto con su tipo, fila y columna correspondiente. El informe se guarda en un archivo HTML y se abre en un navegador web.

8. **reporte_errores_lexicos:** Esta función genera un informe en formato HTML que muestra los errores léxicos detectados durante el análisis léxico, incluyendo el carácter erróneo, el tipo de error, la fila y columna. El informe se guarda en un archivo HTML y se abre en un navegador web.

9. **grafica_arbol_derivación:** Esta función genera un informe en formato DOT, que se usa para crear una representación gráfica de un árbol de derivación. Luego, se utiliza Graphviz (una herramienta para generar gráficos) para convertir el archivo DOT en un archivo PDF que representa el árbol de derivación de los lexemas identificados en el código fuente.

## analizador_sintáctico.py

El código se trata de una implementación de un analizador sintáctico diseñado para procesar el código fuente. El código de análisis sintáctico recibe una lista de lexemas (que proviene de un análisis léxico previo).

1. **analizador_s:** Esta es una clase que inicia un objeto analizador_s. El constructor inicializa varias listas para almacenar información importante: lista_clave para las claves, lista_registro para los registros, y lista_error_sintactico para los errores sintácticos. Además, la variable texto_imprimir se utiliza para acumular texto que se imprimirá en la consola.

2. **analizador_sintactico:** Este método recorre la lista de lexemas y, para cada tipo de instrucción (como definir claves, registros, imprimir, etc.), realiza acciones específicas. Algunas de las acciones que realiza incluyen:

    - Recopilar las claves y registros definidos en el código.
    - Manejar las instrucciones de impresión, incluidas las funciones imprimir e imprimirln.
    - Realizar cálculos como el conteo de registros, promedio, suma, valor máximo y valor mínimo para claves específicas.
    - Exportar un informe HTML con los registros y claves a un archivo.

3. **Funciones de cálculo:** Estas son funciones auxiliares que se utilizan para calcular ciertos valores a partir de los registros y claves definidos. Estas funciones incluyen promedio_clave, contarsi_clave, sumar_clave, maximo_clave y minimo_clave.

4. **datos_consola:** Esta función toma la lista de claves y registros y la convierte en un formato de texto para su posterior impresión en la consola.

5. **exportar_reporte:** Esta función genera un informe en formato HTML que muestra las claves y registros en una tabla y lo guarda en un archivo.

6. **reporte_errores_sintacticos:** Esta función se encarga de generar un informe HTML que muestra los errores sintácticos encontrados durante el análisis.

## Expresiones Regulares

    Claves = [" "," "]
ER: Claves = [ ({ ((Cr+)|(" Cr +") , )+ })+ ]

    Registros = [{," ",}{," ",}]
ER: Registros = [ ({ ((Cr+)|(" Cr +") , )+ })+ ]

    #Comentario
ER: '#' Cr+

    '''Comentario'''
ER: ' ' ' (Cr | \n )+ ' ' '

    imprimir("");
ER: imprimir ( " Cr+ " ) ;

    implimirln("");
ER: imprimirln ( " Cr+ " ) ;

    conteo();
ER: conteo (  ) ;

    datos();
ER: datos (  ) ;

    promedio("");
ER: promedio ( " Cr+ " ) ;

    contarsi("", );
ER: contarsi ( " Cr+ " , Cr+ ) ;

    sumar("");
ER: sumar ( " Cr+ " ) ;

    max("");
ER: max ( " Cr+ " ) ;

    min("");
ER: min ( " Cr+ " ) ;

    exportarReporte("");
ER: exportarReporte ( " Cr+ " ) ;


## Método Del Árbol

    Claves = [" "," "]
<image src="https://i.ibb.co/m6fwWLP/CLAVES.png">

    Registros = [{," ",}{," ",}]
<image src="https://i.ibb.co/yPDB3bQ/REGISTROS.png">

    #Comentario
<image src="https://i.ibb.co/gSc9Vvz/COMENTARIO-NORMAL.png">

    '''Comentario'''
<image src="https://i.ibb.co/VwmGhtv/COMENATRIO-MULTI.png">

    imprimir("");
<image src="https://i.ibb.co/XLhG3PR/IMPRIMIR.jpg">

    implimirln("");
<image src="https://i.ibb.co/VMVPR3W/IMPRIMIRLN.jpg">

    conteo();
<image src="https://i.ibb.co/4srhKC2/CONTEO.png">

    datos();
<image src="https://i.ibb.co/xYny2mP/DATOS.png">

    promedio("");
<image src="https://i.ibb.co/h1zpxyP/PROMEDIO.jpg">

    contarsi("", );
<image src="https://i.ibb.co/k9mGRZx/CONTARSI.png">

    sumar("");
<image src="https://i.ibb.co/gvQf4dn/SUMA.jpg">

    max("");
<image src="https://i.ibb.co/6014ZR3/MAX.jpg">

    min("");
<image src="https://i.ibb.co/QKJfmR1/MIN.jpg">

    exportarReporte("");
<image src="https://i.ibb.co/Y3Hrt9Q/EXPORTAR-REPORTE.jpg">


## Autómata Finito Determinista

    Claves = [" "," "]
<image src="https://i.ibb.co/qgwSvc7/CLAVES.png">

    Registros = [{," ",}{," ",}]
<image src="https://i.ibb.co/9v3BV3q/REGISTROS.png">

    #Comentario
<image src="https://i.ibb.co/dLNKPtd/COMENTARIO-SIMPLE.png">

    '''Comentario'''
<image src="https://i.ibb.co/fYRdz6q/COMENTARIO-MULTI.png">

    imprimir("");
<image src="https://i.ibb.co/d4fDjBw/IMPRIMIR.png">

    implimirln("");
<image src="https://i.ibb.co/3smR9z9/IMPRIMIR-LN.png">

    conteo();
<image src="https://i.ibb.co/bmCNsk1/CONTEO.png">

    datos();
<image src="https://i.ibb.co/HzgpHNk/DATOS.png">

    promedio("");c
<image src="https://i.ibb.co/SXJYtzf/PROMEDIO.png">

    contarsi("", );
<image src="https://i.ibb.co/QvsC1WP/CONTARSI.png">

    sumar("");
<image src="https://i.ibb.co/SQFWSXd/SUMAR.png">

    max("");
<image src="https://i.ibb.co/wRYbZcb/MAX.png">

    min("");
<image src="https://i.ibb.co/bRrrT1Q/MIN.png">

    exportarReporte("");
<image src="https://i.ibb.co/CBXThB0/EXPORTAR-REPORTE.png">



## Gramática Independiente Del Contexto

    Claves = ["",""]
+ Terminales = {'Claves', Igual, Corchete Izquierdo, Corchete Derecho, Comillas, Coma, Texto}
+ No Terminales = {q0, q1, q2, q3}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= Claves Igual < q1 >
+ < q1 >::= Corchete Izquierdo < q2 > Corchete Derecho
+ < q2 >::= Comillas - Texto - Comillas < q3 >
+ < q3 >::= Coma < q2 > | e

	Registros = [{,"",} {,"",}]
+ Terminales = {'Registros', Igual, Corchete Izquierdo, Corchete Derecho, Llave Izquierda, Llave Derecha, Comillas, Coma, Texto}
+ No Terminales = {q0, q1, q2, q3, q4}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= Registros Igual < q1 >
+ < q1 >::= Corchete Izquierdo < q2 > Corchete Derecho
+ < q2 >::= Llave Izquierda < q3 > Llave Derecha
+ < q3 >::= Texto < q4 > | Comillas - Texto - Comillas < q4 >
+ < q4 >::= Coma < q3 > | e

	#Comentario
+ Terminales = {Numeral, Texto}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= Numeral < q1 >
+ < q1 >::= Texto < q2 > | e
+ < q2 >::= Texto < q1 > | e

	'''
+ Terminales = {', Texto, '\n'}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= ''' < q1 > '''
+ < q1 >::= Texto < q2 > | \n < q2 > | e
+ < q2 >::= Texto < q1 > | \n < q2 > | e

	imprimir("");
+ Terminales = {'imprimir', Paréntesis Izquierdo, Paréntesis Derecho, Texto, Comillas, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= imprimir < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas

	implimirln("");
+ Terminales = {'imprimirln', Paréntesis Izquierdo, Paréntesis Derecho, Carácter, Comillas, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= imprimirln < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas
	conteo();
+ Terminales = {'conteo', Paréntesis Izquierdo, Paréntesis Derecho, Punto Y Coma}
+ No Terminales = {q0, q1}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= conteo < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo Paréntesis Derecho

	datos();
+ Terminales = {'datos', Paréntesis Izquierdo, Paréntesis Derecho, Punto Y Coma}
+ No Terminales = {q0, q1}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= datos < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo Paréntesis Derecho

	promedio("");
+ Terminales = {'promedio', Paréntesis Izquierdo, Paréntesis Derecho, Carácter, Comilla, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= promedio < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas

	contarsi("", );
+ Terminales = {'contarsi', Paréntesis Izquierdo, Paréntesis Derecho, Coma, Carácter, Comilla, Punto Y Coma}
+ No Terminales = {q0, q1, q2, q3}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= contarsi < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas < q3 >
+ < q3 >::= Coma Texto | Coma e

	sumar("");
+ Terminales = {'sumar', Paréntesis Izquierdo, Paréntesis Derecho, Carácter, Comilla, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= sumar < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas

	max("");
+ Terminales = {'max', Paréntesis Izquierdo, Paréntesis Derecho, Carácter, Comilla, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= max < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas

	min("");
+ Terminales = {'min', Paréntesis Izquierdo, Paréntesis Derecho, carácter, comilla, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= min < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas

	exportarReporte("");
+ Terminales = {'exportarReporte', Paréntesis Izquierdo, Paréntesis Derecho, Carácter, Comillas, Punto Y Coma}
+ No Terminales = {q0, q1, q2}
+ Inicio = {q0}
+ Producciones:
+ < q0 >::= exportarReporte < q1 > Punto Y Coma
+ < q1 >::= Paréntesis Izquierdo < q2 > Paréntesis Derecho
+ < q2 >::= Comillas - Texto - Comillas