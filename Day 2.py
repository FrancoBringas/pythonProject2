print("Welcome to the trip calculator")
bill = int(input("What was the total bill?"))
tip_percentage = int(input("What percentage tip would you like to give? 10,12, or 15?"))
people = int(input("How many people to split the bill?"))
total = bill*tip_percentage*0.01
total_people = float((total + bill)/people)
print("Each person should pay:",round(total_people,2))


