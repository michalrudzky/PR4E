def computepay(h, r):
    if h > 40:
        p = 40 * r + (r * 1.5) * (h - 40)
    else:
        p = h * r
    return p
    
try:
    x = raw_input("Enter Hours: ")
    hours = float(x)
    y = raw_input("Enter Rate: ")
    rate = float(y)
except:
    print "Error, please enter numeric input"

print computepay(hours, rate)
