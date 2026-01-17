def bmi_calculation(weight, height):

    bmi_value = round(weight/(height**2),2)
    
    if bmi_value < 18.5:
        print(f"You fall in 'Under-Weight' with bmi value '{bmi_value}'")
    elif bmi_value > 18.5 and bmi_value < 24.9:
        print(f"You fall in 'Normal-Weight' with bmi value '{bmi_value}'")
    elif bmi_value > 25 and bmi_value < 29.9:
        print(f"You fall in 'Over-Weight' with bmi value '{bmi_value}'")
    elif bmi_value > 30 and bmi_value < 34.9:
        print(f"You fall in 'Obesity-(class_1)' with bmi value '{bmi_value}'")
    elif bmi_value > 35 and bmi_value < 39.9:
        print(f"You fall in 'Obesity-(class_2)' with bmi value '{bmi_value}'")
    else:
        print(f"You fall in 'Obesity-(class_3)' with bmi value '{bmi_value}'")


while True:
    print("-------BMI Calculator--------")
    user = input("YOu want to check your body-mass (yes/no): ").strip().lower()
    if user == "yes":

        user_weight = float(input("Enter Your Weight (kg) : "))
        user_height = float(input("Enter Your Height (cm) : "))/100

        bmi_calculation(user_weight, user_height)
    elif user == "no":
        break
    else:
        print("Enter Valid Option!")

