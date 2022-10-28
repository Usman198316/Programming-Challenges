#Timestamps

hours1 = int(input("Enter the number of hours for the first timestamp:"))
minutes1 = int(input("Enter the number of minutes for the first timestamp:"))
seconds1 = int(input("Enter the number of seconds for the first timestamp:"))
hours2 = int(input("Enter the number of hours for the second timestamp:"))
minutes2 = int(input("Enter the number of minutes for the second timestamp:"))
seconds2 = int(input("Enter the number of seconds for the second timestamp:"))

convertSeconds1 = (hours1 *60*60) + (minutes1 *60) + seconds1
convertSeconds2 = (hours2 *60*60) + (minutes2 *60) + seconds2

secondsBetween = convertSeconds2 - convertSeconds1
print(secondsBetween)
