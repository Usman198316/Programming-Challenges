s = str(input())
valid = True
while valid == True:
    if s.count("f") == 1:
        print(-1)
        valid = False
    elif s.count("f") == 0:
        print(-2)
        valid = False
    else:
        firstOcc = s.find("f") + 1
        print(s.find("f", firstOcc))
        valid = False
              
        

