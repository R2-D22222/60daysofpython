fibonacci = [0, 1]
for i in range(15):
    fibosum = fibonacci[-1] + fibonacci[-2]
    fibonacci.append(fibosum)
    print(fibonacci)