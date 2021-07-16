
from tkinter import *

from tkinter import messagebox as mb

import json

#classe que define os componentes da GUI
class Quiz:
# Este é o primeiro método que é chamado quando um
# novo objeto da classe é inicializado. Este método
# define a contagem de perguntas para 0. e inicializa todos os
# outras funções para exibir o conteúdo e fazer com que todas as
# funcionalidade disponível
	def __init__(self):
		
		# definir o número da pergunta para 0
		self.q_no=0
		
		# atribui perguntas à função display_question para atualizar mais tarde.
		self.display_title()
		self.display_question()		

		# opt_selected contém um valor inteiro que é usado para
		# opção selecionada em uma questão.
		self.opt_selected=IntVar()
		
		# exibindo botão de opção para a pergunta atual e usado para
		# opções de exibição para a pergunta atual
		self.opts=self.radio_buttons()
		
		# dismostra as opções
		self.display_options()
		
		# mostra os botoes de proximo e de quit
		self.buttons()
		
		# numero de questoes
		self.data_size=len(question)
		
		# contador de respostas corretas
		self.correct=0



   # Este método é usado para exibir o resultado
   # Conta o número de respostas corretas e erradas
   # e depois exibi-los no final como uma caixa de mensagem
	def display_result(self):
		
		wrong_count = self.data_size - self.correct
		correct = f"Correct: {self.correct}"
		wrong = f"Wrong: {wrong_count}"
		
		# calculando a porcentagemdas respostas corretas
		score = int(self.correct / self.data_size * 100)
		result = f"Score: {score}%"
		
		#message box com os resultados
		mb.showinfo("Result", f"{result}\n{correct}\n{wrong}")


	# Esse metado checa a resposta dps de clicarmos em "próximo"
	def check_ans(self, q_no):
		
		# checa se a resposta está correta
		if self.opt_selected.get() == answer[q_no]:
			# Se a alternativa estiver correta retorna True
			return True

   # Este método é usado para verificar a resposta do
   # questão atual chamando o check_ans e a pergunta no.
   # se a pergunta estiver correta aumenta a contagem em 1
   # e aumente o número da pergunta em 1. Se for a última
   # pergunta então chama display result para mostrar a caixa de mensagem.
   # caso contrário, mostra a próxima pergunta.
	def next_btn(self):
		
		# Checar a resposta
		if self.check_ans(self.q_no):
			
			# se a resposta estiver correta incrementa 1
			self.correct += 1
		
		self.q_no += 1
		
		if self.q_no==self.data_size:
			
			self.display_result()
			
			gui.destroy()
		else:
			# mostra a proxima questao
			self.display_question()
			self.display_options()


	def buttons(self):
		
		#botão de proximo
		next_button = Button(gui, text="Próximo",command=self.next_btn,
		width=10,bg="blue",fg="white",font=("ariel",16,"bold"))
		
	
		next_button.place(x=350,y=380)
		
		# Tbotao de sair
		quit_button = Button(gui, text="Quit", command=gui.destroy,
		width=5,bg="black", fg="white",font=("ariel",16," bold"))
		

		quit_button.place(x=700,y=50)


   # Este método desmarca o botão de opção na tela
   # Em seguida, é usado para exibir as opções disponíveis para o atual
   # pergunta que obtemos por meio do número da pergunta e das atualizações
   # cada uma das opções para a questão atual do botão de rádio.
	def display_options(self):
		val=0
		
		# retirar marcação
		self.opt_selected.set(1)
		
      # repetindo as opções a serem exibidas para o
      # texto dos botões de rádio.
		for option in options[self.q_no]:
			self.opts[val]['text']=option
			# PhotoImage(imagens[self.q_no])
			val+=1

	# def display_images(self):
    # 	val=0

	# 	self.opt_selected.set(1)

	# 	for imagem in imagens[self.q_no]:
    # 		self.opts[val]['image']=imagem
	# 		val+=1
   # Este método mostra a questão atual na tela
	def display_question(self):
		
		# propriedades das questoes
		q_no = Label(gui, text=question[self.q_no], width=60,
			font=( 'ariel' ,16, 'bold' ), anchor= 'w')

		
		q_no.place(x=70, y=100)


	# mostrar o titulo
	def display_title(self):
		
		# Ttitulo
		title = Label(gui, text="De onde é o som?",
		width=50, bg="green",fg="white", font=("ariel", 20, "bold"))
		
		# posicao
		title.place(x=0, y=2)


	# Este método mostra os botões de rádio para selecionar a questão
	# na tela na posição especificada. Ele também retorna um
	# lsit do botão de opção que será usado posteriormente para adicionar as opções a
	# eles.
	def radio_buttons(self):
		
      # inicializar a lista com uma lista vazia de opções
		q_list = []
		
		# posição da primeira opção
		y_pos = 150
		
		# adicionando as opções à lista
		while len(q_list) < 4:
			
			# propiedades dos botões
			# radio_btn = Radiobutton(gui,text=" ",variable=self.opt_selected,
			# value = len(q_list)+1, font = ("ariel",14))
			radio_btn = Radiobutton(gui,text = '',variable=self.opt_selected,
				value = len(q_list)+1, font = ("ariel",14), image='')
			# , imagem=PhotoImage(imagens[self.q_no])
			
			# adicionando botão a lista
			q_list.append(radio_btn)
			
			# posicao
			radio_btn.place(x = 100, y = y_pos)
			
			# incrementando y em 40
			y_pos += 40
		
		# reta os radiobuttons
		return q_list

# Criar a janela 
gui = Tk()

# Definindo o tamanho da janela
gui.geometry("800x450")

# O titulo
gui.title("De onde é o som")

# abrindo o json data
with open('data.json') as f:
	data = json.load(f)


# definindos as perguntas e respostas
question = (data['question'])
options = (data['options'])
answer = (data[ 'answer'])
imagens = (data['imagens'])

# criando obj Quiz
quiz = Quiz()


gui.mainloop()

