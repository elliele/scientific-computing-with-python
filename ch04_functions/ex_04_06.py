"""
Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

Enter Hours: 45
Enter Rate: 10
Pay: 475.0
"""

def computepay(hours, rate):
    #print("In computepay", hours, rate)
    if hours > 40:
        #print("Overtime")
        reg = rate*hours
        otp = (hours-40.0)*(rate*0.5)
        #print(reg,otp)
        pay = reg +otp
    else:
        pay = hours * rate
    print("Returning", pay)
    return pay
    #print("Regular")

sh = input ("Enter Hours: ")
sr = input("Enter Rate: ")
fh = float(sh)
fr = float(sr)
#print(fh,fr)
xp = computepay (fh,fr)

print("Pay: ", xp)
