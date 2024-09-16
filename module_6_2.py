class Vehicle:
    __COLOR_VARIANTS = ['blue', 'black', 'orange', 'grey', 'white']

    def __init__(self, owner, __model, __engine_power, __color):
        self.owner: str = owner  # владелец транспорта. (владелец может меняться)
        self.__model: str = __model  # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power: int = __engine_power  # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color: str = __color  # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        return f'Модель: {self.__model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self.__engine_power}'

    def get_color(self):
        return f'Цвет: {self.__color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self.new_color = new_color
        if self.__color.lower() in self.__COLOR_VARIANTS:
            self.__color = self.new_color
        else:
            print(f'Нельзя сменить цвет на {self.new_color}')
            return self


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
