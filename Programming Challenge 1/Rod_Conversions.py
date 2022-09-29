import sys, time

def converter(num):
  print(f"You would like to use a distance of {num} in rods.")
  numMetres = num * 5.0292
  numFeet = num * 16.5
  numMiles = num / 320
  numFurlongs = num / 40
  timeWalk = (num / 992) * 60

  time.sleep(1)
  print(f" >{numMetres} in metres \n >{numFeet} in Feet \n >{numMiles} in miles \n >{numFurlongs} in Furlongs \n \n It will take {timeWalk} minutes to walk this distance")



  
def menu():
  opt = input("=================\n 1. Start Converter \n 2. Quit \n ==================")
  return opt

option = menu()
if option == "2":
  print("Thanks for using!")
  time.sleep(1)
  sys.exit()


if option == "1":
  rodDist = float(input("Enter your distance in rods: "))
  converter(rodDist)

if __name__ == '__main__':
  converter(10)
