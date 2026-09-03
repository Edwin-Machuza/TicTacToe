import csv
import os
from typing import List, Tuple


class Gerenciamento:

    def __init__(self, filepath: str = "data/jogos.csv"):
        self.filepath = filepath
        self._garantir_ficheiro_existe()

    def _garantir_ficheiro_existe(self) -> None:
        diretorio = os.path.dirname(self.filepath)
        if diretorio and not os.path.exists(diretorio):
            os.makedirs(diretorio, exist_ok=True)
        if not os.path.exists(self.filepath):
            with open(self.filepath, mode="w", newline="", encoding="utf-8") as f:
                pass

    def guardar_dados(self, jogador1: str, jogador2: str, resultado: str) -> None:
        self._garantir_ficheiro_existe()
        with open(self.filepath, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f, delimiter=";")
            writer.writerow([jogador1, jogador2, resultado])

    def ler_dados(self) -> List[Tuple[str, str, str]]:
        if not self.tem_dados():
            return []

        dados = []
        with open(self.filepath, mode="r", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=";")
            for linha in reader:
                if len(linha) == 3:
                    dados.append((linha[0], linha[1], linha[2]))
        return dados

    def tem_dados(self) -> bool:
        return os.path.exists(self.filepath) and os.path.getsize(self.filepath) > 0