import customtkinter as ctk
from db import criar_conexao, criar_cursor

def abrir_tela_cadastro(janela_principal):
    cadastro_janela = ctk.CTkToplevel()
    cadastro_janela.title("Tela de Cadastro")
    cadastro_janela.geometry("400x400")
    cadastro_janela.resizable(False, False)

    janela_principal.attributes("-disabled", True)

    def fechar_cadastro():
        janela_principal.attributes("-disabled", False)
        cadastro_janela.destroy()

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

    def cadastrar():
        nome = nome_cadastro.get()
        email = email_cadastro.get()
        senha = senha_cadastro.get()
        confirmar = confirmar_senha.get()

        if nome and email and senha and confirmar:
            if senha == confirmar:
                try:
                    conexao = criar_conexao()
                    cursor = criar_cursor(conexao)

                    comando_inserir = "INSERT INTO usuarios (nome_usuario, senha, email) VALUES (%s, %s, %s)"
                    cursor.execute(comando_inserir, (nome, senha, email))
                    conexao.commit()
                    fechar_cadastro()
                except Exception as e:
                    print("Erro ao cadastrar:", e)
                finally:
                    if cursor:
                        cursor.close()
                    if conexao:
                        conexao.close()
            else:
                print("As senhas não coincidem!")
        else:
            print("Por favor, preencha todos os campos.")

    cadastrar_btn = ctk.CTkButton(master=cadastro_janela, text="Cadastrar", width=300, command=cadastrar)
    cadastrar_btn.pack(pady=20)

    voltar_btn = ctk.CTkButton(master=cadastro_janela, text="Voltar", width=300, command=fechar_cadastro)
    voltar_btn.pack(pady=10)
