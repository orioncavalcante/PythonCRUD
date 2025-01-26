import customtkinter as ctk
from PIL import Image
from tela_cadastro import abrir_tela_cadastro
from db import criar_conexao, criar_cursor
from home import abrir_pagina_inicial

# Configurações iniciais
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

# Criar janela principal
janela = ctk.CTk()
janela.title("Tela de Login")
janela.geometry("700x400")
janela.resizable(False, False)

# Imagem da tela de login
imagem = Image.open("login.png")
img = ctk.CTkImage(light_image=imagem, dark_image=imagem, size=(350, 300))
label_img = ctk.CTkLabel(master=janela, image=img, text="")  # Remove texto
label_img.place(x=5, y=10)

label_tt = ctk.CTkLabel(master=janela, text="Entre ou cadastre-se agora!", font=("Roboto", 20), text_color="#00B0F0")
label_tt.place(x=50, y=10)

# Frame
login_frame = ctk.CTkFrame(master=janela, width=350, height=380)
login_frame.place(x=340, y=10)

# Widgets do frame
label = ctk.CTkLabel(master=login_frame, text="Sistema de Login", font=("", 20), text_color="white")
label.place(x=25, y=5)

# Campos de entrada
nome_inserir = ctk.CTkEntry(master=login_frame, placeholder_text="Nome de usuário", width=300, font=("", 14))
nome_inserir.place(x=25, y=105)
label_nome = ctk.CTkLabel(master=login_frame, text="O campo nome de usuário é obrigatório!", text_color="green", font=("", 10))
label_nome.place(x=25, y=135)

senha_inserir = ctk.CTkEntry(master=login_frame, placeholder_text="Digite sua senha", width=300, font=("", 14), show="*")
senha_inserir.place(x=25, y=175)
label_senha = ctk.CTkLabel(master=login_frame, text="O campo Digite sua senha é obrigatório!", text_color="green", font=("", 10))
label_senha.place(x=25, y=205)

checkbox = ctk.CTkCheckBox(master=login_frame, text="Lembrar de mim")
checkbox.place(x=25, y=235)

# Função para login
def realizar_login():
    nome = nome_inserir.get()
    senha = senha_inserir.get()
    
    if nome and senha:
        if ler_banco(nome, senha):  # Chame a função que verifica o login
            print("Login realizado com sucesso!")
            janela.withdraw()  # Esconde a janela de login
            abrir_pagina_inicial()  # Abre a página inicial
        else:
            print("Nome de usuário ou senha incorretos.")
    else:
        print("Por favor, preencha todos os campos.")

# Botão de login
login_button = ctk.CTkButton(master=login_frame, text="Login", width=300, command=realizar_login)
login_button.place(x=25, y=285)

# Botão de cadastro
label_cadastro = ctk.CTkLabel(master=login_frame, text="Não possui uma conta?")
label_cadastro.place(x=25, y=325)
cadastrar_btn = ctk.CTkButton(master=login_frame, text="Cadastre-se", width=150, command=lambda: abrir_tela_cadastro(janela))
cadastrar_btn.place(x=175, y=325)

# Função para verificar login no banco de dados
def ler_banco(nome, senha):
    try:
        conexao = criar_conexao()  # Cria a conexão
        cursor = criar_cursor(conexao)  # Cria o cursor

        # Query com placeholders para evitar injeção de SQL
        query = "SELECT * FROM usuarios WHERE nome_usuario = %s AND senha = %s"
        cursor.execute(query, (nome, senha))
        
        # Busca o resultado
        resultado = cursor.fetchone()

        if resultado:
            print("Usuário encontrado:", resultado)
            return True
        else:
            print("Nome de usuário ou senha incorretos.")
            return False
    except Exception as e:
        print("Erro ao verificar usuário:", e)
        return False
    finally:
        if cursor:
            cursor.close()  # Fecha o cursor
        if conexao:
            conexao.close()  # Fecha a conexão

# Rodar janela
janela.mainloop()
