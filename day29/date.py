from datetime import datetime

def exibir_data_hora():
    
    fuso_horario = pytz.timezone("America_do_sul/Cuiabá")
    data_hora = datetime.now(fuso_horario)
    formato_data = data_hora.strftime("%d/%m/%Y %H:%M:%S")
    print(f"data e hora atual: {formato_data} ")
    
if __name__ == "__main__":
    exibir_data_hora()