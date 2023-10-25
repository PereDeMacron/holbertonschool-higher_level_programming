#!/usr/bin/python3
from models.base import Base


class Rectangle(Base):
    """Classe pour représenter un rectangle et
    effectuer des opérations sur celui-ci."""

    current_id = 0  # Initialise une variable de classe pour suivre l'ID actuel

    @classmethod
    def increment_id(cls):
        """
        Incrémente l'ID actuel et renvoie la nouvelle valeur.

        Returns:
            int: Nouvelle valeur de l'ID actuel.
        """
        cls.current_id += 1
        return cls.current_id

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initialise un objet Rectangle.

        Args:
            width (int): Largeur du rectangle.
            height (int): Hauteur du rectangle.
            x (int): Coordonnée X du coin supérieur gauche.
            y (int): Coordonnée Y du coin supérieur gauche.
            id (int): Identifiant de l'objet (facultatif).

        Note:
            Si l'ID n'est pas spécifié, il est incrémenté automatiquement.
        """
        super().__init__(id)
        if id is None:
            self.id = self.__class__.increment_id()
        else:
            self.id = id
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Renvoie la largeur du rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """
        Définit la largeur du rectangle.

        Args:
            value (int): Nouvelle largeur.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure ou égale à zéro.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Renvoie la hauteur du rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Définit la hauteur du rectangle.

        Args:
            value (int): Nouvelle hauteur.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure ou égale à zéro.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Renvoie la coordonnée X du coin supérieur gauche du rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        """
        Définit la coordonnée X du coin supérieur gauche du rectangle.

        Args:
            value (int): Nouvelle coordonnée X.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure à zéro.
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Renvoie la coordonnée Y du coin supérieur gauche du rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        """
        Définit la coordonnée Y du coin supérieur gauche du rectangle.

        Args:
            value (int): Nouvelle coordonnée Y.

        Raises:
            TypeError: Si la valeur n'est pas un entier.
            ValueError: Si la valeur est inférieure à zéro.
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Renvoie l'aire du rectangle."""
        return self.__width * self.__height

    def display(self):
        """
        Affiche le rectangle en utilisant des caractères
        '#' avec des décalages en x et y.

        Note:
            Affiche d'abord des lignes vides pour le décalage en y,
            puis des caractères '#' pour le rectangle.
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """Renvoie une représentation en string de caractère du rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        Affecte les arguments aux attributs,
        prend en charge à la fois les arguments et les paires clé-valeur.

        Args:
            *args: Arguments pour mettre à jour les attributs
            (dans l'ordre : id, width, height, x, y).
            **kwargs: Paires clé-valeur pour mettre à jour les attributs.
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                setattr(self, attrs[i], args[i])
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "width" in kwargs:
                self.width = kwargs["width"]
            if "height" in kwargs:
                self.height = kwargs["height"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        Renvoie un dictionnaire représentant l'objet Rectangle.

        Returns:
            dict: Dictionnaire avec les attributs de l'objet.
        """
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
