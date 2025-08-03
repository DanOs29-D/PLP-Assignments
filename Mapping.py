#Write a function that receives a temperature in Celsius and returns a description based on this mapping:
#- range(-100, 0) ➝ "Freezing"
#- range(0, 15) ➝ "Cold"
#- range(15, 25) ➝ "Cool"
#- range(25, 35) ➝ "Warm"
#- range(35, 101) ➝ "Hot"
#If the input is outside the range –100 to 100, return "Invalid temperature".
acceptable = int(input("Enter temperature in Celsius: "))
def thermo(acceptable):
    temp_range = {
        range(-100, 0): "Freezing",
        range(0, 15): "Cold",
        range(15, 25): "Cool",
        range(25, 35): "Warm",
        range(35, 101): "Hot"
    }
    for comment in temp_range:
        if acceptable in comment:
            return temp_range[comment]
    return "Invalid temperature"

print(thermo(acceptable))

