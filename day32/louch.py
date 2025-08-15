from random import randint

def lançar_dados():
    return randint(1, 10)

if __name__ == "__main__":
    print(f"Os dados são: {lançar_dados()}")