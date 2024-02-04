"""
Weather Report
In this exercise you will create a weather reporting function that takes another function as its argument.

Here are some instructions:

Declare a function called report_weather that takes a temperature and a function as its two arguments
Declare two other functions, each of which takes a temperature as an argument
One is called as_sun_lover and it returns 'great' if the temp is 25 Celsius, or above. Otherwise it returns 'not great'
One is called as_snow_lover and it returns 'great' if the temp is 0, or below. Otherwise it returns 'not great'
Combine the functions to generate customised weather reports
Expected Behaviour
>>>  report_weather(24, as_sun_lover)
'not great'
>>>  report_weather(25, as_sun_lover)
'great'
>>>  report_weather(1, as_snow_lover)
'not great'
>>>  report_weather(0, as_snow_lover)
'great'
"""

def report_weather(temp, lover_func):
    return lover_func(temp)

def as_sun_lover(temp):
    return 'not great' if temp < 25 else 'great'

def as_snow_lover(temp):
    return 'great' if temp <= 0 else 'not great'

print(report_weather(24, as_sun_lover))
print(report_weather(25, as_sun_lover))
print(report_weather(1, as_snow_lover))
print(report_weather(0, as_snow_lover))