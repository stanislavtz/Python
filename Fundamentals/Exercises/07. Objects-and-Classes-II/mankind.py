from abc import ABC, abstractmethod

class Exceptions:
    def __init__(self):
        pass

    def uppercase_exception(self, argument):
        return f"Expected upper case letter! Argument: {argument}"

    def lenght_name_exception(self, num_symbols, argument):
        return f"Expected length at least {num_symbols} symbols! Argument: {argument}"

    def faculty_number_exception(self):
        return "Invalid faculty number!"

    def value_mishmash_exception(self, argument):
        return f"Expected value mismatch! Argument: {argument}"


class Human(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @first_name.setter
    def first_name(self, first_name):
        argument = 'firstName'

        if not first_name[0].isupper():
            raise Exception(excp.uppercase_exception(argument))
        if len(first_name) < 4:
            raise Exception(excp.lenght_name_exception(4, argument))
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        argument = 'lastName'

        if not last_name[0].isupper():
            raise Exception(excp.uppercase_exception(argument))
        
        if len(last_name) < 3:
            raise Exception(excp.lenght_name_exception(3, argument))
        
        self.__last_name = last_name

    @abstractmethod
    def __str__(self):
        return f"First Name: {self.first_name}\nLast Name: {self.last_name}"


class Student(Human):
    def __init__(self, first_name, last_name, faculty_number):
        super().__init__(first_name, last_name)
        self.faculty_number = faculty_number

    @property
    def faculty_number(self):
        return self.__faculty_number
    
    @faculty_number.setter
    def faculty_number(self, fcn):
        if not fcn.isalnum() or not len(fcn) in range(5, 11):
            raise Exception(excp.faculty_number_exception())
        self.__faculty_number = fcn

    def __str__(self):
        return f"{super().__str__()}\nFaculty number: {self.faculty_number}"


class Worker(Human):
    def __init__(self, first_name, last_name, salary, working_hours):
        super().__init__(first_name, last_name)
        self.salary = salary
        self.working_hours = working_hours
    
    @property
    def salary(self):
        return self.__salary
    
    @property
    def working_hours(self):
        return self.__working_hours

    @salary.setter
    def salary(self, salary):
        if salary <= 10:
            raise Exception(excp.value_mishmash_exception('weekSalary'))
        self.__salary = salary

    @working_hours.setter
    def working_hours(self, wh):
        if wh < 1 or wh > 12:
            raise Exception(excp.value_mishmash_exception('workHoursPerDay')) 
        self.__working_hours = wh

    def salary_per_hour(self):
        s = self.salary / (self.working_hours * 5)
        return s

 
    def __str__(self):
        return f"{super().__str__()}\nWeek Salary: {self.salary:.2f}\nHours per day: {self.working_hours:.2f}\nSalary per hour: {self.salary_per_hour():.2f}"


excp = Exceptions()

try:
    for _ in range(2):
        data = input().split()
        first_name, last_name = data[:2]
        if len(data) == 3:
            faculty_number = data[-1]
            student = Student(first_name, last_name, faculty_number)
        elif len(data) == 4:
            salary, working_hours = map(float, data[-2:])
            worker = Worker(first_name, last_name, salary, working_hours)

    print(student,'\n')
    print(worker)
except Exception as ex:
    print(ex)