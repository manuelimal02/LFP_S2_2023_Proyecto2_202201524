from objetos.lexema import Lexema
from errores.error import Error
import os
import webbrowser

class analizador_l:

    def __init__(self):
        self.lista_lexemas = []
        self.lista_errores = []
        self.n_linea = 1
        self.n_columna = 1

    #Función Para Analizar Toda La Cadena
    def analizador_lexico(self, cadena):
        lexema = ''
        puntero = 0
        while cadena:
            char = cadena[puntero]
            puntero += 1
            #Si Se Encuentra Una Comilla, Se Arma Una Cadena
            if char == '"':
                nuevo_lexema = Lexema('"', self.n_linea, self.n_columna, 'COMILLA')
                self.lista_lexemas.append(nuevo_lexema)
                lexema, cadena = self.armar_cadena(cadena[puntero:])
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'TEXTO')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('"', self.n_linea, self.n_columna, 'COMILLA')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra Una Comilla Simple, Se Arma Un Comentario
            elif char == "'": 
                nuevo_lexema = Lexema("'", self.n_linea, self.n_columna, 'COMILLA-SIMPLE')
                self.lista_lexemas.append(nuevo_lexema)
                lexema, cadena = self.armar_comentario(cadena[puntero:])
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'COMENTARIO')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema("'", self.n_linea, self.n_columna, 'COMILLA-SIMPLE')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra Una Comilla Simple, Se Arma Una Cadena Como Comentario
            elif cadena.startswith("#"):
                lexema, cadena = self.armar_cadena(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'COMENTARIO')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
            #Si Se Encuentra La Palabra "Clave", Se Arma Una Cadena
            elif cadena.startswith("Claves"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'CLAVES')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
            #Si Se Encuentra La Palabra "Registros", Se Arma Una Cadena
            elif cadena.startswith("Registros"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'REGISTROS')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
            #Si Se Encuentra La Palabra "imprimirln", Se Arma Una Cadena
            elif cadena.startswith("imprimirln"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'IMPRIMIRLN')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "imprimir", Se Arma Una Cadena
            elif cadena.startswith("imprimir"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'IMPRIMIR')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "conteo", Se Arma Una Cadena
            elif cadena.startswith("conteo"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'CONTEO')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "conteo", Se Arma Una Cadena
            elif cadena.startswith("promedio"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'PROMEDIO')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "contarsi", Se Arma Una Cadena
            elif cadena.startswith("contarsi"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'CONTAR-SI')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "datos", Se Arma Una Cadena
            elif cadena.startswith("datos"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'DATOS')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "sumar", Se Arma Una Cadena
            elif cadena.startswith("sumar"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'SUMAR')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "max", Se Arma Una Cadena
            elif cadena.startswith("max"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'MAX')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "min", Se Arma Una Cadena
            elif cadena.startswith("min"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'MIN')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra La Palabra "exportarReporte", Se Arma Una Cadena
            elif cadena.startswith("exportarReporte"):
                lexema, cadena = self.armar_lexema(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, 'EXPORTAR-REPORTE')
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(lexema) + 1
                    puntero = 0
                nuevo_lexema = Lexema('(', self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                self.n_columna += 1
                puntero = 0
            #Si Se Encuentra Un Cero, Se Arma Un Numero Como Lexema
            elif char=="0":
                nuevo_lexema = Lexema(0, self.n_linea, self.n_columna, 'NUMERO')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Un Numero, Se Arma Un Numero Como Lexema
            elif char.isdigit():
                lexema, cadena = self.armar_numero(cadena)
                if lexema and cadena:
                    self.n_columna += 1
                    nuevo_lexema = Lexema(lexema, self.n_linea, self.n_columna, "NUMERO")
                    self.lista_lexemas.append(nuevo_lexema)
                    self.n_columna += len(str(lexema)) + 1
                    puntero = 0
            #Si Se Encuentra Un Corchete, Se Guarda Un Corchete Como Lexema
            elif char == '[' or char == ']':
                nuevo_lexema = Lexema(char, self.n_linea, self.n_columna, 'CORCHETE')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Una Llave, Se Guarda Una Llave Como Lexema
            elif char == '{' or char == '}':
                nuevo_lexema = Lexema(char, self.n_linea, self.n_columna, 'LLAVE')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Un Punto y Coma, Se Guarda Un Punto y Coma Como Lexema
            elif char == ';':
                nuevo_lexema = Lexema(char, self.n_linea, self.n_columna, 'PUNTOYCOMA')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Un Igual, Se Guarda Un Igual Como Lexema
            elif char == '=':
                nuevo_lexema = Lexema(char, self.n_linea, self.n_columna, 'IGUAL')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Una Coma, Se Guarda Una Coma Como Lexema
            elif char == ',':
                nuevo_lexema = Lexema(char, self.n_linea, self.n_columna, 'COMA')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Un Parentesis, Se Guarda Un Parentesis Como Lexema
            elif char=="(" or char == ')':
                nuevo_lexema = Lexema(char, self.n_linea, self.n_columna, 'PARENTESIS')
                self.lista_lexemas.append(nuevo_lexema)
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1
            #Si Se Encuentra Una Tabulación, Se Agrega 4 Espacios Como Columna
            elif char == "\t":
                self.n_columna += 4
                cadena = cadena[4:]
                puntero = 0
            #Si Se Encuentra Un Salto De Linea, Se Agrega 1 Espacio Como Columna Y Una Fila
            elif char == "\n":
                cadena = cadena[1:]
                puntero = 0
                self.n_linea += 1
                self.n_columna = 1
            #Si Se Encuentra Un Espacio En Blanco, Se Agrega 1 Espacio Como Columna
            elif char == ' ' or char == '\r':
                self.n_columna += 1
                cadena = cadena[1:]
                puntero = 0
            #Se Agrega El Caracter Como Error Léxico
            else:
                self.lista_errores.append(Error(char, "LÉXICO",self.n_linea, self.n_columna))
                cadena = cadena[1:]
                puntero = 0
                self.n_columna += 1

    #Función Para Armar Un Lexema
    def armar_lexema(self, cadena):
        lexema = ''
        puntero = ''
        for char in cadena:
            puntero += char
            if char == '"' or char == '\n' or char == '\t' or char == '(' or char == ')' or char == ' ':
                return lexema, cadena[len(puntero):]   
            else:
                lexema += char
        return None, None

    #Función Para Armar Una Cadena
    def armar_cadena(self, cadena):
        lexema = ''
        puntero = ''
        for char in cadena:
            puntero += char
            if char == '"' or char == '\n':
                return lexema, cadena[len(puntero):]   
            else:
                lexema += char
        return None, None

    #Función Para Armar Un Comentario
    def armar_comentario(self, cadena):
        lexema = ''
        puntero = ''
        for char in cadena:
            puntero += char
            if char == "'":
                return lexema, cadena[len(puntero):]   
            else:
                lexema += char
        return None, None

    #Función Para Armar Un Número
    def armar_numero(self, cadena):
        numero = ''
        puntero = ''
        is_decimal =  False
        for char in cadena:
            puntero += char
            if char == '.':
                is_decimal = True
            if char==',' or char==')' or char == ' ' or char == '\n' or char == '\t' or char=='}':
                if is_decimal:
                    return float(numero), cadena[len(puntero)-1:]
                else:
                    return int(numero), cadena[len(puntero)-1:]
            elif char != ',' or char != ')':
                    numero += char
        return None, None

    #Función Para Crear El Reporte De Tokens
    def reporte_tokens(self):
        nombre_archivo = "reportes/Reporte_Tokens.html"
        html = f"""<!DOCTYPE html>
                    <html>
                    <meta charset="UTF-8">
                    <head>
                        <title>Reporte Tokens</title>
                        <style>
                            body {{
                                font-family: Courier, monospace;
                                background-color: white;
                                margin: 0;
                                padding: 0;
                            }}
                            h1 {{
                                text-align: center;
                                color: black;
                                padding: 10px;
                            }}
                            table {{
                                width: 80%;
                                margin: 20px auto;
                                border-collapse: collapse;
                                background-color: #ecf0f1;
                            }}
                            th, td {{
                                border: 1px solid #3498db;
                                padding: 10px;
                                text-align: left;
                            }}
                            th {{
                                background-color: #3498db;
                                color: white;
                            }}
                            tr:nth-child(even) {{
                                background-color: #d5dbdb;
                            }}
                            tr:nth-child(odd) {{
                                background-color: #ecf0f1;
                            }}
                            h3 {{
                                text-align: center;
                                margin-top: 20px;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1>Reporte de Tokens</h1>
                        <table>
                            <thead>
                                <tr>
                                    <th>Token</th>
                                    <th>Lexema</th>
                                    <th>Fila</th>
                                    <th>Columna</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for lexema in self.lista_lexemas:
            fila = f"""
            <tr>
                <td>{lexema.tipo}</td>
                <td>{lexema.lexema}</td>
                <td>{lexema.fila}</td>
                <td>{lexema.columna}</td>
            </tr>"""
            html += fila
        html += """
                        </tbody>
                    </table>
                    <h3>Reporte de Tokens - Carlos Manuel Lima y Lima - 202201524</h3>
                </body>
                </html>"""
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)
        webbrowser.open('file://' + os.path.abspath(nombre_archivo))


    #Función Para Crear El Reporte De Errores Léxicos

    def reporte_errores_lexicos(self):
        nombre_archivo = "reportes/Reporte_Errores_Lexicos.html"
        html = f"""<!DOCTYPE html>
                    <html>
                    <meta charset="UTF-8">
                    <head>
                        <title>Errores Léxicos</title>
                        <style>
                            body {{
                                font-family: Courier, monospace;
                                background-color: white;
                                margin: 0;
                                padding: 0;
                            }}
                            h1 {{
                                text-align: center;
                                color: black;
                                padding: 10px;
                            }}
                            table {{
                                width: 80%;
                                margin: 20px auto;
                                border-collapse: collapse;
                                background-color: #ecf0f1;
                            }}
                            th, td {{
                                border: 1px solid #3498db;
                                padding: 10px;
                                text-align: left;
                            }}
                            th {{
                                background-color: #3498db;
                                color: white;
                            }}
                            tr:nth-child(even) {{
                                background-color: #d5dbdb;
                            }}
                            tr:nth-child(odd) {{
                                background-color: #ecf0f1;
                            }}
                            h3 {{
                                text-align: center;
                                margin-top: 20px;
                            }}
                        </style>
                    </head>
                    <body>
                        <h1>Reporte de Errores Léxicos</h1>
                        <table>
                            <thead>
                                <tr>
                                    <th>Token</th>
                                    <th>Tipo</th>
                                    <th>Fila</th>
                                    <th>Columna</th>
                                </tr>
                            </thead>
                            <tbody>"""
        for error in self.lista_errores:
            fila = f"""
            <tr>
                <td>{error.error}</td>
                <td>{error.tipo}</td>
                <td>{error.fila}</td>
                <td>{error.columna}</td>
            </tr>"""
            html += fila
        html += """
                        </tbody>
                    </table>
                    <h3>Reporte de Errores Léxicos - Carlos Manuel Lima y Lima - 202201524</h3>
                </body>
                </html>"""
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)
        webbrowser.open('file://' + os.path.abspath(nombre_archivo))


    def grafica_arbol_derivación(self):
        lista_lexema = self.lista_lexemas.copy()
        nombre_archivo = "reportes/Reporte_Árbol_Derivación"
        f = open(nombre_archivo + '.dot', 'w')
        texto_g = """
            graph "" {bgcolor="#f2f2f2" gradientangle=90 label="Árbol De Derivación - Carlos Manuel Lima y Lima - 202201524"
                fontname="Courier New"
                node [fontname="Courier New"]
                edge [fontname="Courier New"]"""
        contador_subgrafo=1
        contador_nodo=1
        while lista_lexema:
            lexema = lista_lexema.pop(0)
            if lexema.lexema == "imprimir" or  lexema.lexema == "imprimirln" or  lexema.lexema == "conteo" or  lexema.lexema == "promedio" or  lexema.lexema == "contarsi" or lexema.lexema == "datos" or lexema.lexema == "sumar" or  lexema.lexema == "max" or  lexema.lexema == "min" or  lexema.lexema == "exportarReporte":
                nodo_actual = lexema.lexema
                texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+nodo_actual+f'"'+""" style="filled" gradientangle="270"\n"""
                contador_actual=contador_nodo
                contador_nodo+=1
                texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=doublecircle, label="""+f'"'+nodo_actual+f'"'+"""];\n"""
                while lista_lexema:
                    lex = lista_lexema[0]
                    if lex.lexema == ';':
                        texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                        texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                        break
                    if lex.lexema !='"':
                        texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                        texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                        contador_nodo+=1
                    else:
                        texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+"``"+f'"'+"""];\n"""
                        texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                        contador_nodo+=1
                    lista_lexema.pop(0)
                texto_g += """\n}\n"""
                contador_subgrafo+=1
                contador_nodo+=1
            elif lexema.lexema == "Claves" or lexema.lexema=="Registros":
                nodo_actual = lexema.lexema
                texto_g+= """subgraph cluster0"""+str(contador_subgrafo)+"""{label="""+f'"'+nodo_actual+f'"'+""" style="filled" gradientangle="270"\n"""
                contador_actual=contador_nodo
                contador_nodo+=1
                texto_g += """n00"""+str(contador_actual)+"""[fillcolor="#d43440", style=filled, shape=doublecircle, label="""+f'"'+nodo_actual+f'"'+"""];\n"""
                while lista_lexema:
                    lex = lista_lexema[0]
                    if lex.lexema == ']':
                        texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                        texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                        break
                    if lex.lexema =='{' or lex.lexema=='}':
                        texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#085879", style=filled, shape=circle, label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                        texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                        contador_nodo+=1
                    elif lex.lexema !='"':
                        texto_g += """n00"""+str(contador_nodo)+""" [fillcolor="#65babf", style=filled, shape=circle, label="""+f'"'+str(lex.lexema)+f'"'+"""];\n"""
                        texto_g += """n00"""+str(contador_actual)+ """--"""+ """n00"""+str(contador_nodo)+""" ;\n"""
                        contador_nodo+=1
                    lista_lexema.pop(0)
                texto_g += """\n}\n"""
                contador_subgrafo+=1
                contador_nodo+=1
        texto_g += """\n}"""
        f.write(texto_g)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpdf {nombre_archivo}.dot -o {nombre_archivo}.pdf')
        webbrowser.open('D:/USAC/4 Cuarto Semestre/Lenguajes Formales Y De Programación Laboratorio/PROYECTO-2/reportes/Reporte_Árbol_Derivación.pdf')
