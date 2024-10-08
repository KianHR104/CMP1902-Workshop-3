time = float(input("whats the time in hours?   "))
till_alarm = float(input("when the alarm in hours?   "))
left_over = till_alarm % 24 
time_of_alarm = time + left_over
if time_of_alarm > 24:
    time_of_alarm = time_of_alarm - 24
print("time of alarm:")
print(time_of_alarm)