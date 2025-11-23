# 🏦 Sistema de Descomposición de Billetes

## 📌 Descripción del Proyecto

Este programa simula el funcionamiento de un **cajero automático** que calcula la cantidad óptima de billetes necesarios para entregar un monto solicitado por el usuario, utilizando la **menor cantidad posible de billetes**.

El sistema trabaja con las denominaciones de billetes colombianos (COP) y aplica un **algoritmo greedy** para garantizar la solución óptima.

---

## 🎯 Objetivo

Demostrar el dominio de conceptos fundamentales de programación en Python, incluyendo:
- **Funciones modulares** con responsabilidades únicas
- **Validación robusta** de datos de entrada
- **Manejo de excepciones** con try-except
- **Type hints** para claridad del código
- **Documentación** con docstrings
- **Buenas prácticas** de programación

---

## 💵 Denominaciones Disponibles

El programa trabaja con las siguientes denominaciones de billetes colombianos:
- $50,000 COP
- $20,000 COP
- $10,000 COP
- $5,000 COP
- $2,000 COP
- $1,000 COP

---

## ⚙️ Funcionalidades

### 1. **Validación de Entrada**
- Verifica que el monto sea un número entero válido
- Asegura que sea mayor que cero
- Valida que sea múltiplo de $1,000 (el billete más pequeño)
- Maneja errores y solicita reintentos cuando sea necesario

### 2. **Algoritmo de Descomposición**
- Utiliza el **algoritmo greedy** (voraz)
- Selecciona siempre el billete de mayor denominación posible
- Garantiza la solución con la menor cantidad de billetes
- Usa división entera (`//`) y módulo (`%`) para optimizar el cálculo

### 3. **Presentación de Resultados**
- Muestra el monto solicitado
- Lista cada denominación de billete y su cantidad
- Indica el total de billetes a entregar
- Formato claro y profesional con emojis y separadores

### 4. **Múltiples Transacciones**
- Permite realizar varias operaciones sin reiniciar el programa
- Pregunta al usuario si desea continuar después de cada transacción

---

## 🚀 Cómo Ejecutar el Programa

### Requisitos
- Python 3.8 o superior

### Pasos
1. Clona o descarga este repositorio
2. Navega a la carpeta del proyecto
3. Ejecuta el programa:
   ```bash
   python codigo_fuente.py
   ```

---

## 📖 Ejemplos de Uso

### Ejemplo 1: Caso Simple
```
💵 Ingrese el monto a retirar (COP): $50000

💰 Monto solicitado: $50,000 COP
------------------------------------------------------------
📋 Billetes necesarios:
   💵 Billetes de $50,000: 1

📊 Total de billetes a entregar: 1
```

### Ejemplo 2: Caso Complejo
```
💵 Ingrese el monto a retirar (COP): $187000

💰 Monto solicitado: $187,000 COP
------------------------------------------------------------
📋 Billetes necesarios:
   💵 Billetes de $50,000: 3
   💵 Billetes de $20,000: 1
   💵 Billetes de $10,000: 1
   💵 Billetes de $5,000: 1
   💵 Billetes de $2,000: 1

📊 Total de billetes a entregar: 7
```

### Ejemplo 3: Validación de Errores
```
💵 Ingrese el monto a retirar (COP): $12500
⚠️  Error: El monto debe ser múltiplo de $1,000
   Por favor ingrese nuevamente.

💵 Ingrese el monto a retirar (COP): $abc
⚠️  Error: Debe ingresar un número válido.
   Por favor intente de nuevo.
```

---

## 🏗️ Estructura del Código

El programa está organizado en módulos funcionales:

```python
# 1. CONSTANTES GLOBALES
DENOMINACIONES = [50000, 20000, 10000, 5000, 2000, 1000]

# 2. FUNCIONES DE VALIDACIÓN
validar_monto()  # Solicita y valida entrada del usuario

# 3. FUNCIONES DE LÓGICA DE NEGOCIO
descomponer_billetes()  # Implementa el algoritmo greedy

# 4. FUNCIONES DE PRESENTACIÓN
mostrar_encabezado()    # Interfaz visual
mostrar_resultado()     # Presenta resultados
preguntar_continuar()   # Gestiona múltiples transacciones

# 5. FUNCIÓN PRINCIPAL
main()  # Orquesta el flujo del programa

# 6. PUNTO DE ENTRADA
if __name__ == "__main__"
```

---

## 🧮 Conceptos Matemáticos Aplicados

### División Entera (`//`)
Calcula cuántos billetes de una denominación caben en el monto:
```python
187000 // 50000 = 3  # 3 billetes de $50,000
```

### Módulo (`%`)
Calcula el dinero restante después de usar una denominación:
```python
187000 % 50000 = 37000  # Quedan $37,000
```

### Algoritmo Greedy
Siempre selecciona el billete más grande posible primero, garantizando la solución óptima (menor cantidad de billetes totales).

---

## ✅ Buenas Prácticas Aplicadas

1. **Nombres Descriptivos**: Variables y funciones con nombres claros y significativos
2. **Modularidad**: Cada función tiene una única responsabilidad
3. **Type Hints**: Anotaciones de tipo para mayor claridad
4. **Docstrings**: Documentación completa en todas las funciones
5. **Manejo de Errores**: Try-except para validación robusta
6. **Constantes**: Uso de constantes globales para valores fijos
7. **Separación de Responsabilidades**: Lógica, validación y presentación separadas
8. **Código Limpio**: Comentarios, espaciado y organización profesional

---

## 🎓 Conceptos de Python Demostrados

- ✅ Funciones (`def`)
- ✅ Type hints (`int`, `str`, `dict`, `list`, `bool`)
- ✅ Docstrings
- ✅ Manejo de excepciones (`try-except`)
- ✅ Bucles (`while`, `for`)
- ✅ Condicionales (`if-elif-else`)
- ✅ Operadores matemáticos (`//`, `%`)
- ✅ Estructuras de datos (`dict`, `list`)
- ✅ F-strings y formato de números
- ✅ Constantes globales
- ✅ Guard clause (`if __name__ == "__main__"`)

---

## 👤 Autor

**Santiago Ovalle**  
Estudiante de DevSenior - Módulo de Python Senior AI
Actividad Final del Módulo 1: Explica tu Código  
Fecha: Noviembre 2025

---

## 📹 Video Explicativo

En el repositorio del ejercicio se encuentra adjunto el video explicativo, en el que se describe como este programa funciona de manera detallada.

---

## 📄 Licencia

Este proyecto es de uso educativo, parte de una actividad presentada para el curso de DevSenior: Python Senior AI.

