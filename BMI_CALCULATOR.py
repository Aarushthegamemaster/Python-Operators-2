a = float(input("Please enter your weight here"))
b = float(input("PLease enter your height here"))

BMI = a / (b/100)**2

print("Your BMI is", BMI)

if BMI<=18.4:
    print("You are underweight")
elif BMI<=24.9:
    print("You are healthy")
elif BMI<=29.9:
    print("you are overweight")
elif BMI<=34.9:
    print("You are severely overweight")
elif BMI<=39.9:
    print("You are obese")
else:
    print("You are severly obese")
