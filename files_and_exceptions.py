def read_file_to_dict(filename):
    new_dict = {}
    try: 
        with open('filename','r') as file:
            line = file.readline() # lee linea del archivo
            lista_de_entradas = line.split(';') 
            for entrada in lista_de_entradas: # recorre cada entrada de producto: valor
                if entrada == "":
                    pass

                producto, valor = entrada.split(':') 
                valor = float(valor)

                if producto not in new_dict:
                    new_dict[producto] = []
                 
                 
                new_dict[producto].append(valor)
        return new_dict
    except FileNotFoundError: 
        raise FileNotFoundError(f"El archivo '{filename}' no existe")


def process_dict(data):
    for producto, valores in data.items():
        total = sum(valores)
        promedio = total/len(valores)

        print(f"{producto}: ventas totales ${total:.2f}, promedio ${promedio:.2f}")
