# Task 2 - Rewriting code using a while loop instead of a for loop.

a = [7,12,9,14,15,18,12] 
b = [9,14,8,3,15,17,15] 
big = [ ] 

counter = 0

while counter != len(a):
    big.append(max(a[counter],b[counter])) 
    counter = counter + 1

print(big)