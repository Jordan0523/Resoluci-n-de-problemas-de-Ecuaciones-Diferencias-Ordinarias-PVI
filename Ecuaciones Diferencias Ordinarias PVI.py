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

import math

# ==========================================================
# FUNCIÓN DEL PROBLEMA (ingresada por el usuario en tiempo de ejecución)
# ==========================================================

# Funciones y constantes matemáticas permitidas dentro de la ecuación
FUNCIONES_PERMITIDAS = {
    "sin": math.sin, "cos": math.cos, "tan": math.tan,
    "asin": math.asin, "acos": math.acos, "atan": math.atan,
    "sinh": math.sinh, "cosh": math.cosh, "tanh": math.tanh,
    "exp": math.exp, "log": math.log, "log10": math.log10, "ln": math.log,
    "sqrt": math.sqrt, "fabs": math.fabs, "pow": pow,
    "pi": math.pi, "e": math.e,
}


def construir_funcion(expresion):
    """
    Convierte un string como 'x**3*y - 1.5*y' o 'x^3*y - 1.5*y'
    (ingresado por el usuario) en una función f(x, y) evaluable.
    """
    expr_normalizada = expresion.replace("^", "**")

    def f(x, y):
        entorno = dict(FUNCIONES_PERMITIDAS)
        entorno["x"] = x
        entorno["y"] = y
        entorno["__builtins__"] = {}
        return eval(expr_normalizada, entorno)

    return f


def leer_ecuacion():
    """
    Solicita al usuario la ecuación diferencial y' = f(x, y)
    y devuelve una función evaluable junto con el texto ingresado.
    """
    print("=" * 60)
    print("INGRESO DE LA ECUACIÓN DIFERENCIAL".center(60))
    print("=" * 60)
    print("Ingrese y' = f(x, y) usando sintaxis de Python.")
    print("Operadores: + - * / ** (o ^ para potencia)")
    print("Funciones disponibles: sin, cos, tan, asin, acos, atan,")
    print("                       sinh, cosh, tanh, exp, log, log10,")
    print("                       sqrt, fabs, pow  |  Constantes: pi, e")
    print("Ejemplos: x**3*y - 1.5*y   |   x + y   |   sin(x) - y**2")
    print("-" * 60)

    while True:
        expresion = input("y' = ").strip()
        if not expresion:
            print("La ecuación no puede estar vacía.")
            continue

        f = construir_funcion(expresion)

        # Validar que la expresión sea evaluable con un punto de prueba
        try:
            f(1.0, 1.0)
        except ZeroDivisionError:
            print("Error: la ecuación produce una división por cero en el punto de prueba.")
            continue
        except (ValueError, ArithmeticError):
            print("Error: la ecuación no es válida en el punto de prueba (dominio inválido).")
            continue
        except NameError as error:
            print(f"Error: nombre no reconocido en la ecuación ({error}). Revise la sintaxis.")
            continue
        except SyntaxError:
            print("Error: sintaxis inválida. Revise la ecuación ingresada.")
            continue
        except Exception as error:
            print(f"Error al interpretar la ecuación: {error}")
            continue

        return f, expresion


# ==========================================================
# EULER MEJORADO
# ==========================================================

def euler_mejorado(f, x0, y0, h, n):
    resultados = []

    x = x0
    y = y0
    paso = 0

    resultados.append((paso, x, y))

    print("\nProcedimiento detallado - Método de Euler Mejorado")

    for i in range(n):

        try:
            # Pendiente inicial
            k1 = f(x, y)

            # Predicción de Euler
            y_pred = y + h * k1

            # Pendiente corregida
            k2 = f(x + h, y_pred)

            # Corrección (no cambiar la lógica matemática)
            y_nuevo = y + (h / 2) * (k1 + k2)

            if math.isnan(y_nuevo) or math.isinf(y_nuevo):
                raise OverflowError("resultado no finito (NaN o infinito)")

        except (OverflowError, ValueError, ZeroDivisionError, ArithmeticError) as error:
            print("-" * 76)
            print(f"La solución diverge (se vuelve infinita) cerca de x = {x:.6f}.")
            print(f"Detalle: {error}")
            print("Es probable que la ecuación no tenga solución finita en todo el")
            print("intervalo solicitado. Se muestran los resultados hasta este punto.")
            print("-" * 76)
            break

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

def runge_kutta4(f, x0, y0, h, n):
    resultados = []

    x = x0
    y = y0
    paso = 0

    resultados.append((paso, x, y))

    print("\nProcedimiento detallado - Método de Runge-Kutta 4")

    for i in range(n):

        try:
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

            if math.isnan(y_nuevo) or math.isinf(y_nuevo):
                raise OverflowError("resultado no finito (NaN o infinito)")

        except (OverflowError, ValueError, ZeroDivisionError, ArithmeticError) as error:
            print("-" * 76)
            print(f"La solución diverge (se vuelve infinita) cerca de x = {x:.6f}.")
            print(f"Detalle: {error}")
            print("Es probable que la ecuación no tenga solución finita en todo el")
            print("intervalo solicitado. Se muestran los resultados hasta este punto.")
            print("-" * 76)
            break

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
        entrada = input("Ingrese x0:")
        try:
            x0 = float(entrada)
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    # Leer y0
    while True:
        entrada = input("Ingrese y0:")
        try:
            y0 = float(entrada)
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    # Leer xn (debe ser mayor que x0)
    while True:
        entrada = input("Ingrese xn:")
        try:
            xn = float(entrada)
            if xn <= x0:
                print("El valor final xn debe ser mayor que x0.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número.")

    # Leer número de intervalos n (entero > 0)
    while True:
        entrada = input("Ingrese número de intervalos (n):")
        try:
            n = int(entrada)
            if n <= 0:
                print("El número de intervalos debe ser un entero mayor que 0.")
                continue
            break
        except ValueError:
            print("Entrada no válida. Debe ingresar un número entero válido.")

    # Calcular tamaño del paso h
    h = (xn - x0) / n

    # Mostrar resumen de datos del problema
    print("========================================DATOS DEL PROBLEMA========================================")
    print(f"x0 = {x0}")
    print(f"y0 = {y0}")
    print(f"xn = {xn}")
    print(f"Número de intervalos = {n}")
    print(f"Tamaño del paso (h) = {h}")

    return x0, y0, xn, n, h


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

        f, ECUACION = leer_ecuacion()
        x0, y0, xn, n, h = leer_datos()

        # Mostrar resumen antes de comenzar los cálculos
        print("\n" + "=" * 60)
        print("PROBLEMA DE VALOR INICIAL".center(60))
        print("=" * 60)
        print(f"Función: y' = {ECUACION}")
        print(f"Condición inicial x0 = {x0}")
        print(f"Condición inicial y0 = {y0}")
        print(f"Valor final xn = {xn}")
        print(f"Paso h = {h}")

        # Número de iteraciones igual al número de intervalos ingresado
        print(f"\nNúmero de iteraciones: {n}")

        euler = rk4 = None

        if opcion == 1 or opcion == 3:
            euler = euler_mejorado(f, x0, y0, h, n)
            imprimir_tabla("MÉTODO DE EULER MEJORADO", euler)

        if opcion == 2 or opcion == 3:
            rk4 = runge_kutta4(f, x0, y0, h, n)
            imprimir_tabla("MÉTODO DE RUNGE-KUTTA ORDEN 4", rk4)

        # Comparación final si se ejecutaron ambos métodos
        if opcion == 3 and euler is not None and rk4 is not None:
            y_euler = euler[-1][2]
            x_euler = euler[-1][1]
            y_rk4 = rk4[-1][2]
            x_rk4 = rk4[-1][1]

            print("\n" + "=" * 60)
            print("COMPARACIÓN FINAL".center(60))
            print("=" * 60)

            if abs(x_euler - x_rk4) > 1e-9:
                # Alguno de los dos métodos divergió antes de llegar a xn
                print("Aviso: los dos métodos no llegaron al mismo valor de x")
                print("porque al menos uno de ellos divergió antes de alcanzar xn.")
                print(f"Euler Mejorado llegó hasta x = {x_euler:.6f}, y = {y_euler:.8f}")
                print(f"Runge-Kutta 4 llegó hasta x = {x_rk4:.6f}, y = {y_rk4:.8f}")
                continue_comparacion = False
            else:
                continue_comparacion = True

            if continue_comparacion:
                x_final = x_euler
                diferencia = abs(y_euler - y_rk4)
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