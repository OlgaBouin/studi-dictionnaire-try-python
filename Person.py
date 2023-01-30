import math


class Person:
    _nom: str
    _prenom: str
    _sexe: str
    _taille: float
    _age: int
    _silhouette: int
    _poids: float

    def __init__(self, nom: str, prenom: str):
        self._nom = nom
        self._prenom = prenom
        self._age = 0
        self._sexe = "Masculin"
        self._taille = 0.5
        self._silhouette = "sportive"
        self._poids = 3.5

    def imc(self):
        return self._poids / math.pow(self._taille, 2)

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, new_nom: str):
        self._nom = new_nom
