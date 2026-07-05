"""
---------------------------------------------------------
PROYECTO DE MÉTODOS NUMÉRICOS
Método de Euler Mejorado y Runge-Kutta de 4° Orden

Autor(es):
Fecha:

Descripción:
Programa para resolver un Problema de Valor Inicial (PVI)
utilizando los métodos de Euler Mejorado y
Runge-Kutta de cuarto orden.
---------------------------------------------------------
"""

# ==========================================================
# FUNCIÓN DEL PROBLEMA
# ==========================================================

def f(x, y):
    """
    Función diferencial.

    IMPORTANTE:
    Cambiar únicamente esta función cuando el profesor
    indique un nuevo problema.

    Ejemplo:
        y' = x + y
    """
    return x + y

# Ecuación en formato texto para mostrar al usuario y facilitar futuros cambios
ECUACION = "x + y"


# ==========================================================
# EULER MEJORADO
# ==========================================================

def euler_mejorado(f, x0, y0, h, xf, n):
    resultados = []

    x = x0
    y = y0
    paso = 0

    resultados.append((paso, x, y))

    print("\nProcedimiento detallado - Método de Euler Mejorado")

    for i in range(n):

        # Pendiente inicial
        k1 = f(x, y)

        # Predicción de Euler
        y_pred = y + h * k1

        # Pendiente corregida
        k2 = f(x + h, y_pred)

        # Corrección (no cambiar la lógica matemática)
        y_nuevo = y + (h / 2) * (k1 + k2)

        # Mostrar procedimiento de la iteración en varias líneas
        print("-" * 76)
        print(f"Iteración {i+1}")
        print(f"  x       = {x:.6f}")
        print(f"  y       = {y:.8f}")
        print(f"  k1      = {k1:.8f}")
        print(f"  y_pred  = {y_pred:.8f}")
        print(f"  k2      = {k2:.8f}")
        print(f"  y_nuevo = {y_nuevo:.8f}")
        print("-" * 76)

        # Actualizar valores para la siguiente iteración
        y = y_nuevo
        paso += 1
        x = x0 + paso * h

        resultados.append((paso, x, y))

    return resultados


# ==========================================================
# RUNGE-KUTTA ORDEN 4
# ==========================================================

def runge_kutta4(f, x0, y0, h, xf, n):
    resultados = []

    x = x0
    y = y0
    paso = 0

    resultados.append((paso, x, y))

    print("\nProcedimiento detallado - Método de Runge-Kutta 4")

    for i in range(n):

        k1 = f(x, y)

        k2 = f(
            x + h / 2,
            y + h * k1 / 2
        )

        k3 = f(
            x + h / 2,
            y + h * k2 / 2
        )

        k4 = f(
            x + h,
            y + h * k3
        )

        y_nuevo = y + (h / 6) * (
            k1 +
            2 * k2 +
            2 * k3 +
            k4
        )

        # Mostrar procedimiento de la iteración en varias líneas
        print("-" * 76)
        print(f"Iteración {i+1}")
        print(f"  x       = {x:.6f}")
        print(f"  y       = {y:.8f}")
        print(f"  k1      = {k1:.8f}")
        print(f"  k2      = {k2:.8f}")
        print(f"  k3      = {k3:.8f}")
        print(f"  k4      = {k4:.8f}")
        print(f"  y_nuevo = {y_nuevo:.8f}")
        print("-" * 76)

        # Actualizar valores para la siguiente iteración
        y = y_nuevo
        paso += 1
        x = x0 + paso * h

        resultados.append((paso, x, y))

    return resultados


# ==========================================================
# IMPRESIÓN DE TABLAS
# ==========================================================

def imprimir_tabla(nombre, datos):

    print("\n")
    print("=" * 60)
    print(nombre.center(60))
    print("=" * 60)

    print(f"{'Paso':<8}{'x':<15}{'y':<20}")

    print("-" * 60)

    for paso, x, y in datos:

        print(
            f"{paso:<8}"
            f"{x:<15.4f}"
            f"{y:<20.8f}"
        )


# ==========================================================
# INGRESO DE DATOS
# ==========================================================

def leer_datos():

    print("=" * 60)
    print("RESOLUCIÓN DE PVI".center(60))
    print("=" * 60)

    # Leer x0
    while True:
        entrada = input("Ingrese x0: ")
        try:
            x0 = float(entrada)
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    # Leer y0
    while True:
        entrada = input("Ingrese y0: ")
        try:
            y0 = float(entrada)
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    # Leer xf (debe ser mayor que x0)
    while True:
        entrada = input("Ingrese xf: ")
        try:
            xf = float(entrada)
            if xf <= x0:
                print("El valor final xf debe ser mayor que x0.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    # Leer h (debe ser mayor que 0)
    while True:
        entrada = input("Ingrese el tamaño del paso h: ")
        try:
            h = float(entrada)
            if h <= 0:
                print("El tamaño del paso (h) debe ser mayor que cero.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    return x0, y0, xf, h


# ==========================================================
# PROGRAMA PRINCIPAL
# ==========================================================

def main():
    while True:

        print("\n" + "=" * 60)
        print("        MÉTODOS NUMÉRICOS PARA PVI".center(60))
        print("=" * 60)
        print("1. Resolver utilizando Euler Mejorado")
        print("2. Resolver utilizando Runge-Kutta de 4° Orden")
        print("3. Resolver utilizando ambos métodos")
        print("4. Salir")

        try:
            opcion = int(input("\nSeleccione una opción (1-4): "))
        except ValueError:
            print("Opción no válida. Intente nuevamente.")
            continue

        if opcion == 4:
            print("Saliendo...")
            break

        if opcion not in (1, 2, 3):
            print("Opción no válida. Intente nuevamente.")
            continue

        x0, y0, xf, h = leer_datos()

        # Mostrar resumen antes de comenzar los cálculos
        print("\n" + "=" * 60)
        print("PROBLEMA DE VALOR INICIAL".center(60))
        print("=" * 60)
        print(f"Función: y' = {ECUACION}")
        print(f"Condición inicial x0 = {x0}")
        print(f"Condición inicial y0 = {y0}")
        print(f"Valor final xf = {xf}")
        print(f"Paso h = {h}")


        # Calcular número de iteraciones una sola vez
        ratio = (xf - x0) / h
        nearest = int(round(ratio))
        tol = 1e-9
        if abs(ratio - nearest) > tol:
            print("\nADVERTENCIA")
            print("El tamaño del paso (h) no divide exactamente el intervalo.")
            print("El último punto calculado puede no coincidir exactamente con xf.")
            print("El programa continuará utilizando el número de iteraciones más cercano.")

        n = nearest
        print(f"\nNúmero de iteraciones: {n}")

        euler = rk4 = None

        if opcion == 1 or opcion == 3:
            euler = euler_mejorado(f, x0, y0, h, xf, n)
            imprimir_tabla("MÉTODO DE EULER MEJORADO", euler)

        if opcion == 2 or opcion == 3:
            rk4 = runge_kutta4(f, x0, y0, h, xf, n)
            imprimir_tabla("MÉTODO DE RUNGE-KUTTA ORDEN 4", rk4)

        # Comparación final si se ejecutaron ambos métodos
        if opcion == 3 and euler is not None and rk4 is not None:
            y_euler = euler[-1][2]
            x_euler = euler[-1][1]
            y_rk4 = rk4[-1][2]
            x_rk4 = rk4[-1][1]
            # Preferir el último x calculado (de ambos debería ser similar)
            x_final = x_euler
            diferencia = abs(y_euler - y_rk4)

            print("\n" + "=" * 60)
            print("COMPARACIÓN FINAL".center(60))
            print("=" * 60)
            print(f"Último valor de x: {x_final:.4f}")
            print("\nEuler Mejorado\n  y = {:.8f}".format(y_euler))
            print("Runge-Kutta 4\n  y = {:.8f}".format(y_rk4))
            print("\nDiferencia absoluta: {:.8f}".format(diferencia))

        # Encabezado final
        print("\n" + "=" * 60)
        print("Proceso finalizado correctamente. Gracias por utilizar el programa.".center(60))
        print("=" * 60)

        input("\nPresione Enter para continuar en el menú...")


# ==========================================================

if __name__ == "__main__":
    main()