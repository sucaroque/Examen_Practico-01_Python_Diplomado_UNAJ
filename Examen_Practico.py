import pandas as pd

def promedio_notas(notas):
    notas = pd.Series(notas)
    return notas.mean()

# Diccionario con notas
notas = {'Nota 1': 9, 'Nota 2': 6.5, 'Nota 3': 4, 'Nota 4': 8.5, 'Nota 5': 5}

print("\033[1mREGISTRO DE NOTAS\033[0m")
# Recorremos el diccionario para imprimir cada nota
for nombre, nota in notas.items():
    print(f'{nombre}: {nota}')
    
print("\nEl promedio de las notas es:", promedio_notas(notas))
print("=" * 50)
print("\033[1mDeveloped with love by RUBEN ROQUE SUCARI\033[0m \u2764\uFE0F")
print("=" * 50)