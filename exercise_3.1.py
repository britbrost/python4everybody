hrs = input("Enter Hours:")
rate = input("enter rate")
fhrs = float(hrs)
frate = float(rate)
if fhrs > 40 :
    reg = frate * fhrs
    otp = (fhrs - 40) * (frate *0.5)
    pay = reg + otp
print (" total pay:", pay)
