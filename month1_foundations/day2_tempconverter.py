temperature = input ("Which method do you use to calculate temperature? Celsius or Fahrenheit?" )
if temperature == "Celsius":
    value1 = float(input("What is the temperature in celsius right now?"))
    print("Okay, so ", value1, " degrees celsius is ",((value1 * 1.8) + 32)," fahrenheit")
elif temperature == "Fahrenheit":
    value2 = float(input("What is the temperature in fahrenheit right now?"))
    print("Okay, so ", value2, " degrees fahrenheit is ",((value2 - 32) / 1.8), " celsius")
else:
    input ("Which method do you use to calculate temperature? Celsius or Fahrenheit?" )
