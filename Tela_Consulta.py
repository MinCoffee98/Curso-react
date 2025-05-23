from tkinter import *

class TelaConsulta:
    def __init__(self, master):
        self.frame = Frame(master)

        Label(self.frame, text="Tela de Consulta", font=("roboto", 14)).pack(pady=10)

        #exemplo de campo para busca
        Label(self.frame, text="Buscar por Código:").pack(anchor='w', padx=20)
        self.busca_entry = Entry(self.frame)
        self.busca_entry.pack(anchor='w', padx=20, pady=5)

        #botão busca
        self.busca_button = Button(self.frame, text="Buscar", command=self.buscar)
        self.busca_button.pack(anchor='w', padx=20, pady=5)

        #Área para exibir resultados
        self.resultados_text = Text(self.frame, height=10, width=50)
        self.resultados_text.pack(anchor='w', padx=20, pady=5)

def mostrar(self):
    self.frame.pack(fill='both', expand=True)

def esconder(self):
    self.frame.pack_forget()

def buscar(self):
    #logica para buscar dados e exibir resultados
    codigo = self.busca_entry.get()
    #exemplo de resultado
    resultados = f"Resultados para o codigo: {codigo}\n- Item 1\n- Item 2"
    self.resultados_text.delete(1.0, END) #Limpa resultados anteriores
    self.resultados_text.insert(END, resultados) #insere novos resultados

    