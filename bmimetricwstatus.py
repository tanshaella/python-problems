print("Please enter weight in kilograms")
weight=int(input())
print("Please enter height in meters")
height=float(input())
bmi=weight/height**2

if (bmi < 18.5):
    print("BMI is", ":", bmi,",", "Status is Underweight")
elif (18.5 < bmi < 24.9):
    print("BMI is", ":", bmi,",", "Status is Normal")
elif (25.5 < bmi < 29.9):
    print("BMI is", ":", bmi,".", "Status is Overweight")
elif (bmi > 30.0):
    print("BMI is", ":", bmi,",", "Status is Obese")
