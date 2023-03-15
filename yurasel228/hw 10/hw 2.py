class Human:
    species = "Homosapiens"

    def __init__(self, name):
        """
        Конструктор класу Human.

        :param name: Ім'я людини.
        """
        self.name = name

    def greet(self):
        """
        Виводить привітання з іменем людини.
        """
        print(f"Hello, my name is {self.name}.")

    @classmethod
    def species_info(cls):
        """
        Повертає інформацію про вид людини.

        :return: Рядок з інформацією про вид людини.
        """
        return f"This is a {cls.species}."

    @staticmethod
    def random_message():
        """
        Повертає довільне повідомлення.

        :return: Довільне повідомлення.
        """
        return "This is a random message."

    def __str__(self):
        """
        Повертає рядок з інформацією про об'єкт.

        :return: Рядок з інформацією про об'єкт.
        """
        return f"Ім'я людини: {self.name}, Вид: {self.species}"


# Приклад використання:
person1 = Human("Alice")