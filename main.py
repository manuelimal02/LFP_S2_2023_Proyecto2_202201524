import tkinter as tk
from tkinter import Menu
from tkinter import messagebox
from tkinter import filedialog
from tkinter import scrolledtext
from tkinter.filedialog import asksaveasfilename
from analizadores.analizador_lexico import analizador_l
from analizadores.analizador_sintactico import analizador_s

analizador_lexico=analizador_l()
analizador_sintactico=analizador_s()

class ventana_principal:

    def on_enter(self, event):
        event.widget.config(bg='GREY')

    def on_leave(self, event):
        event.widget.config(bg='#142157')

    def __init__(self, root):
        #Variable Analizado
        self.archivo_seleccionado=False
        self.archivo_analizado=False
        #Ventana Pricipal
        self.root = root
        self.root.title("PROYECTO 2 - CARLOS MANUEL LIMA Y LIMA")
        self.root.geometry("1200x700")
        self.root.configure(bg='white')
        self.root.resizable(0,0)
        #Frame Botones Opciones
        titulo_frame=tk.Frame(root,bg='#114C5F')
        #Label Titulo
        label_titulo = tk.Label(titulo_frame, text="Business Data Analysis - Análizador")
        label_titulo.pack(fill='both', expand=True)
        label_titulo.config(fg="white", bg="#114C5F", font=("Verdana", 20))
        #Configuraciones Frame
        titulo_frame.place(x=0, y=0)
        titulo_frame.pack_propagate(0)  
        titulo_frame.configure(width=1200, height=50)
        #Frame Botones Opciones
        opciones_frame=tk.Frame(root,bg='#4A6EB0')
        #Boton Cargar Archivo
        boton_archivo=tk.Menubutton(opciones_frame, text="Archivo", bg='#142157', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')        
        boton_archivo.place(x=50, y=10, width=150, height=30)
        #Opciones
        opciones=Menu(boton_archivo,tearoff=0)
        boton_archivo["menu"]=opciones
        opciones.add_command(label="Abrir", font=("Verdana", 13), activeforeground='black', command=self.cargar_archivo)
        opciones.add_command(label="Guardar", font=("Verdana", 13),  activeforeground='black', command=self.guardar_archivo)
        opciones.add_command(label="Guardar Como", font=("Verdana", 13),  activeforeground='black', command=self.guardar_como)
        opciones.add_command(label="Salir", font=("Verdana", 13), activeforeground='black', command=self.salir)
        #Boton Analizar
        boton_analizar=tk.Button(opciones_frame,text="Analizar Archivo", bg='#142157', font=("Verdana", 13), bd=0, fg='white', activeforeground='black', command=self.analizar)
        boton_analizar.place(x=250, y=10, width=150, height=30)
        boton_analizar.bind("<Enter>", self.on_enter)
        boton_analizar.bind("<Leave>", self.on_leave)
        #Boton Reporte Archivo
        boton_reporte=tk.Menubutton(opciones_frame, text="Menú Reporte", bg='#142157', font=("Verdana", 13), bd=0, fg='white', activeforeground='black')        
        boton_reporte.place(x=450, y=10, width=150, height=30)
        #Opciones
        opciones=Menu(boton_reporte,tearoff=0)
        boton_reporte["menu"]=opciones
        opciones.add_command(label="Reporte De Tokens", font=("Verdana", 13), activeforeground='black', command=self.reporte_tokens)
        opciones.add_command(label="Reporte De Errores Léxicos", font=("Verdana", 13),  activeforeground='black', command=self.reporte_errores_lexicos)
        opciones.add_command(label="Reporte De Errores Sintácticos", font=("Verdana", 13),  activeforeground='black', command=self.reporte_errores_sintacticos)
        opciones.add_command(label="Árbol De Derivación", font=("Verdana", 13),  activeforeground='black', command=self.reporte_arbol_derivacion)
        #Configuraciones Frame  
        opciones_frame.place(x=0, y=50)
        opciones_frame.pack_propagate()
        opciones_frame.configure(width=1200, height=50)
        #Frame Cuadro De Texto
        cuadrotexto_frame=tk.Frame(root,bg='#0799B6')
        #Area De Texto
        self.areatexto=scrolledtext.ScrolledText(cuadrotexto_frame, font=("Verdana", 10), bg="white", width=60, height=34)
        self.areatexto.place(x=30, y=30)
        self.consola=scrolledtext.ScrolledText(cuadrotexto_frame, font=("Verdana", 10), bg="white", width=73, height=34)
        self.consola.place(x=560, y=30)
        #Configuraciones Frame
        cuadrotexto_frame.place(x=0, y=100)
        cuadrotexto_frame.pack_propagate()
        cuadrotexto_frame.configure(width=1200, height=600)
    
    def cargar_archivo(self):
        texto_archivo = ""
        ruta = tk.Tk()
        ruta.withdraw()
        ruta.attributes('-topmost', True)
        try:
            self.ruta_seleccionada= nueva_ruta = filedialog.askopenfilename(filetypes=[("Archivos BIZDATA", f"*.bizdata")])
            with open(nueva_ruta, encoding="utf-8") as archivo:
                texto_archivo = archivo.read()
            self.texto = texto_archivo
            self.areatexto.delete(1.0, "end")
            self.areatexto.insert(1.0, self.texto)
            messagebox.showinfo("BizData", "Archivo Cargado Correctamente.")
            self.archivo_seleccionado=True
        except Exception as e:
            messagebox.showerror("Error", "No Se Ha Seleccionado Ningún Archivo.")
            return
    
    def guardar_archivo(self):
        try:
            if self.archivo_seleccionado==True:
                self.texto = self.areatexto.get(1.0, "end")
                archivo = open(self.ruta_seleccionada, 'w', encoding="utf-8")
                archivo.write(self.texto)
                messagebox.showinfo("BizData", "Archivo Guardado Correctamente.")
            else:
                messagebox.showwarning("Error", "No Se Ha Seleccionado Ningún Archivo.")
            return
        except Exception as e:
            messagebox.showerror("Error", "No Se Ha Seleccionado Ningún Archivo.")
            return

    def guardar_como(self):
        try:
            if self.archivo_seleccionado==True:
                self.texto = self.areatexto.get(1.0, "end")
                self.archivo = asksaveasfilename(filetypes=[("Archivos BIZDATA", f"*.bizdata")], defaultextension=[("Archivos BIZDATA", f"*.bizdata")], initialfile=" ")
                archivo = open(self.archivo, 'w', encoding="utf-8")
                archivo.write(self.texto)
                messagebox.showinfo("BizData", "Archivo Guardado Correctamente.")
            else:
                messagebox.showwarning("Error", "No se ha seleccionado ningún archivo.")
            return
        except Exception as e:
            messagebox.showerror("Error", "No se ha seleccionado ningún archivo.")
            return

    def salir(self):
        try:
            messagebox.showinfo("BizData", "Gracias Por Utilizar El Programa.")
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error: {str(e)}")

    def reporte_tokens(self):
        try:
            if self.archivo_analizado == True:
                messagebox.showinfo("BizData", "Reporte Tokens Creado Correctamente.")
                analizador_lexico.reporte_tokens()
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error: {str(e)}")

    def reporte_errores_lexicos(self):
        try:
            if self.archivo_analizado == True:
                messagebox.showinfo("BizData", "Reporte Errores Léxicos Creado Correctamente.")
                analizador_lexico.reporte_errores_lexicos()
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error: {str(e)}")

    def reporte_errores_sintacticos(self):
        try:
            if self.archivo_analizado == True:
                messagebox.showinfo("BizData", "Reporte Errores Sintácticos Creado Correctamente.")
                analizador_sintactico.reporte_errores_sintacticos()
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error: {str(e)}")
    
    def reporte_arbol_derivacion(self):
        try:
            if self.archivo_analizado == True:
                messagebox.showinfo("BizData", "Reporte Arbol Derivación Creado Correctamente.")
                analizador_lexico.grafica_arbol_derivación()
            else:
                messagebox.showerror("Error", "No se ha realizado el análisis de archivo.")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error: {str(e)}")

    def analizar(self):
        try:
            self.archivo_analizado=True
            codigo_fuente = self.areatexto.get(1.0, tk.END)
            #Se Vacían Las Listas del Analizador_Lexico
            analizador_lexico.lista_lexemas.clear()
            analizador_lexico.lista_errores.clear()
            analizador_lexico.n_linea = 1
            analizador_lexico.n_columna = 1
            #Se Vacían Las Listas del Analizador_Sintactico
            analizador_sintactico.lista_clave.clear()
            analizador_sintactico.lista_registro.clear()
            analizador_sintactico.lista_error_sintactico.clear()
            analizador_sintactico.texto_imprimir=""
            #Se Limpia La Caja De Texto
            self.consola.delete(1.0, tk.END)
            #Se Llama Al Analizador Léxico
            analizador_lexico.analizador_lexico(codigo_fuente)
            #Se crea Una Copia Del La Lista_Lexemas
            lista_lexemas_local=[]
            lista_lexemas_local=analizador_lexico.lista_lexemas.copy()
            #Se Llama Al Analizador Sintáctico
            analizador_sintactico.analizador_sintactico(lista_lexemas_local)
            self.consola.config(state='normal')
            self.consola.delete(1.0, tk.END)
            self.consola.insert(1.0, analizador_sintactico.texto_imprimir)
            self.consola.config(state='disabled')
            messagebox.showinfo("BizData", "Código Analizado Correctamente.")
        except Exception as e:
            messagebox.showerror("Error", f"Se ha producido un error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    aplicacion = ventana_principal(root)
    root.mainloop()