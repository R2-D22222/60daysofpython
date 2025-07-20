fruits = []

while True:
    fruit = input("The name of the fruit: ")
    if fruit == "exit":
        break
    
    fruits.append(fruit)
    print(fruits)