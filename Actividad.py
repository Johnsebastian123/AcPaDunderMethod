from typing import List
from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str


    def __eq__(self, other):
        return self.nombre == other


class Conjunto:
    contador = 0

    def __init__(self, nombre: str):
        self.elementos: List[Elemento] = []
        self.nombre = nombre
        self.__id = Conjunto.contador
        Conjunto.contador += 1

    @property
    def id(self):
        return self.__id

    def contiene(self, elem: Elemento) -> bool:
        return elem in self.elementos

    def agregar_elemento(self, elem: Elemento):
        if not self.contiene(elem):
            self.elementos.append(elem)

    def unir(self, otro_conjunto):
        for elem in otro_conjunto.elementos:
            self.agregar_elemento(elem)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto("{} UNION {}".format(self.nombre, otro_conjunto.nombre))
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nuevos_elementos = []
        for elem in conjunto1.elementos:
            if conjunto2.contiene(elem):
                nuevos_elementos.append(elem)
        nombre = "{} INTERSECTADO {}".format(conjunto1.nombre, conjunto2.nombre)
        nuevo_conjunto = Conjunto(nombre)
        nuevo_conjunto.elementos = nuevos_elementos
        return nuevo_conjunto

    def __str__(self):
        elementos_str = ", ".join([elem.nombre for elem in self.elementos])
        return "Conjunto {}: ({})".format(self.nombre, elementos_str)