print("Please enter weight in pounds")
pounds=int(input())
print("Please enter height in inches")
inches=int(input())
weight=pounds*0.453592
height=inches*0.0254
bmi=weight/height**2
print("BMI is :", bmi)

