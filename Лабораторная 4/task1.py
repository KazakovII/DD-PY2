class Animal:
    """
    Класс Animal - абстрактное животное

    Attributes:
        name    - кличка животного
        gender  - пол животного
        age     - возраст животного
    """

    name: str
    gender: str
    age: int

    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def __str__(self):
        return f"Кличка {self.name}. Пол {self.gender}. Возраст {self.age}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, gender={self.gender!r}, age={self.age})"

    def walk(self) -> str:
        """
        заставляет животное двигаться
        :return: Животное двигается
        """
        pass

    def scream(self) -> str:
        """
        заставляет животное издавать звуки
        :return: Животное издает звуки
        """
        pass


class Dog(Animal):
    """
    Класс Dog - собака

    Attributes:
        name    - кличка собаки
        gender  - пол собаки
        age     - возраст собаки
    """


    def __init__(self, name, gender, age):
        super().__init__(name, gender, age)

    def __str__(self):
        super().__str__()

    def __repr__(self):
        super().__repr__()

    def scream(self) -> str:
        """
        перегружаем, потому что собака издает особый звук (лает)
        :return: Собака лает
        """
        pass


if __name__ == "__main__":
    dog = Dog("Jack", "male", 10)
    print(dog.age)
