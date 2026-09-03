
from typing import Optional, Tuple, Union
from entidades.jogador import Jogador
from entidades.board import Board
from gerenciamento.gerenciamento import Gerenciamento
from gui.gui import GUI
import pygame


class Controller:

    def __init__(self, gui: GUI, gerenciamento: Gerenciamento):
        self.gui = gui
        self.gerenciamento = gerenciamento
        self.board = Board()

        self.jogador1: Optional[Jogador] = None
        self.jogador2: Optional[Jogador] = None
        self.simbolo_jogador1: str = "X"
        self.simbolo_jogador2: str = "O"
        self.simbolo_atual: str = "X"

        self.gui.set_on_casa_click(self.finalizar_casa)
        self.gui.set_on_repetir_click(self.repetir)
        self.gui.set_on_historico_click(self.ver_historico)
        self.gui.set_on_terminar_click(self.terminar)

        pygame.mixer.init()

        self.tocar_musica_fundo("music/cartoon.mp3")


    def tocar_musica_fundo(self, caminho_arquivo: str):
        try:
            pygame.mixer.music.load(caminho_arquivo)

            pygame.mixer.music.play(-1)
           
            pygame.mixer.music.set_volume(.3)
        except Exception as e:
           print(f"Erro ao carregar áudio: {e}")
            
            
    def iniciar_jogo(self):
        nome1 = self.gui.pedir_nome(1)
        nome2 = self.gui.pedir_nome(2)

        self.jogador1 = Jogador(nome1)
        self.jogador2 = Jogador(nome2)

        self.board.reset()
        self.simbolo_atual = "X"

        self.gui.mostrar_tabuleiro()
        self.gui.set_status(f"{self.simbolo_atual} joga ({self.obter_nome_por_simbolo(self.simbolo_atual)})")

    def finalizar_casa(self, linha: int, coluna: int):
        if not self.board.is_valid_move(linha, coluna):
            return

        self.board.place(linha, coluna, self.simbolo_atual)
        self.gui.atualizar_casa(linha, coluna, self.simbolo_atual)

        resultado = self.verificar_fim()

        if resultado == 2:
            self.trocar_vez()
            self.gui.set_status(f"{self.simbolo_atual} joga ({self.obter_nome_por_simbolo(self.simbolo_atual)})")
            return

        self.fim_jogo(resultado)

    def trocar_vez(self):
        self.simbolo_atual = "O" if self.simbolo_atual == "X" else "X"

    def verificar_fim(self) -> Union[Tuple[int, str], int]:
        vencedor = self.board.get_winner_symbol()
        if vencedor is not None:
            return 0, vencedor

        if self.board.is_full():
            return 1

        return 2

    def fim_jogo(self, resultado: Union[Tuple[int, str], int]):
        if resultado == 1:
            texto_resultado = "Empate"
            mensagem = "Empate!"
            self.gui.set_status("Fim da Partida")
        else:
            self.gui.set_status("Fim da Partida")
            _, simbolo_vencedor = resultado
            nome_vencedor = self.obter_nome_por_simbolo(simbolo_vencedor)
            texto_resultado = nome_vencedor
            mensagem = f"{nome_vencedor} venceu!"

        self.gerenciamento.guardar_dados(
            self.jogador1.nome, self.jogador2.nome, texto_resultado
        )

        self.gui.mostrar_mensagem_fim(mensagem)
        self.gui.mostrar_menu_final()

    def obter_nome_por_simbolo(self, simbolo: str) -> str:
        if simbolo == self.simbolo_jogador1:
            return self.jogador1.nome
        return self.jogador2.nome

    def repetir(self):
        self.iniciar_jogo()

    def ver_historico(self):
        self.gui.set_status("")
        dados = self.gerenciamento.ler_dados()
        self.gui.mostrar_historico(dados)

    def terminar(self):
        pygame.mixer.music.stop()
        
        self.gui.fechar()