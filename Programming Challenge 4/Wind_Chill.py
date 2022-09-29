def WCTCalc(air_temp, air_speed):
    WCTindex = 35.74 + 0.6215 * air_temp - 35.75 * air_speed**0.16 + 0.4275 * air_temp * air_speed**0.16
    return WCTindex

print(f"Temperature of 10 and speed of 15 gives windchill of: {WCTCalc(10, 15)}")
print(f"Temperature of 0 and speed of 25 gives windchill of: {WCTCalc(0, 25)}")
print(f"Temperature of -10 and speed of 35 gives windchill of: {WCTCalc(-10, 35)}")

tempInput = float(input("Enter Temperature >> "))
speedInput = float(input("Enter Speed >> "))
print(f"Windchill >> {WCTCalc(tempInput, speedInput)}")

if __name__ == "__main__":
    WCTcalc(10, 15)
