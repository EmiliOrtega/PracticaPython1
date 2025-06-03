import pandas as pd

def ingresar_datos():
    estudiantes = {}
    while True:
        nombre = input("Nombre del estudiante (o escribe 'salir'): ")
        if nombre.lower() == 'salir':
            break
        try:
            notas = input("Ingresa las calificaciones separadas por coma: ")
            calificaciones = [float(n) for n in notas.split(',')]
            estudiantes[nombre] = calificaciones
        except ValueError:
            print("Error: ingresa números válidos.")
    return estudiantes

def calcular_promedios(estudiantes):
    promedios = {nombre: sum(notas)/len(notas) for nombre, notas in estudiantes.items()}
    return promedios

def estudiante_destacado(promedios):
    return max(promedios, key=promedios.get)

def guardar_resultados(estudiantes, promedios, mejor):
    with open("resultados.txt", "w") as f:
        for nombre, notas in estudiantes.items():
            f.write(f"{nombre}: Notas: {notas}, Promedio: {promedios[nombre]:.2f}\n")
        f.write(f"\nEstudiante con mejor promedio: {mejor} ({promedios[mejor]:.2f})\n")

def main():
    estudiantes = ingresar_datos()
    if estudiantes:
        promedios = calcular_promedios(estudiantes)
        mejor = estudiante_destacado(promedios)
        guardar_resultados(estudiantes, promedios, mejor)
        print("Resultados guardados en 'resultados.txt'")
    else:
        print("No se ingresaron datos.")

if __name__ == "__main__":
    main()
