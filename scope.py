# BMI Calculator


POUNDS_TO_KG = 0.453592
INCHES_TO_METERS = 0.0254

# Function to calculate BMI based on height and weight
def calculate_BMI(weight,height):


    bmi = weight(kg) / (height(m) * height(m))
    return bmi #returns to calculated bmi value


# Function to determain BMI category
def BMI_category (bmi):
 if bmi < 18.5:
        return "Underweight"
 elif 18.5 <= bmi < 25:
        return "Normal weight"
 elif 25 <= bmi < 30:
        return "Overweight"
 else:
        return "Obese"


weight= float(input("enter wieght in pounds: "))
height= float (input("enter height in inches:"))


bmi = calculate_BMI(weight, height)
print(f"Your BMI is: {bmi:.2f}")
print("you are (category)")
