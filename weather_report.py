def get_weather_report(temperature):
    # Complete this function
    if temperature<22:
        return "Cold"
    elif temperature>=22 and temperature<35:
        return "Warm"
    else:
        return "Hot"

temperature = int(input())
# Call the get_weather_report function
print(get_weather_report(temperature))

"""
input:18
output:Cold
"""
