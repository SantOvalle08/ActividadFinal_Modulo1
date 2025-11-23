"""
Sistema de Descomposicion de Billetes para Cajero Automatico
=============================================================

Este programa simula el funcionamiento de un cajero automatico que calcula
la cantidad optima de billetes necesarios para entregar un monto solicitado,
utilizando la menor cantidad posible de billetes.

Autor: Santiago Ovalle
Fecha: Noviembre 2025
Curso: Programacion en Python - DevSenior
"""

# ============================================================================
# CONSTANTES GLOBALES
# ============================================================================

# Denominaciones de billetes disponibles en Colombia (en pesos COP)
DENOMINACIONES = [50000, 20000, 10000, 5000, 2000, 1000]

# Billete de menor denominación (usado para validación)
BILLETE_MINIMO = 1000


# ============================================================================
# FUNCIONES DE VALIDACIÓN
# ============================================================================

def validar_monto(mensaje: str) -> int:
    """
    Solicita y valida un monto de dinero al usuario.
    
    La funcion garantiza que el monto ingresado sea:
    - Un numero entero valido
    - Mayor que cero
    - Multiplo de 1000 (la denominacion mas pequena)
    
    Args:
        mensaje (str): Texto que se muestra al solicitar el monto
        
    Returns:
        int: Monto valido ingresado por el usuario
        
    Raises:
        Ninguna. Los errores se manejan internamente con reintentos.
    """
    while True:
        try:
            # Solicitar entrada al usuario
            entrada = input(mensaje)
            
            # Convertir a entero (puede lanzar ValueError)
            monto = int(entrada)
            
            # Validar que sea positivo
            if monto <= 0:
                print("ERROR: El monto debe ser mayor que cero.")
                print("Por favor ingrese nuevamente.\n")
                continue
            
            # Validar que sea multiplo de 1000
            if monto % BILLETE_MINIMO != 0:
                print(f"ERROR: El monto debe ser multiplo de ${BILLETE_MINIMO:,}")
                print("Por favor ingrese nuevamente.\n")
                continue
            
            # Si pasa todas las validaciones, retornar el monto
            return monto
            
        except ValueError:
            # Manejar errores de conversion (entrada no numerica)
            print("ERROR: Debe ingresar un numero valido.")
            print("Por favor intente de nuevo.\n")


# ============================================================================
# FUNCIONES DE LÓGICA DE NEGOCIO
# ============================================================================

def descomponer_billetes(monto: int, denominaciones: list[int]) -> dict[int, int]:
    """
    Calcula la cantidad optima de billetes necesarios para un monto dado.
    
    Utiliza un algoritmo greedy (voraz) que selecciona siempre el billete
    de mayor denominacion posible, garantizando la solucion optima.
    
    Args:
        monto (int): Cantidad total de dinero a descomponer
        denominaciones (list[int]): Lista de valores de billetes disponibles
                                     (debe estar ordenada de mayor a menor)
    
    Returns:
        dict[int, int]: Diccionario donde las claves son las denominaciones
                        y los valores son las cantidades de billetes necesarios.
                        Solo incluye denominaciones con cantidad > 0
    
    Example:
        >>> descomponer_billetes(187000, [50000, 20000, 10000, 5000, 2000, 1000])
        {50000: 3, 20000: 1, 10000: 1, 5000: 1, 2000: 1}
    """
    resultado = {}
    monto_restante = monto
    
    # Iterar sobre cada denominacion de mayor a menor
    for denominacion in denominaciones:
        # Calcular cuantos billetes de esta denominacion caben
        cantidad_billetes = monto_restante // denominacion
        
        # Si se necesita al menos un billete de esta denominacion
        if cantidad_billetes > 0:
            # Guardar en el diccionario
            resultado[denominacion] = cantidad_billetes
            
            # Restar el valor usado del monto restante
            monto_restante = monto_restante % denominacion
        
        # Si ya no queda dinero por descomponer, terminar
        if monto_restante == 0:
            break
    
    return resultado


# ============================================================================
# FUNCIONES DE PRESENTACIÓN
# ============================================================================

def mostrar_encabezado() -> None:
    """
    Muestra el encabezado visual del programa.
    """
    print("\n" + "="*60)
    print("SISTEMA DE DESCOMPOSICION DE BILLETES")
    print("="*60)
    print("Calcula la cantidad optima de billetes para un retiro")
    print("="*60 + "\n")


def mostrar_resultado(monto_original: int, billetes: dict[int, int]) -> None:
    """
    Presenta los resultados de la descomposicion de forma clara y profesional.
    
    Muestra:
    - El monto original solicitado
    - Cada denominacion de billete y su cantidad
    - El total de billetes necesarios
    
    Args:
        monto_original (int): Monto total solicitado
        billetes (dict[int, int]): Diccionario con denominaciones y cantidades
    """
    print("\n" + "-"*60)
    print(f"Monto solicitado: ${monto_original:,} COP")
    print("-"*60)
    print("\nBilletes necesarios:\n")
    
    # Mostrar cada denominacion y cantidad
    total_billetes = 0
    for denominacion, cantidad in billetes.items():
        print(f"  Billetes de ${denominacion:,}: {cantidad}")
        total_billetes += cantidad
    
    # Mostrar total de billetes
    print("\n" + "-"*60)
    print(f"Total de billetes a entregar: {total_billetes}")
    print("-"*60 + "\n")


def preguntar_continuar() -> bool:
    """
    Pregunta al usuario si desea realizar otra transaccion.
    
    Returns:
        bool: True si el usuario desea continuar, False en caso contrario
    """
    while True:
        respuesta = input("Desea realizar otra transaccion? (s/n): ").strip().lower()
        
        if respuesta in ['s', 'si', 'yes', 'y']:
            return True
        elif respuesta in ['n', 'no']:
            return False
        else:
            print("Por favor responda 's' para si o 'n' para no.\n")


# ============================================================================
# FUNCIÓN PRINCIPAL
# ============================================================================

def main() -> None:
    """
    Funcion principal que orquesta el flujo del programa.
    
    Coordina:
    1. Presentacion del programa
    2. Validacion de entrada del usuario
    3. Calculo de descomposicion de billetes
    4. Presentacion de resultados
    5. Opcion de realizar multiples transacciones
    """
    # Mostrar encabezado del programa
    mostrar_encabezado()
    
    # Bucle principal para permitir multiples transacciones
    continuar = True
    
    while continuar:
        # Paso 1: Solicitar y validar el monto
        monto = validar_monto("Ingrese el monto a retirar (COP): $")
        
        # Paso 2: Calcular la descomposicion de billetes
        billetes = descomponer_billetes(monto, DENOMINACIONES)
        
        # Paso 3: Mostrar resultados
        mostrar_resultado(monto, billetes)
        
        # Paso 4: Preguntar si desea continuar
        continuar = preguntar_continuar()
        
        if continuar:
            print("\n" + "="*60 + "\n")
    
    # Mensaje de despedida
    print("\n" + "="*60)
    print("Gracias por usar nuestro sistema. Hasta pronto!")
    print("="*60 + "\n")


# ============================================================================
# PUNTO DE ENTRADA DEL PROGRAMA
# ============================================================================

if __name__ == "__main__":
    """
    Punto de entrada principal del programa.
    Se ejecuta solo cuando el archivo se ejecuta directamente,
    no cuando se importa como modulo.
    """
    main()
