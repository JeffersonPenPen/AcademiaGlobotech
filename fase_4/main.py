import sys
import os

def processar_fase4():
    os.system(f'py "{os.path.join(os.path.dirname(__file__), "fase_4.py")}"')

def menu_fase4():
    while True:
        print("\n->-> TÁ NA GLOBO - FASE 4 <-<-")
        print("1. Processar CSV e Alimentar Banco de Dados")
        print("5. Voltar ao Launcher")
        print("0. Sair do Programa")
        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            processar_fase4()
            input("\nProcessamento concluído. Pressione Enter para continuar...")
        elif escolha == "5":
            print("Retornando ao launcher...")
            break
        elif escolha == "0":
            print("Encerrando o launcher.")
            sys.exit()
        else:
            print("[ERRO] Opção inválida.")

if __name__ == "__main__":
    menu_fase4()
