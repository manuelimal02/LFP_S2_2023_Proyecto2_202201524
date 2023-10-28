from errores.error import Error
import os
import webbrowser

def promedio_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None 
    indice_clave = lista_clave.index(clave)
    valores_clave = [registro[indice_clave] for registro in lista_registro if isinstance(registro[indice_clave], (int, float))]
    if not valores_clave:
        return 0
    promedio = sum(valores_clave) / len(valores_clave)
    return promedio

def contarsi_clave(lista_clave, lista_registro, clave, valor):
    if clave not in lista_clave:
        return None 
    indice_clave = lista_clave.index(clave)
    contador = 0
    for registro in lista_registro:
        if len(registro) > indice_clave and registro[indice_clave] == valor:
            contador += 1
    return contador

def datos_consola(lista_clave, lista_registro):
    texto_imprimir=""
    texto_imprimir+="Registros Leídos: "+"\n"
    texto_imprimir+=str(lista_clave)+"\n"
    for registro in lista_registro:
        texto_imprimir+=str(registro)+"\n"
    return texto_imprimir

def sumar_clave(lista_clave, lista_registro, campo):
    if campo not in lista_clave:
        return None
    indice_clave = lista_clave.index(campo)
    suma = sum(registro[indice_clave] for registro in lista_registro)
    return suma

def maximo_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None  
    indice_clave = lista_clave.index(clave)
    valores_clave = [registro[indice_clave] for registro in lista_registro]
    if not valores_clave:
        return 0
    maximo = max(valores_clave)
    return maximo

def minimo_clave(lista_clave, lista_registro, clave):
    if clave not in lista_clave:
        return None  
    indice_clave = lista_clave.index(clave)
    valores_clave = [registro[indice_clave] for registro in lista_registro]
    if not valores_clave:
        return 0
    minimo = min(valores_clave)
    return minimo

import webbrowser
import os

def exportar_reporte(titulo, lista_clave, lista_registro):
    nombre_archivo = "reportes/Reporte_En_Consola.html"
    html = f"""<!DOCTYPE html>
                <html>
                <meta charset="UTF-8">
                <head>
                    <title>Reporte Consola</title>
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
                    <h1>{titulo}</h1>
                    <table>
                        <tr>
                            {"".join(f"<th>{clave}</th>" for clave in lista_clave)}
                        </tr>
                        {"".join("<tr>" + "".join(f"<td>{valor}</td>" for valor in registro) + "</tr>" for registro in lista_registro)}
                    </table>
                    <h3>Reporte En Consola - Carlos Manuel Lima y Lima - 202201524</h3>
                </body>
                </html>"""
    with open(nombre_archivo, "w", encoding="utf-8") as archivo:
        archivo.write(html)

class analizador_s:
    def __init__(self):
        self.lista_clave = []
        self.lista_registro = []
        self.lista_error_sintactico = []
        self.texto_imprimir=""

    def analizador_sintactico(self, lista_lexemas):
        while lista_lexemas:
            lexema = lista_lexemas.pop(0)
            # Si se encuentra el lexema "Claves", se llena la lista_clave.
            if lexema.lexema == 'Claves':
                igual = lista_lexemas.pop(0)
                if igual.lexema == '=':
                    corchete_izq = lista_lexemas.pop(0)
                    if corchete_izq.lexema == '[':
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            if lex.lexema == '"':
                                continue
                            elif lex.lexema == ',':
                                continue
                            elif lex.lexema == ']':
                                break
                            else:
                                self.lista_clave.append(lex.lexema)
                    else:
                        self.lista_error_sintactico.append(Error("Clave","SINTÁCTICO", lexema.fila, lexema.columna))
                        self.lista_error_sintactico.append(Error("=","SINTÁCTICO", igual.fila, igual.columna))
                        self.lista_error_sintactico.append(Error(corchete_izq.lexema,"SINTÁCTICO", corchete_izq.fila, corchete_izq.columna))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            self.lista_error_sintactico.append(Error(lex.lexema, "SINTÁCTICO",lex.fila, lex.columna))
                            if lex.lexema == ']':
                                break
                else:
                    self.lista_error_sintactico.append(Error("Clave","SINTÁCTICO", lexema.fila, igual.columna))
                    self.lista_error_sintactico.append(Error(igual.lexema,"SINTÁCTICO", igual.fila, igual.columna))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        self.lista_error_sintactico.append(Error(lex.lexema, "SINTÁCTICO",lex.fila, lex.columna))
                        if lex.lexema == ']':
                            break
            # Si se encuentra el lexema "Registros", se llena la lista_registro.
            if lexema.lexema == 'Registros':
                igual = lista_lexemas.pop(0)
                if igual.lexema == '=':
                    corchete_izq = lista_lexemas.pop(0)
                    if corchete_izq.lexema == '[':
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            if lex.lexema == ']':
                                break
                            elif lex.lexema == '{':
                                nuevo_registro = []
                                while lista_lexemas:
                                    lex = lista_lexemas.pop(0)
                                    if lex.lexema == '"':
                                        continue
                                    elif lex.lexema == ',':
                                        continue
                                    elif lex.lexema == '}':
                                        self.lista_registro.append(nuevo_registro)
                                        break 
                                    else:
                                        nuevo_registro.append(lex.lexema)
                    else:
                        self.lista_error_sintactico.append(Error("Registros","SINTÁCTICO", lexema.fila, lexema.columna))
                        self.lista_error_sintactico.append(Error("=","SINTÁCTICO", igual.fila, igual.columna))
                        self.lista_error_sintactico.append(Error(corchete_izq.lexema,"SINTÁCTICO", corchete_izq.fila, corchete_izq.columna))
                        while lista_lexemas:
                            lex = lista_lexemas.pop(0)
                            self.lista_error_sintactico.append(Error(lex.lexema, "SINTÁCTICO",lex.fila, lex.columna))
                            if lex.lexema == ']':
                                break
                else:
                    self.lista_error_sintactico.append(Error("Registros","SINTÁCTICO", lexema.fila, lexema.columna))
                    self.lista_error_sintactico.append(Error(igual.lexema,"SINTÁCTICO", igual.fila, igual.columna))
                    while lista_lexemas:
                        lex = lista_lexemas.pop(0)
                        self.lista_error_sintactico.append(Error(lex.lexema, "SINTÁCTICO",lex.fila, lex.columna))
                        if lex.lexema == ']':
                            break
            # Si se encuentra el lexema "imprimir", se guarda el texto a imprimir.
            if lexema.lexema == 'imprimir':
                lexema_iz = lista_lexemas.pop(0)
                if lexema_iz.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    self.texto_imprimir+=texto.lexema
            # Si se encuentra el lexema "imprimirln", se guarda el texto a imprimir.
            if lexema.lexema == 'imprimirln':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    self.texto_imprimir+=texto.lexema
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "conteo", se llama a la función len().
            if lexema.lexema == 'conteo':
                self.texto_imprimir+="\n"
                lexema_iz = lista_lexemas.pop(0)
                if lexema_iz.lexema == '(':
                    parentesis = lista_lexemas.pop(0)
                    if parentesis.lexema == ')':
                        punto_coma = lista_lexemas.pop(0)
                        if punto_coma.lexema == ';':
                            conteo=len(self.lista_registro)
                            self.texto_imprimir+=f"Cantidad de registros: {str(conteo)}."
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "datos", se llama a la función datos_consola().
            if lexema.lexema == 'datos':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    parentesis = lista_lexemas.pop(0)
                    if parentesis.lexema == ')':
                        punto_coma = lista_lexemas.pop(0)
                        if punto_coma.lexema == ';':
                            datos=datos_consola(self.lista_clave, self.lista_registro)
                            self.texto_imprimir+=datos
            # Si se encuentra el lexema "promedio", se llama a la función promedio_clave().
            if lexema.lexema == 'promedio':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    promedio=promedio_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if promedio is None:
                                        self.lista_error_sintactico.append(Error(texto.lexema,"SINTÁCTICO", texto.fila, texto.columna))
                                    else:
                                        self.texto_imprimir+=f"El promedio de '{texto.lexema}' es: {str(promedio)}."
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "contarsi", se llama a la función contarsi_clave().
            if lexema.lexema == 'contarsi':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            coma=lista_lexemas.pop(0)
                            if coma.lexema==",":
                                numero=lista_lexemas.pop(0)
                                parentesis = lista_lexemas.pop(0)
                                if parentesis.lexema == ')':
                                    punto_coma = lista_lexemas.pop(0)
                                    if punto_coma.lexema == ';':
                                        contador=contarsi_clave(self.lista_clave, self.lista_registro, texto.lexema, numero.lexema)
                                        if contador is None:
                                            self.lista_error_sintactico.append(Error(texto.lexema,"SINTÁCTICO", texto.fila, texto.columna))
                                        else:
                                            self.texto_imprimir+=f"El número '{numero.lexema}' aparece '{str(contador)}' veces en '{texto.lexema}'."
                                    else:
                                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "sumar", se llama a la función sumar_clave().
            if lexema.lexema == 'sumar':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    suma=sumar_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if suma is None:
                                        self.lista_error_sintactico.append(Error(texto.lexema,"SINTÁCTICO", texto.fila, texto.columna))
                                    else:
                                        self.texto_imprimir+=f"La suma de '{texto.lexema}' es: {str(suma)}."
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "max", se llama a la función maximo_clave().
            if lexema.lexema == 'max':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    max=maximo_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if max is None:
                                        self.lista_error_sintactico.append(Error(texto.lexema,"SINTÁCTICO", texto.fila, texto.columna))
                                    else:
                                        self.texto_imprimir+=f"El valor máximo de '{texto.lexema}' es: {str(max)}."
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "min", se llama a la función minimo_clave().
            if lexema.lexema == 'min':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    min=minimo_clave(self.lista_clave, self.lista_registro, texto.lexema)
                                    if min is None:
                                        self.lista_error_sintactico.append(Error(texto.lexema,"SINTÁCTICO", texto.fila, texto.columna))
                                    else:
                                        self.texto_imprimir+=f"El valor mínimo de '{texto.lexema}' es: {str(min)}."
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
            # Si se encuentra el lexema "exporteReporte", se llama a la función exportar_reporte().
            if lexema.lexema == 'exportarReporte':
                self.texto_imprimir+="\n"
                lexema = lista_lexemas.pop(0)
                if lexema.lexema == '(':
                    comillas = lista_lexemas.pop(0)
                    if comillas.lexema == '"':
                        texto = lista_lexemas.pop(0)
                        comillas = lista_lexemas.pop(0)
                        if comillas.lexema == '"':
                            parentesis = lista_lexemas.pop(0)
                            if parentesis.lexema == ')':
                                punto_coma = lista_lexemas.pop(0)
                                if punto_coma.lexema == ';':
                                    self.texto_imprimir+=f"Se ha creado un reporte con el nombre: {texto.lexema}."
                                    exportar_reporte(texto.lexema, self.lista_clave, self.lista_registro)
                                else:
                                    self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                            else:
                                self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                        else:
                            self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
                    else:
                        self.lista_error_sintactico.append(Error(lexema.lexema, "SINTÁCTICO",lexema.fila, lexema.columna))
    #Función Para Crear El Reporte De Errores Sintácticos
    def reporte_errores_sintacticos(self):
        nombre_archivo = "reportes/Reporte_Errores_Sintacticos.html"
        html = f"""<!DOCTYPE html>
                    <html>
                    <meta charset="UTF-8">
                    <head>
                        <title>Error Sintáctico</title>
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
                        <h1>Reporte de Errores Sintácticos</h1>
                        <table>
                            <thead>
                                <tr>
                                    <th>Token</th>
                                    <th>Tipo</th>
                                    <th>Fila</th>
                                    <th>Columna</th>
                                </tr>
                            </thead>
                            <tbody>
        """
        for error in self.lista_error_sintactico:
            fila_html = f"""
            <tr>
                <td>{error.error}</td>
                <td>{error.tipo}</td>
                <td>{error.fila}</td>
                <td>{error.columna}</td>
            </tr>"""
            html += fila_html
        html += """
                        </tbody>
                    </table>
                    <h3>Reporte de Errores Sintácticos - Carlos Manuel Lima y Lima - 202201524</h3>
                </body>
                </html>"""
        with open(nombre_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(html)
        webbrowser.open('file://' + os.path.abspath(nombre_archivo))