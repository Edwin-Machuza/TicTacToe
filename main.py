import tkinter as tk



from controller.controller import Controller
from gerenciamento.gerenciamento import Gerenciamento
from gui.gui import GUI


def main():
    root = tk.Tk()

    gui = GUI(root)
    gerenciamento = Gerenciamento(filepath="data/jogos.csv")
    controller = Controller(gui, gerenciamento)

    controller.iniciar_jogo()
    gui.run()


if __name__ == "__main__":
    main()