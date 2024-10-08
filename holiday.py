time = float(input("when you leave?   "))
till_home = float(input("how long leave for in days?   "))
left_over = (till_home % 6)-1
time_of_home = time + left_over
if time_of_home > 6:
    time_of_home = time_of_home - 73
print("time of home:")
print(time_of_home)