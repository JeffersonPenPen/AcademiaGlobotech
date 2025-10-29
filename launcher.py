import os

def abrir_fase(fase):
    launcher = os.path.join(os.path.dirname(__file__), fase)
    caminho = os.path.join(launcher, "main.py")
    if os.path.exists(caminho):
        os.chdir(launcher)
        os.system(f'python "main.py"')
    else:
        print(f"[ERRO] main.py não encontrado na pasta {fase}.")


def menu_launcher():
    while True:
        print("\n->-> TÁ NA GLOBO - LAUNCHER <-<-")
        print("1. Projeto Fase 1")
        print("2. Projeto Fase 2")
        print("3. Projeto Fase 3")
        print("4. Projeto Fase 4")
        print("0. Sair")

        escolha = input("Escolha uma opção: ")
        if escolha == "1":
            abrir_fase("fase_1")
        elif escolha == "2":
            abrir_fase("fase_2")
        elif escolha == "3":
            abrir_fase("fase_3")
        elif escolha == "4":
            abrir_fase("fase_4")
        elif escolha == "0":
            print("Encerrando o launcher.")
            break
        else:
            print("[ERRO] Opção inválida.")

if __name__ == "__main__":
    menu_launcher()
