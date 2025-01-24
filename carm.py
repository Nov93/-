class Car:
    def __init__(self, model, year, V, pr, dist):
        self.model=model
        self.year=year
        self.V=V
        self.pr=pr
        self.dist=dist
        self.количество_колес=4


    def descrition (self):
        return (f"модель-{self.model}, год выпуска-{self.year}, объем двигателя-{self.V}, цена-{self.pr}, пробег-{self.dist}, количество_колес-{self.количество_колес}")
модель=Car("Фольксваген","2018","1.4","2500000 руб.","175000")
print("Создан класс легковые автомобили")
print(модель.descrition())

class Track(Car):
    def __init__(self,model, year, V, pr, dist):
        super().__init__(model, year, V, pr, dist)
        self.количество_колес = 8


    def descrition(self):
        return (f"модель-{self.model}, год выпуска-{self.year}, объем двигателя-{self.V}, цена-{self.pr}, пробег-{self.dist}, количество_колес-{self.количество_колес}")

грузовая_модель = Car("Tatra", "2021", "8.0", "7500000 руб.", "90000")
print("Создан класс грузовые автомобили")
print(грузовая_модель.descrition())
