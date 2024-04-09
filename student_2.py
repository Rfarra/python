# Class definition
class Student:
    # Class variable
    Vet = "Dog Clinic"

    def __init__(self, first_name, pet_id, pet_name, pet_type="Dog"):
        # Instance variables
        self.__first_name = first_name
        pet_id = pet_id
        pet_name = pet_name
        pet_type = pet_type

    # Getter and Setter for first_name
    def get_first_name(self):
        return self.__first_name

    def get_pet_id(self):
        return self.pet_id

    def get_student_id(self):
        return self.__pet_name

    def get_grade_level(self):
        return self.__grade_level

    def set_first_name(self, value):
        self.pet_type



    # Method to print student details
    def print_student_details(self):
        print("Student Details:", vars(self))

    # Method to print basic info about the student
    def print_info(self):
        print(self.__first_name + " " + self.__last_name)
        print(self.__student_id)
        print(self.__grade_level)


# Main function to demonstrate usage of the Student class
def main():
    # Creating an instance of Student
    Vet = Dog clinic("John", "Bald", "009234", "adam","dog")
 


# Calling the main function
main()
