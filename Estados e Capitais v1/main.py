from tkinter import *
import tkinter as ttk
from customtkinter import *
from random import randint, shuffle
from time import sleep

class Brasil:
    # Lista dos estados brasileiros
    estados = [
        'AC - Acre', 'AL - Alagoas', 'AP - Amapá', 'AM - Amazonas', 'BA - Bahia', 'CE - Ceará', 'DF - Distrito Federal',
        'ES - Espírito Santo', 'GO - Goiás', 'MA - Maranhão', 'MT - Mato Grosso', 'MS - Mato Grosso do Sul',
        'MG - Minas Gerais', 'PA - Pará', 'PB - Paraíba', 'PR - Paraná', 'PE - Pernambuco', 'PI - Piauí', 'RJ - Rio de Janeiro',
        'RN - Rio Grande do Norte', 'RS - Rio Grande do Sul', 'RO - Rondônia', 'RR - Roraima', 'SC - Santa Catarina',
        'SP - São Paulo', 'SE - Sergipe', 'TO - Tocantins'
    ]

    # Lista das capitais brasileiras correspondentes aos estados
    capitais = [
        'Rio Branco', 'Maceió', 'Macapá', 'Manaus', 'Salvador', 'Fortaleza', 'Brasília',
        'Vitória', 'Goiânia', 'São Luís', 'Cuiabá', 'Campo Grande', 'Belo Horizonte',
        'Belém', 'João Pessoa', 'Curitiba', 'Recife', 'Teresina', 'Rio de Janeiro',
        'Natal', 'Porto Alegre', 'Porto Velho', 'Boa Vista', 'Florianópolis',
        'São Paulo', 'Aracaju', 'Palmas'
    ]
    
class Funcoes(Brasil):  
    Pontos = 0
    def ATTPontos(self):
        Funcoes.Pontos += 1
        self.frame_Pontuacao.destroy()
        self.frame_Pontuacao = CTkFrame(master=self.frame_Capitais, width=250, height=60)
        self.frame_Pontuacao.place(relx=0.5, rely=0) 
        self.labelPontuacao = CTkLabel(master=self.frame_Pontuacao, text=f"Pontos: {Funcoes.Pontos}", font=("Comic Sans MS", 34))
        self.labelPontuacao.place(relx=0.22, rely=0.1)

    def centralizar_tela(self, tela, h, w):
        largura = h
        altura = w

        largura_tela = tela.winfo_screenwidth()
        altura_tela = tela.winfo_screenheight()

        x = (largura_tela - largura) // 2
        y = (altura_tela - altura) // 2

        posicao = f"{largura}x{altura}+{x}+{y}"
        tela.geometry(posicao)

    def mostrar_Btn_Estados(self):
        estados_embaralhado = self.estados[:]
        shuffle(estados_embaralhado)
        for enum, estado in enumerate(estados_embaralhado):
            btn = CTkButton(master=self.frame_Estados, text=estado, width=250, height=30, fg_color='black')
            btn.place(relx=0.2 if enum < 14 else 0.6, rely=0.10 + (enum % 14) * 0.05)
            btn.bind("<Button-1>", lambda event, button=btn, estado_btn=btn._text, capital_btn="vazio": self.btnJogo(event, button, estado_btn, capital_btn))

    def mostrar_Btn_Capitais(self):
        capitais_embaralhado = self.capitais[:]
        shuffle(capitais_embaralhado)

        for enum, capital in enumerate(capitais_embaralhado):
            btn = CTkButton(master=self.frame_Capitais, text=capital, width=250, height=30, fg_color='black')
            btn.place(relx=0.1 if enum < 14 else 0.5, rely=0.10 + (enum % 14) * 0.05)
            btn.bind("<Button-1>", lambda event, button=btn, estado_btn="vazio",capital_btn=btn._text: self.btnJogo(event, button, estado_btn, capital_btn))
            
    btnsApert = 0
    estado = capital = btn1 = btn2 = ''
    def btnJogo(self, event, botao, estado_btn="vazio", capital_btn="vazio"):
        Funcoes.btnsApert += 1
        
        if Funcoes.btnsApert == 1:
            
            btn1 = botao
            #btn1.configure(fg_color='yellow', text_color='black')
            btn1.destroy()
            print(btn1)
            if estado_btn == "vazio":
                Funcoes.capital = capital_btn
            if capital_btn == "vazio":
                Funcoes.estado = estado_btn
        elif Funcoes.btnsApert == 2:
            if Funcoes.Pontos == 27:
                ttk.messagebox.showinfo(title="Aviso", message=f"Você venceu, parabéns!")
            btn2 = botao
            #btn2.configure(fg_color='yellow', text_color='black')
            if estado_btn == "vazio":
                Funcoes.capital = capital_btn
            if capital_btn == "vazio":
                Funcoes.estado = estado_btn

            if self.estados.index(Funcoes.estado) == self.capitais.index(Funcoes.capital):
                print(f"O estado: {Funcoes.estado} tem como capital {Funcoes.capital}")
                self.ATTPontos()
                btn2.destroy()
                Funcoes.capital = Funcoes.estado = ''
            else:
                ttk.messagebox.showinfo(title="Aviso", message=f"Você perdeu, tente novamente.")
                self.frame_Estados.destroy()
                self.frame_Estados = CTkFrame(master=self.janela, width=640, height=720)
                self.frame_Estados.place(relx=0, rely=0)
                title = CTkLabel(master=self.frame_Estados, text="Estados e Capitais", font=("Comic Sans MS", 34))
                title.place(relx=0.1, rely=0.015)
                self.mostrar_Btn_Estados()
                self.frame_Capitais.destroy()
                self.frame_Capitais = CTkFrame(master=self.janela, width=640, height=720)
                self.frame_Capitais.place(relx=0.5, rely=0)
                self.mostrar_Btn_Capitais()
                Funcoes.Pontos = 0
                self.frame_Pontuacao.destroy()
                self.frame_Pontuacao = CTkFrame(master=self.frame_Capitais, width=250, height=60)
                self.frame_Pontuacao.place(relx=0.5, rely=0.01) 
                self.labelPontuacao = CTkLabel(master=self.frame_Pontuacao, text=f"Pontos: {Funcoes.Pontos}", font=("Comic Sans MS", 34))
                self.labelPontuacao.place(relx=0.22, rely=0.1)
                print(f"Estado e Capital não correspondem")

            Funcoes.btnsApert = 0
            

        
               
    
class App(Funcoes, Brasil):
    def __init__(self):
        self.janela = CTk()
        self.propriedadesJanela()
        self.frameEstados()
        self.frameCapitais()
        self.framePontuacao()

    def propriedadesJanela(self):
        self.janela.title("Estados e Capitais")
        #self.janela.geometry("1280x720")
        self.janela.resizable(width=False, height=False)
        #self.janela._set_appearance_mode("dark")
        self.centralizar_tela(self.janela, 1280, 720)

    def frameEstados(self):
        self.frame_Estados = CTkFrame(master=self.janela, width=640, height=720)
        self.frame_Estados.place(relx=0, rely=0)
     
        title = CTkLabel(master=self.frame_Estados, text="Estados e Capitais", font=("Comic Sans MS", 34))
        title.place(relx=0.1, rely=0.015)
        
        self.mostrar_Btn_Estados()

    def frameCapitais(self):
        self.frame_Capitais = CTkFrame(master=self.janela, width=640, height=720)
        self.frame_Capitais.place(relx=0.5, rely=0)

        self.mostrar_Btn_Capitais()

    def framePontuacao(self):
        self.frame_Pontuacao = CTkFrame(master=self.frame_Capitais, width=250, height=60)
        self.frame_Pontuacao.place(relx=0.5, rely=0.01) 
        self.labelPontuacao = CTkLabel(master=self.frame_Pontuacao, text=f"Pontos: {Funcoes.Pontos}", font=("Comic Sans MS", 34))
        self.labelPontuacao.place(relx=0.22, rely=0.1)
    

    def run(self):
        self.janela.mainloop()

app = App()
app.run()