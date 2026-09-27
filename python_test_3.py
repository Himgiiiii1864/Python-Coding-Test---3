grades = {"Anne": 97, "Julian": 92, "Dick": 84, "Timmy": 73, "George": 6}

total = 0

for score in grades.values():
    total += score

average = total / len(grades)
print("Average:", average)

highestscore = max(grades.values())
lowestscore = min(grades.values())

highest = [name for name, score in grades.items() if score == highestscore]
lowest = [name for name, score in grades.items() if score == lowestscore]

print("Top scorer:", highest[0], "-", highestscore)
print("Bottom scorer:", lowest[0], "-", lowestscore)


name = input("Enter the student's name whose grade you need: ")
scores =  grades.get(name)
if name in grades:
  print(f"{name} scored: {scores}")
else: 
  print("Unfortunately, the name is not registered. Kindly enter a valid name.")