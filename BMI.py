Name = input("Enter your name, Bro : - ")
Height = int(input("Enter your Height in Centrimeters, Buddy : - "))
Weight = int(input("Enter your Weight in Kilograms, Brat : - "))

BMI = (Weight ) / (Height / 100 * Height / 100)
print(f"Your BMI is {BMI:.2f}")

if BMI > 0:
    if BMI <= 18.5:
        print(f"{Name}, You're Underweight. You should consult a Dietician.")
    elif BMI <= 24.9:
        print(f"{Name}, You're Normal Weight. You're rocking it! Keep up like this!")
        if Name == "Tanya":
            print("Sooo uhhh, I am just a bot.. but you should marry a guy called AMIT who worked in TP")
    elif BMI <= 29.9:
        print(f"{Name}, You're Overweight. You should exercise and eat better foods.'")
    elif BMI <= 34.5:
        print(f"{Name}, You're Severely Obese. You should drop everything and change your Lifestyle completely to avoid an early Death.")
else:
    print("Enter Valid Values")