#(a) Use a for loop with range(0, 101, 20) to print the conversion table below. 

def celsius_to_fahrenheit(c,round_to=1):
    return round(c*9/5+32,round_to)

def fahrenheit_to_celsius(f,round_to=1):
    return round((f-32)*5/9,round_to)

print("\n  °C  |   °F")
print("------+-------")

for c in range(0,101,20):
    print(f"{c:5} | {fahrenheit_to_celsius(c):5}")

#(b) Convert 98.6 °F (normal body temperature) to Celsius.
print("\n\n")
print("98.6 °F =",fahrenheit_to_celsius(98.6),"°C")
#(c) Convert 37 °C to Fahrenheit and back again. Do you get 37.0? 
print("Round trip 37 °C:", fahrenheit_to_celsius(celsius_to_fahrenheit(37)))
