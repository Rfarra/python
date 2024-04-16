class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def get_name(self):
        return self.name

   

    def get_number(self):
        return self.number




class ProductionWorker(Employee):
    def __init__(self, name, number, shift_number, hourly_pay_rate):
        super().__init__(name, number)
        self.shift_number = shift_number
        self.hourly_pay_rate = hourly_pay_rate

    def get_shift_number(self):
        return self.shift_number

   

    def get_hourly_pay_rate(self):
        return self.hourly_pay_rate

  


def main():
   
  
    print("Employee Details:")
    print("Name:", worker.get_name())
    print("Hourly Pay Rate:", worker.get_hourly_pay_rate())
    


main()
