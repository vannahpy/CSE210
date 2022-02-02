class Student:
    def __init__(self, fname,lname):
        self.__first_name = fname
        self.__last_name = lname
    
    def __first_name(self):
        return self.__first_name
    def __last_name(self):
        pass
    def show_name(self):
        return f"{self.__last_name}, {self.__first_name}"
    
person = Student("Vannah", "Pyatt")
person.show_name