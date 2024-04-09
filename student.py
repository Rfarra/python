class Student:
    def __init__(self, first_name, last_name, address, age,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address= address
        self.age = age
        self.phone_number= phone_number

    def get_info(self):
        return f"{self.first_name} {self.last_name}, address: {self.address}, age: {self.age}, phone_number{self.phone_number}"

    def set_first_name(self, first_name):
        self.first_name = first_name

    def set_last_name(self, last_name):
        self.last_name = last_name

    def set_studentID(self, address):
        self.address = address

    def set_year(self, age):
        self.age = age

    def set_phone_number(self,phone_number):
        self.phone_number=phone_number

student1 = Student("John", "Doe", "1584 cool Ln", "19", "123-456-7890")
student2 = Student("Jane", "Smith", "1584 cool Ln", "19" ,"123-456-7890")

print(student1.get_info())
print(student2.get_info())
