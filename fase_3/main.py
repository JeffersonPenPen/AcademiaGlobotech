import os
from analise.sistema_fase3 import SistemaAnaliseEngajamento

sistema = SistemaAnaliseEngajamento()


def carregar_csv():
    caminho = "data/interacoes_globo.csv"
    if os.path.exists("path.txt"):
        with open("path.txt", "r", encoding="utf-8") as f:
            path_custom = f.read().strip()
            if os.path.exists(path_custom):
                caminho = path_custom

    if os.path.exists(caminho):
        sistema.carregar_interacoes_csv(caminho)
    else:
        print("[ERRO] Arquivo CSV não encontrado. Verifique o caminho.")


def menu_relatorios():
    while True:
        print("\n->-> RELATÓRIOS <-<-")
        print("1. Top Conteúdos por Consumo")
        print("2. Usuários com Maior Engajamento")
        print("3. Engajamento por Plataforma")
        print("4. Conteúdos Mais Comentados")
        print("5. Total de Interações por Tipo")
        print("6. Tempo Médio por Plataforma")
        print("7. Comentários por Conteúdo")
        print("0. Voltar")

        op = input("Escolha uma opção: ")
        if op == "1":
            sistema.relatorio1_top_conteudos_por_consumo()
        elif op == "2":
            sistema.relatorio2_usuarios_mais_engajados()
        elif op == "3":
            sistema.relatorio3_engajamento_por_plataforma()
        elif op == "4":
            sistema.relatorio4_conteudos_mais_comentados()
        elif op == "5":
            sistema.relatorio5_total_interacoes_por_tipo()
        elif op == "6":
            sistema.relatorio6_tempo_medio_por_plataforma()
        elif op == "7":
            sistema.relatorio7_comentarios_por_conteudo()
        elif op == "0":
            break
        else:
            print("[ERRO] Opção inválida.")


def menu_ajuda():
    print("\n->-> AJUDA <-<-")
    print("\n1. Carregar Dados")
    print("- O arquivo com os dados deve estar em formato CSV UTF-8.")
    print("- Se estiver em outro diretório, informe o caminho no arquivo 'path.txt'.")
    print("- Caso não seja encontrado, você receberá uma mensagem de erro.")
    print("\n2. Processar Interações")
    print("- Processa os dados carregados em uma fila e distribui para as árvores.")
    print("- Essa etapa é obrigatória antes de acessar os relatórios.")
    print("\n3. Relatórios")
    print("- Exibe os relatórios estatísticos com base nas interações processadas.")
    print("- Após a visualização, digite 0 para retornar ao menu principal.")
    print("\n0. Sair")
    print("- Encerra a execução do programa.")


def main():
    while True:
        print("\n->-> OLHO NO LANCE 3.0 <-<-")
        print("1. Carregar Dados")
        print("2. Processar Interações da Fila")
        print("3. Relatórios")
        print("4. Ajuda")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            carregar_csv()
        elif escolha == "2":
            sistema.processar_interacoes()
        elif escolha == "3":
            menu_relatorios()
        elif escolha == "4":
            menu_ajuda()
        elif escolha == "0":
            print("Encerrando...")
            break
        else:
            print("[ERRO] Opção inválida.")


if __name__ == "__main__":
    main()
