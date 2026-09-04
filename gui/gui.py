import sys
import tkinter as tk
from tkinter import messagebox, simpledialog
from typing import List, Tuple, Callable, Optional
from time import time
from menu.menu import Menu
from validacoes.validacoes import validate_name


class GUI:
    TAMANHO = 3


    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.root.resizable(False, False)

        self._casa_clicada: Optional[Callable[[int, int], None]] = None

        self._buttons = [[None] * self.TAMANHO for _ in range(self.TAMANHO)]

        self.status_label = tk.Label(self.root, text="", font=("Helvetica", 13))
        self.status_label.grid(row=0, column=0, columnspan=self.TAMANHO, pady=(10, 5))

        self.board_frame = tk.Frame(self.root)
        self._construir_tabuleiro()

        self.menu = Menu(self.root, columnspan=self.TAMANHO)




    def mostrar_tela_inicial(self):
        pass


    def set_on_casa_click(self, callback: Callable[[int, int], None]) -> None:
        self._casa_clicada = callback

    def set_on_repetir_click(self, callback: Callable) -> None:
        self.menu.set_on_repetir_click(callback)

    def set_on_historico_click(self, callback: Callable) -> None:
        self.menu.set_on_historico_click(callback)

    def set_on_terminar_click(self, callback: Callable) -> None:
        self.menu.set_on_terminar_click(callback)

    def _construir_tabuleiro(self) -> None:
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                botao = tk.Button(
                    self.board_frame,
                    text="",
                    font=("Helvetica", 24, "bold"),
                    width=4,
                    height=2,
                    command=lambda l=linha, c=coluna: self._handle_casa_click(l, c),
                )
                botao.grid(row=linha, column=coluna, padx=2, pady=2)
                self._buttons[linha][coluna] = botao

    def _handle_casa_click(self, linha: int, coluna: int) -> None:
        if self._casa_clicada:
            self._casa_clicada(linha, coluna)

    def pedir_nome(self, numero_jogador: int) -> str:
        while True:
            nome = simpledialog.askstring(
                "Jogador", f"Nome do jogador {numero_jogador}:", parent=self.root
            )
            if nome is None:
                resposta = messagebox.askokcancel("Escape Door", "Deseja sair?")
                if resposta:
                    sys.exit(0)
                else:
                    valido, mensagem = validate_name(nome)
                    if valido:
                        return nome
                    messagebox.showwarning("Nome inválido", mensagem, parent=self.root)


    def atualizar_casa(self, linha: int, coluna: int, simbolo: str) -> None:
        self._buttons[linha][coluna].config(text=simbolo, state="disabled")

    def set_status(self, texto: str) -> None:
        self.status_label.config(text=texto)

    def mostrar_tabuleiro(self) -> None:
        self._limpar_casas()
        self.menu.esconder()
        self.board_frame.grid(row=1, column=0, columnspan=self.TAMANHO, padx=10, pady=10)

    def _limpar_casas(self) -> None:
        for linha in range(self.TAMANHO):
            for coluna in range(self.TAMANHO):
                self._buttons[linha][coluna].config(text="", state="normal")

    def mostrar_mensagem_fim(self, texto: str) -> None:
        messagebox.showinfo("Fim de jogo", texto, parent=self.root)


    def alterar_musica_fundo(self):
        pass


    def mostrar_menu_final(self) -> None:
        self.board_frame.grid_remove()
        self.menu.mostrar()

    def mostrar_historico(self, dados: List[Tuple[str, str, str]]) -> None:
        if not dados:
            messagebox.showinfo(
                "Histórico", "Ainda não foi jogado nenhum jogo.", parent=self.root
            )
            return

        linhas = [f"{nome1} vs {nome2} -> {resultado}" for nome1, nome2, resultado in dados]
        messagebox.showinfo("Histórico", "\n".join(linhas), parent=self.root)

    def fechar(self) -> None:
        self.root.quit()
        self.root.destroy()

    def run(self) -> None:
        self.root.mainloop()
