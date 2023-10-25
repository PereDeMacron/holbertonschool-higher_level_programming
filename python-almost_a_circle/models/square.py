#!/usr/bin/python3
from models.rectangle import Rectangle


class Square(Rectangle):
    """Classe pour représenter un carré et effectuer
    des opérations sur celui-ci."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialise un objet Square.

        Args:
            size (int): Longueur du côté du carré.
            x (int): Coordonnée X du coin supérieur gauche.
            y (int): Coordonnée Y du coin supérieur gauche.
            id (int): Identifiant de l'objet (facultatif).
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Renvoie la longueur du côté du carré
        (équivalent à la largeur du rectangle)."""
        return self.width

    @size.setter
    def size(self, value):
        """
        Définit la longueur du côté du carré
        (équivalent à la largeur et la hauteur du rectangle).

        Args:
            value (int): Nouvelle longueur du côté.
        """
        self.width = value
        self.height = value

    def __str__(self):
        """Renvoie une représentation en string de caractères du carré."""
        return "[Square] \
        ({}) {}/{} - {}".format(self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """
        Affecte les arguments aux attributs, prend en charge
        à la fois les arguments et les paires clé-valeur.

        Args:
            *args: Arguments pour mettre à jour les attributs
            (dans l'ordre : id, size, x, y).
            **kwargs: Paires clé-valeur pour mettre à jour les attributs.
        """
        if args:
            attrs = ["id", "size", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
            self.width = self.size
            self.height = self.size
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)
                if key == "size":
                    self.width = value
                    self.height = value

    def to_dictionary(self):
        """
        Renvoie un dictionnaire représentant l'objet Square.

        Returns:
            dict: Dictionnaire avec les attributs de l'objet.
        """
        return {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
