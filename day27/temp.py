def celsius_to_fahrenheit(celsius):
    return(celsius * 9/5) + 32
def fahrenheit_to_celsius(fahrenheit):
    return(fahrenheit -32) * 5/9
def main(temperatura, t_conversion):
    if t_conversion == "celsius":
        print(celsius_to_fahrenheit(temperatura))
    elif t_conversion == "fahrenheit":
        print(fahrenheit_to_celsius(temperatura))
    else:
       return print("tipagem de temperatura invalida")
        
        
if __name__ == "__main__":
    main(20, "celsius")
    main(20, "fahrenheit")