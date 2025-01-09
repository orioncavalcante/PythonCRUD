import customtkinter as ctk
from db import criar_conexao, criar_cursor

def abrir_tela_cadastro(janela_principal):
    # Criar uma nova janela
    cadastro_janela = ctk.CTkToplevel()
    cadastro_janela.title("Tela de Cadastro")
    cadastro_janela.geometry("400x400")
    cadastro_janela.resizable(False, False)

    # Fazer a janela aparecer na frente
    cadastro_janela.lift()
    cadastro_janela.focus_force()

    # Desabilitar a janela principal enquanto a de cadastro está aberta
    janela_principal.attributes("-disabled", True)

    # Quando a janela de cadastro for fechada, reativar a janela principal
    def fechar_cadastro():
        janela_principal.attributes("-disabled", False)
        cadastro_janela.destroy()

    # Widgets na janela de cadastro
    label_cadastro = ctk.CTkLabel(master=cadastro_janela, text="Cadastro", font=("Roboto", 20))
    label_cadastro.pack(pady=20)

    nome_cadastro = ctk.CTkEntry(master=cadastro_janela, placeholder_text="Nome de usuário", width=300, font=("", 14))
    nome_cadastro.pack(pady=10)

    email_cadastro = ctk.CTkEntry(master=cadastro_janela, placeholder_text="Email", width=300, font=("", 14))
    email_cadastro.pack(pady=10)

    senha_cadastro = ctk.CTkEntry(master=cadastro_janela, placeholder_text="Digite sua senha", width=300, font=("", 14), show="*")
    senha_cadastro.pack(pady=10)

    confirmar_senha = ctk.CTkEntry(master=cadastro_janela, placeholder_text="Confirme sua senha", width=300, font=("", 14), show="*")
    confirmar_senha.pack(pady=10)

    cadastrar_btn = ctk.CTkButton(master=cadastro_janela, text="Cadastrar", width=300, command=lambda: cadastrar(nome_cadastro, email_cadastro, senha_cadastro, confirmar_senha))
    cadastrar_btn.pack(pady=20)

    voltar_btn = ctk.CTkButton(master=cadastro_janela, text="Voltar", width=300, command=fechar_cadastro)
    voltar_btn.pack(pady=10)

    def cadastrar(nome_cadastro, email_cadastro, senha_cadastro, confirmar_senha):
        # Obter os valores dos campos
        nome = nome_cadastro.get()
        email = email_cadastro.get()
        senha = senha_cadastro.get()
        confirmar = confirmar_senha.get()

        # Verificar se todos os campos foram preenchidos
        if nome and email and senha and confirmar:
            if senha == confirmar:
                try:
                    # Criar nova conexão e cursor para a operação de inserção
                    conexao = criar_conexao()
                    cursor = criar_cursor(conexao)

                    comando_inserir = "INSERT INTO usuarios (nome_usuario, senha, email) VALUES (%s, %s, %s)"
                    cursor.execute(comando_inserir, (nome, senha, email))
                    conexao.commit()
                    print("Cadastro realizado com sucesso!")
                    fechar_cadastro()
                except Exception as e:
                    print("Erro ao cadastrar:", e)
                finally:
                    # Fechar o cursor e a conexão ao finalizar
                    if cursor:
                        cursor.close()
                    if conexao:
                        conexao.close()
            else:
                print("As senhas não coincidem!")
        else:
            print("Por favor, preencha todos os campos.")
