from typing import Tuple


def validate_name(name: str) -> Tuple[bool, str]:
    if not name or not name.strip():
        return False, "O nome não pode ser vazio!"
    if name[0].isdigit():
        return False, "O nome não pode começar por um número!"
    return True, "Nome válido!"