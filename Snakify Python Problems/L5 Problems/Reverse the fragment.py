s = str(input())
first_occ = s.find("h")
last_occ = s.rfind("h")
fragment = s[first_occ : last_occ + 1]
reversed_fragment = fragment[ : : -1]
new_string = s.replace(fragment , reversed_fragment)
print(new_string)
