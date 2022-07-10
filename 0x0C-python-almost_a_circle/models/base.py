#!/usr/bin/python3
import json
import csv


class Base:
    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        filename = "{}.json".format(cls.__name__)
        list1 = []

        if list_objs is None:
            with open(filename, "w") as f:
                f.write("[]")
        for i in list_objs:
            dic = i.to_dictionary()
            list1.append(dic)
        js = json.loads(cls.to_json_string(list1))
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(js, f)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        from rectangle import Rectangle
        from square import Square
        if cls.__name__ == 'Rectangle':
            m = Rectangle(2, 3)
        if cls.__name__ == 'Square':
            m = Square(4)
        m.update(**dictionary)
        return m

    @classmethod
    def load_from_file(cls):
        filename = "{}.json".format(cls.__name__)
        list1 = []
        try:
            with open(filename, "r", encoding="utf-8") as f:
                list2 = cls.from_json_string(f.read())
        except:
            return list
        for i in list2:
            list1.append(cls.create(**i))
        return list1

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = "{}.csv".format(cls.__name__)

        if list_objs is None:
            with open(filename, "w") as f:
                f.write("[]")
        with open(filename, "w") as f:
            writer = csv.writer(f)
            for i in list_objs:
                if cls.__name__ == 'Rectangle':
                    writer.writerow([i.id, i.width, i.height, i.x, i.y])
                if cls.__name__ == 'Square':
                    writer.writerow([i.id, i.size, i.x, i.y])

    @classmethod
    def load_from_file_csv(cls):
        filename = "{}.csv".format(cls.__name__)
        with open(filename, "r") as f:
            if cls.__name__ == 'Rectangle':
                red = csv.DictReader(f, fieldnames=['id', 'width', 'height', 'x', 'y'])

            elif cls.__name__ == 'Square':
                red = csv.DictReader(f, fieldnames=['id', 'size', 'x', 'y'])

            list1 = []
            for instance in red:
                list2 = {x: int(y) for x, y in instance.items()}
                temp = cls.create(**list2)
                list1.append(temp)
        return list1
