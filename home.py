import customtkinter as ctk
from db import criar_conexao, criar_cursor
from cadastro_transacao import nova_transacao_screen

def abrir_pagina_inicial():
    """Abre a página inicial após login bem-sucedido."""
    pagina_inicial = ctk.CTk()
    pagina_inicial.title("Página Inicial")
    pagina_inicial.geometry("800x600")

    # Conteúdo da página inicial
    label_bem_vindo = ctk.CTkLabel(
        master=pagina_inicial, 
        text="Bem-vindo à Página Inicial!", 
        font=("Roboto", 24), 
        text_color="green"
    )
    label_bem_vindo.pack(pady=30)

    nova_transacao = ctk.CTkButton(master=pagina_inicial, text="Cadastrar Transação", width=300, command=nova_transacao_screen)
    nova_transacao.pack(pady=15)

    # Exibe transações e resumo financeiro
    listar_transacoes(pagina_inicial)
    
    botao_sair = ctk.CTkButton(
        master=pagina_inicial, 
        text="Sair", 
        command=pagina_inicial.destroy
    )
    botao_sair.pack(pady=20)

    pagina_inicial.mainloop()

def listar_transacoes(pagina_inicial):
    # Exibir transações e resumo financeiro
    try:
        conexao = criar_conexao()
        cursor = criar_cursor(conexao)

        query = "SELECT * FROM transacoes"
        cursor.execute(query)
        transacoes = cursor.fetchall()

        # Exibir as transações
        for transacao in transacoes:
            transacao_texto = f"Categoria: {transacao[4]} - Valor: {transacao[3]} - Descrição: {transacao[5]}"
            label_transacao = ctk.CTkLabel(master=pagina_inicial, text=transacao_texto, font=("Roboto", 12))
            label_transacao.pack(pady=5)
        
        # Calcular o saldo
        query_saldo = "SELECT SUM(valor) FROM transacoes"
        cursor.execute(query_saldo)
        saldo = cursor.fetchone()[0]
        if saldo is None:
            saldo = 0
        
        # Exibir saldo
        label_saldo = ctk.CTkLabel(master=pagina_inicial, text=f"Saldo: {saldo:.2f}", font=("Roboto", 16, "bold"), text_color="blue")
        label_saldo.pack(pady=15)
    
    except Exception as e:
        print("Erro ao listar transações:", e)
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
