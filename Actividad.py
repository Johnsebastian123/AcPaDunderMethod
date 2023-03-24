from typing import List
from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str


    def __eq__(self, other):
        return self.nombre == other


