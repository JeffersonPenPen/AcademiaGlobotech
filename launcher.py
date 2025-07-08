import os

def abrir_fase(fase):
    caminho = os.path.join(fase, "main.py")
    if os.path.exists(caminho):
        os.system(f'python "{caminho}"')
    else:
        print(f"[ERRO] main.py não encontrado na pasta {fase}.")

def menu_launcher():
    while True:
        print("\n->-> OLHO NO LANCE - LAUNCHER <-<-")
        print("1. Abrir Projeto Fase 1")
        print("2. Abrir Projeto Fase 2")
        print("3. Abrir Projeto Fase 3")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            abrir_fase("fase_1")
        elif escolha == "2":
            abrir_fase("fase_2")
        elif escolha == "3":
            abrir_fase("fase_3")
        elif escolha == "0":
            print("Encerrando o launcher.")
            break
        else:
            print("[ERRO] Opção inválida.")

if __name__ == "__main__":
    menu_launcher()
