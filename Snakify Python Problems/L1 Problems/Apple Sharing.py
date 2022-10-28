#Apple Sharing

N = int(input("How many students are there?"))
K = int(input("How many apples are there in the basket?"))
ApplesPerStudent = K / N
print("Each student will get", int(ApplesPerStudent), "apples!")
ApplesRemaining = K % N
print("There will be", ApplesRemaining, "Apples left in the basket.")
