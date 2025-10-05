from scipy.optimize import linprog

def simplex():
    print("=== MÉTODO SIMPLEX ===")
    tipo = input("¿Deseas maximizar o minimizar? (max/min): ").strip().lower()

    n = int(input("Número de variables: "))
    m = int(input("Número de restricciones: "))

    print("\n--- Función objetivo ---")
    c = []
    for i in range(n):
        c.append(float(input(f"Coeficiente de x{i+1}: ")))

    # Si es maximización, scipy requiere multiplicar por -1
    if tipo == "max":
        c = [-x for x in c]

    print("\n--- Restricciones ---")
    A = []
    b = []
    for j in range(m):
        print(f"\nRestricción {j+1}:")
        fila = []
        for i in range(n):
            fila.append(float(input(f"Coeficiente de x{i+1}: ")))
        A.append(fila)

        signo = input("Signo de la restricción (<=, >=, =): ").strip()
        valor = float(input("Valor del lado derecho: "))

        # scipy solo maneja <=, así que si es >= multiplicamos por -1
        if signo == ">=":
            A[-1] = [-x for x in A[-1]]
            valor = -valor
        elif signo == "=":
            # Convertir igualdad a dos desigualdades (≤ y ≥)
            A.append([-x for x in fila])
            b.append(-valor)

        b.append(valor)

    print("\n--- Resolviendo con el método Simplex ---")

    res = linprog(c, A_ub=A, b_ub=b, method='highs')

    if res.success:
        if tipo == "max":
            print(f"\nValor óptimo Z = {round(-res.fun, 4)}")
        else:
            print(f"\nValor óptimo Z = {round(res.fun, 4)}")

        print("Valores de las variables:")
        for i, val in enumerate(res.x):
            print(f"x{i+1} = {round(val, 4)}")
    else:
        print("\nNo se encontró una solución óptima.")

if __name__ == "__main__":
    simplex()
