def computepay(hr,rt):
    if hr <= 40 :
    	rpay = hr * rt
        return rpay
    elif hr > 40 :
        reg = rt * hr
        otp = (hr - 40) * (rt *0.5)
        pay = reg + otp
        return pay

h = input("Enter Hours:")
hr = float(h)
r = input ("enter pay rate")
rt = float(r)
p = computepay(hr, rt)
print("Pay",p)
