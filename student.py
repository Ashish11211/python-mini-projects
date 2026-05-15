---Student Result System
name = input("Enter student name: ")

math = int(input("Enter Math marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

total = math + science + english
percentage = total / 3

print("\n----- RESULT -----")

print(f"Student Name : {name}")
print(f"Total Marks  : {total}")
print(f"Percentage   : {percentage}%")

if percentage >= 90:
    print("Grade : A+")

elif percentage >= 75:
    print("Grade : A")

elif percentage >= 60:
    print("Grade : B")

else:
    print("Grade : C")
  ------output:----------
Enter student name: Akash
Enter Math marks: 90
Enter Science marks: 85
Enter English marks: 80

----- RESULT -----

Student Name : Akash
Total Marks  : 255
Percentage   : 85.0%
Grade : A
