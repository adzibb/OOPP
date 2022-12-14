class Company:
    def __init__(self, name, location):
        self.name = name
        self.location = location


class Manager(Company):
    def __init__(self, name, number_managers, company_name, company_location):
        super(Manager, self).__init__(company_name, company_location)
        self._name = name
        self._number_managers = number_managers

    def __str__(self):
        return ('********** Company **********\n' +
                '\nCompany Name: ' + self.name +
                '\nManager: ' + self._name +
                '\nNumber of Managers: ' + str(self._number_managers) +
                '\nLocation of Company: ' + self.location)


class Employee(Company):
    def __init__(self, name, age, gender, role, company_name, company_location):
        self._name = name
        self.age = age
        self.gender = gender
        self.role = role
        super(Employee, self).__init__(company_name, company_location)

    def __str__(self):
        return ('\n*+*+*+*+*+*+* Company *+*+*+*+*+*+*\n' +
                '\nEmployee: ' + self._name + '\nSex: ' + self.gender +
                '\nAge: ' + str(self.age) + '\nRole: ' + self.role +
                '\nWorking for: ' + self.name +
                '\nlocated in ' + self.location + '\n')


manager1 = Manager('Kojo', 1, 'D & J Company Limited', 'Accra-Ghana')
employee = Employee('Agbavor', 25, 'Male', 'Secretary', 'JB & SONS COMPANY LTD', 'Tamale')
print(employee)
