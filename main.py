from models.plant import Plant
from models.employee import Employee
from models.salon import Salonuser

if __name__ == '__main__':
    while True:
        print(
            "Choose a menu item by number: \n" +
              "1. Add new Plant \n" +
              "2. Add new Employee \n" +
              "3. Get plant by id \n" +
              "4. Get employee by id \n"
              "5. Add new Salon \n"
              "6. Get Salon by id"
              )
        menu_flag = int(input("Your choose: "))
        if menu_flag == 1:
            id = int(input("ID: "))
            location = input("Location: ")
            name = input("Name: ")
            director_id = int(input("Director ID: "))
            plant = Plant(id, location, name, director_id)
            plant.save()
        elif menu_flag == 2:
            id = int(input("ID: "))
            name = input("Name: ")
            email = input("Email: ")
            department_type = input("Department Type: ")
            department_id = int(input("Department id: "))
            employee = Employee(id, name, email, department_type, department_id)
            employee.save()
        elif menu_flag == 3:
            id = int(input("ID: "))
            plant = Plant.get_by_id(id)
            print(plant)
        elif menu_flag == 4:
            id = int(input("ID: "))
            employee = Employee.get_by_id(id)
            print(employee)
        elif menu_flag == 5:
            id = int(input('Id:'))
            name_salon = input('Choose letters!\n'
                               'Name Salon:')
            adress_salon = input('Adress Salon:')
            salon = Salonuser(id,name_salon,adress_salon)
            salon.save()
        elif menu_flag == 6:
            id = int(input('ID: '))
            salon = Salonuser.get_by_id(id)
            print(salon)