from typing import List, Optional, Tuple


class Board:
    TAMANHO = 3

    def __init__(self):
        self._grelha = [[None] * self.TAMANHO for _ in range(self.TAMANHO)]

    def reset(self) -> None:
        self._grelha = [[None] * self.TAMANHO for _ in range(self.TAMANHO)]

    def place(self, linha: int, coluna: int, simbolo: str) -> None:
        if not self.is_valid_move(linha, coluna):
            raise ValueError(f"Jogada inválida na posição ({linha}, {coluna})")
        self._grelha[linha][coluna] = simbolo

    def is_valid_move(self, linha: int, coluna: int) -> bool:
        dentro_dos_limites = 0 <= linha < self.TAMANHO and 0 <= coluna < self.TAMANHO
        return dentro_dos_limites and self._grelha[linha][coluna] is None

    def get_cell(self, linha: int, coluna: int) -> Optional[str]:
        return self._grelha[linha][coluna]

    def get_grid(self) -> List[List[Optional[str]]]:
        return [linha[:] for linha in self._grelha]

    def is_full(self) -> bool:
        return all(self._grelha[l][c] is not None
                   for l in range(self.TAMANHO)
                   for c in range(self.TAMANHO))

    def get_winner_symbol(self) -> Optional[str]:
        for linha in self._todas_as_linhas():
            valores = [self._grelha[l][c] for l, c in linha]
            if valores[0] is not None and all(v == valores[0] for v in valores):
                return valores[0]
        return None

    def _todas_as_linhas(self) -> List[List[Tuple[int, int]]]:
        linhas = []
        for i in range(self.TAMANHO):
            linhas.append([(i, c) for c in range(self.TAMANHO)])
            linhas.append([(r, i) for r in range(self.TAMANHO)])
        linhas.append([(i, i) for i in range(self.TAMANHO)])
        linhas.append([(i, self.TAMANHO - 1 - i) for i in range(self.TAMANHO)])
        return linhas