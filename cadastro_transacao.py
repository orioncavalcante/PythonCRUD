import customtkinter as ctk
from db import criar_conexao, criar_cursor

def nova_transacao_screen():
    cadastrar = ctk.CTk()
    cadastrar.title("Cadastrar Transação")
    cadastrar.geometry("400x300")

    # Widgets de cadastro de transação
    label_bem_vindo = ctk.CTkLabel(
        master=cadastrar, 
        text="Cadastre uma nova transação", 
        font=("Roboto", 24), 
        text_color="green"
    )
    label_bem_vindo.pack(pady=20)

    tipo = ctk.CTkComboBox(master=cadastrar, values=["Entrada", "Saída"], width=300, font=("", 14))
    tipo.pack(pady=10)

    valor = ctk.CTkEntry(master=cadastrar, placeholder_text="Valor", width=300, font=("", 14))
    valor.pack(pady=10)

    categoria = ctk.CTkEntry(master=cadastrar, placeholder_text="Categoria", width=300, font=("", 14))
    categoria.pack(pady=10)

    descricao = ctk.CTkEntry(master=cadastrar, placeholder_text="Descrição", width=300, font=("", 14))
    descricao.pack(pady=10)

    cadastrar_btn = ctk.CTkButton(master=cadastrar, text="Cadastrar", width=300, command=lambda: cadastrar_transacao(tipo, valor, categoria, descricao))
    cadastrar_btn.pack(pady=20)

    cadastrar.mainloop()

def cadastrar_transacao(tipo, valor, categoria, descricao):
    tipo_valor = tipo.get()
    valor_valor = valor.get()
    categoria_valor = categoria.get()
    descricao_valor = descricao.get()

    if tipo_valor and valor_valor and categoria_valor and descricao_valor:
        try:
            conexao = criar_conexao()
            cursor = criar_cursor(conexao)

            comando_inserir = "INSERT INTO transacoes (tipo, valor, categoria, descricao, data) VALUES (%s, %s, %s, %s, CURDATE())"
            cursor.execute(comando_inserir, (tipo_valor, valor_valor, categoria_valor, descricao_valor))
            conexao.commit()
            print("Transação cadastrada com sucesso!")
            

        except Exception as e:
            print("Erro ao cadastrar transação:", e)
        finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()
    else:
        print("Por favor, preencha todos os campos.")
