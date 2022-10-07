from models.models import Toyota

action = True

while action:

    print("-----------------------\n"
          "\tHello! User\n"
          "-----------------------\n"+
          "\t1.Add new car\n" +
          "\t2.Get all cars\n" +
          "\t3.Get car by id\n" +
          "\t0. Exit\n"+
          "-----------------------\n"
          )
    flag = int(input("Choose an action from the list: "))
    if flag ==1:
        model = input("Model name: ").title()
        type_of_car = input("Type of car: ").title()
        color = input("color: ").title()
        drive = input("drive: ").title()
        shift_gear = input('Shift gear: ').title()
        car = Toyota(model, type_of_car, color, drive, shift_gear)
        car.save()
    elif flag == 2:
        Toyota.get_all_cars()
    elif flag == 3:
        id = int(input("Type id:"))
        Toyota.get_by_id(id)
    elif flag == 0:
        action = False