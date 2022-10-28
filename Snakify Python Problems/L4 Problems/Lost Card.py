n = int(input())
full_total = 0
input_total = 0
for i in range(1, n+1):
    full_total += i
for i in range(1, n):
    num = int(input())
    input_total += num

lost_card = full_total - input_total
print(lost_card)
    

    

    
