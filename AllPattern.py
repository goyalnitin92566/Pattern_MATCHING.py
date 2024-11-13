# Pattern Printing 

# Ques - 1 ( Basic Square Printing)

row = 7

for i in range(row): # The outer loop controls the number of rows
  for j in range(row): # The inner loop controls the number of asterisks being printed
    print("*",end="")
  print() # This print is use for print the line to next statement


# Q2) Triangle Pattern Printing

row = 7
for i in range(1,row+1): # or we can also do this for i in range(row)
  for j in range(i):
    print("*",end = "")
  print()

 #Q3) Inverted Triangle Pattern

row = 7
for i in range(row,0,-1): # In the loop for i in range(row, 0, -1), the -1 is the step value. It specifies that the loop should decrement i by 1 after each iteration, which allows us to go from a higher number down to a lower number.
  for j in range(i):
    print("*",end = "")
  print()

