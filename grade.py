score = float(input("what score?   "))
if score >= 0 and score <= 30:
    grade = "D"
elif score >= 30 and score <= 50:
    grade = "C"
elif score >= 50 and score <= 70:
    grade = "B"
elif score >= 70 and score <= 100:
    grade = "A"
else:
    grade ="invalid"   
print(grade)