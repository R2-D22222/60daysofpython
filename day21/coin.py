def conversion(valor, taxcam, tipcon):
   
#    Dolar: 5.50
#    Euro: 6.37
#    libra 7.31 
   
   
   
    if tipcon == "dolar_real": 
             return round(valor * taxcam, 2)
    elif tipcon == "real_dolar":
            return round(valor / taxcam, 2)
    
    elif tipcon == "euro_real":
        return round(valor * taxcam, 2)
    elif tipcon == "real_euro":
        return round(valor / taxcam, 2)
    
    elif tipcon == "libra_real":
        return round(valor * taxcam, 2)
    elif tipcon == "real_libra":
        return round(valor / taxcam, 2)
    
    else:
            return ValueError("Tipo de conversão invalida")
  
print(conversion(12, 7.31, "real_libra"))
   