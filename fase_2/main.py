from analise.sistema import SistemaAnaliseEngajamento
#Classe principal que gerencia os relatórios em sistema.py
import os #Para verificar csv
import subprocess #Adicionado para retornar ao launcher.

def exibir_menu(): #Menu para Processamento de Dados e Seleção de Relatórios
    print("\n--- MENU PRINCIPAL ---")
    print("1. Processar arquivo CSV")
    print("2. Gerar Relatório de Engajamento por Conteúdo")
    print("3. Gerar Relatório de Atividade de Usuários")
    print("4. Top Conteúdos por Tempo Total Consumido")
    print("5. Voltar ao Launcher")
    print("0. Sair")
    return input("Escolha uma opção: ")

"""
Menu simples a partir de While/True para organizar o acesso
aos relatórios solicitados na diretriz do projeto.
'O main.py deve instanciar SistemaAnaliseEngajamento,
carregar os dados e apresentar as métricas.'
"""

sistema = SistemaAnaliseEngajamento()

caminho_csv = "interacoes_globo.csv"
"""
Pode ser ampliado futuramente para acessar um arquivo específico
com o endereço do csv e assim não ficar preso a apenas interacoes_globo.csv.
"""
dados_processados = False
#Processamento será inicializado pelo usuário no menu.

print("\n\nFase 2: Análise de Engajamento de Mídias Globo com Orientação a Objetos\n")

while True:
    opcao = exibir_menu()

    if opcao == "1":
        if os.path.exists(caminho_csv):
            sistema.processar_interacoes_do_csv(caminho_csv)
            dados_processados = True
            print("\nDados do arquivo CSV processados.")
        else:
            print(f"Arquivo CSV não encontrado: {caminho_csv}")

    elif opcao == "2":
        if dados_processados:
            sistema.gerar_relatorio_engajamento_conteudos() #Em sistema.py
        else:
            print("Primeiro processe o arquivo CSV (Opção 1).")

    elif opcao == "3":
        if dados_processados:
            sistema.gerar_relatorio_atividade_usuarios() #Em sistema.py
        else:
            print("Primeiro processe o arquivo CSV (Opção 1).")

    elif opcao == "4":
        if dados_processados:
            sistema.gerar_relatorio_top_conteudos_consumidos(5) #Em sistema.py
        else:
            print("Primeiro processe o arquivo CSV (Opção 1).")

    elif opcao == "5":
        import subprocess #Biblioteca para abrir o arquivo launcher.py
        print("Retornando ao launcher...")
        subprocess.run(["python", "../launcher.py"])
        break

    elif opcao == "0":
        print("Encerrando o programa.")
        break
    else:
        print("Opção inválida. Tente novamente.")
