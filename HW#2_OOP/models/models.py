import json


class Toyota:
    file = "cars.json"

    def __init__(self, model, type_of_car, color, drive, shift_gear):
        self.model = model
        self.type_of_car = type_of_car
        self.color = color
        self.drive = drive
        self.shift_gear = shift_gear

    @classmethod
    def get_data(cls):
        file = open("database/" + cls.file)
        data_in_json = file.read()
        data = json.loads(data_in_json)
        file.close()
        return data

    @classmethod
    def get_all_cars(cls):
        data = cls.get_data()
        for car in data:
            print('\n')
            print("\tCar id: " + str(car["id"]))
            print("\tToyota model: " + car["model"])
            print("\tType of car: " + car["type of car"])
            print("\tColor: " + car["car color"])
            print("\tType of drive: " + car["drive"])
            print("\tShift gear: " + car["shift gear"])
            print("------------------------")

    @classmethod
    def get_by_id(cls, id):
        cars = cls.get_data()
        counter = 0
        for car in cars:
            if id == car["id"]:
                print('\n')
                print("\tCar id: " + str(car["id"]))
                print("\tToyota model: " + car["model"])
                print("\tType of car: " + car["type of car"])
                print("\tColor: " + car["car color"])
                print("\tType of drive: " + car["drive"])
                print("\tShift gear: " + car["shift gear"])
                print("------------------------")
            counter += 1
            if counter == len(cars):
                print("Not found car with this id")

    def save(self):
        data = self.get_data()
        new_car = {"model": self.model, "type of car": self.type_of_car, "car color": self.color,
                   "drive": self.drive, "shift gear": self.shift_gear}
        if len(data) > 0:
            new_car["id"] = data[-1]["id"] + 1
        else:
            new_car["id"] = 1
        data.append(new_car)
        file = open("database/" + self.file, "w")
        data_in_json = json.dumps(data)
        file.write(data_in_json)
        return