#!/usr/bin/python3
import json
import os

class Base:
    """La classe de base pour gérer des objets et les sauvegarder en JSON."""

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialise un nouvel objet.

        Args:
            id (int): L'identifiant de l'objet, S'il n'est pas spécifier, un identifiant unique est attribue.
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converti une liste de dictionaries en une string JSON.

        Args:
            list_dictionaries (list): List de dictionaries à convertir.

        Returns:
            str: string JSON représentant la liste de dictionaries
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Sauvegarde une list d'objets dans un fichier JSON.

        Args:
            cls (class): La classe à laquelle les objets appartiennent.
            list_objs (list): Liste d'objets à sauvegarder.

        Example:
            Base.save_to_file([obj1, obj2, obj3])
        """
        if list_objs is None:
            list_objs = []

        class_name = cls.__name__
        filename = f"{class_name}.json"
        list_dictionaries = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dictionaries)

        with open(filename, "w") as file:
            file.write(json_string)

    @classmethod
    def from_json_string(cls, json_string):
        """
        Convertit une string JSON en une liste de dictionnaires.

        Args:
            cls (class): La classe à laquelle les objets appartiennent.
            json_string (str): string JSON à convertir.

        Returns:
            list: Liste de dictionnaires.

        Example:
            data = Base.from_json_string(json_data)
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Crée un nouvel objet à partir d'un dictionnaire de valeurs initiales.

        Args:
            cls (class): La classe à partir de laquelle créer l'objet.
            **dictionary (dict): Dictionnaire de valeurs initiales.

        Returns:
            object: Nouvel objet créé avec les valeurs spécifiées.

        Example:
            obj = Base.create(id=1, width=10, height=20)
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls(0)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Charge des objets à partir d'un fichier JSON et les crée en utilisant la méthode `create`.

        Args:
            cls (class): La classe à partir de laquelle créer les objets.

        Returns:
            list: Liste d'objets créés.

        Example:
            objects = Base.load_from_file()
        """
        filename = f"{cls.__name__}.json"

        if os.path.exists(filename) is False:
            return []

        with open(filename, 'r') as f:
            list_str = f.read()

        list_cls = cls.from_json_string(list_str)
        list_ins = []

        for index in range(len(list_cls)):
            list_ins.append(cls.create(**list_cls[index]))

        return list_ins

    def to_dictionary(self):
        """
        Convertit l'objet en un dictionnaire représentant ses attributs.

        Returns:
            dict: Dictionnaire des attributs de l'objet.

        Example:
            obj_dict = obj.to_dictionary()
        """
        return self.__dict__

    def update(self, *args, **kwargs):
        """
        Met à jour les attributs de l'objet en fonction des arguments ou des paires clé-valeur spécifiés.

        Args:
            *args: Arguments pour mettre à jour les attributs (dans l'ordre : id, width, height, x, y).
            **kwargs: Paires clé-valeur pour mettre à jour les attributs.

        Example:
            obj.update(id=2, width=30, x=5)
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i in range(len(args)):
                if i < len(attrs):
                    setattr(self, attrs[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
