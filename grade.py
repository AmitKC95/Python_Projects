score = int (input("Score: "))

if score >= 90 and score <= 100:
    print("Grade: A")

elif 80 <= score < 90:
    print("Grade: B")

elif score >= 70:
    print ("Grade: C")

elif score >= 60:
    print("Grade: D")

else:
    print("Grade: F")