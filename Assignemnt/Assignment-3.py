# python has int,float,str function for typecasting not double and char

# Question : smart temperature convertere
# Question : smart bill calculator
0

print("smart temperature converter")
print("enter temperature in to convert in another form")
print("time to conver celcius to fahrenheit")

celcius = input("enter temperature in celsius")
c = float(celcius)
# celcius convert to fahrenheit
fahrenheit = (c *(9/5)) +32
print("temperature convern in fahrenheit :",round(fahrenheit,2))


# converter conver celcius to kelvin
kelvin = c + 273.15
print("Celsius converted in Kelvin:", kelvin)


