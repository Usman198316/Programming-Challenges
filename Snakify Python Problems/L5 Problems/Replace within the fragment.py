s = str(input())

if s[0] == "h" and s[-1] == "h":
    replace = s[0] + s[1:-1].replace(s[0], 'H') + s[-1]
    print(replace)
else:
    between_s = s[s.find("h")+1 : s.rfind("h")]
    replace = between_s.replace("h" , "H")
    print(s.replace(between_s , replace))
    





