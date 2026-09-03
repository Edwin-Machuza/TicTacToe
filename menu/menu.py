import tkinter as tk
from typing import Callable, Optional


class Menu:

    def __init__(self, container: tk.Widget, columnspan: int):
        self._columnspan = columnspan
        self.frame = tk.Frame(container)

        self._on_repetir_click: Optional[Callable] = None
        self._on_historico_click: Optional[Callable] = None
        self._on_terminar_click: Optional[Callable] = None

        self._construir_botoes()

    def set_on_repetir_click(self, callback: Callable) -> None:
        self._on_repetir_click = callback

    def set_on_historico_click(self, callback: Callable) -> None:
        self._on_historico_click = callback

    def set_on_terminar_click(self, callback: Callable) -> None:
        self._on_terminar_click = callback

    def _construir_botoes(self) -> None:
        botao_repetir = tk.Button(
            self.frame, text="Jogar novamente", width=20,
            command=self._handle_repetir_click,
        )
        botao_historico = tk.Button(
            self.frame, text="Ver histórico", width=20,
            command=self._handle_historico_click,
        )
        botao_terminar = tk.Button(
            self.frame, text="Terminar", width=20,
            command=self._handle_terminar_click,
        )
        botao_repetir.pack(pady=5)
        botao_historico.pack(pady=5)
        botao_terminar.pack(pady=5)

    def _handle_repetir_click(self) -> None:
        if self._on_repetir_click:
            self._on_repetir_click()

    def _handle_historico_click(self) -> None:
        if self._on_historico_click:
            self._on_historico_click()

    def _handle_terminar_click(self) -> None:
        if self._on_terminar_click:
            self._on_terminar_click()

    def mostrar(self) -> None:
        self.frame.grid(row=1, column=0, columnspan=self._columnspan, padx=10, pady=10)

    def esconder(self) -> None:
        self.frame.grid_remove()
