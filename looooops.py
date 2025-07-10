
x = [None] * 5

for i in range(1,5):
    x[i-1] = input("Jesse Enter some element names : ") # Yeah i know how tou use input directly
    
with open("LetsCook.txt", "w") as f:
    for i in range(1,5):
        print(f"Element {i} is {x[i-1]}") 
        f.write(f"{x[i-1]} \n")
