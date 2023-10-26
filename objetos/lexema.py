class Lexema():
    def __init__(self, lexema, fila, columna, tipo):
        self.lexema = lexema
        self.fila=fila
        self.columna=columna
        self.tipo = tipo

    def __str__(self):
        return f"'{self.lexema}', '{self.fila}', '{self.columna}, '{self.tipo}'"