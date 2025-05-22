
---

## ¿Qué es un condicional?

En programación, un **condicional** es una estructura de control que permite ejecutar diferentes bloques de código basándose en si una condición específica es verdadera (`True`) o falsa (`False`). Sería como uan decisión, si se cumple la condición haz esto, sino lo otro. Las sentencias condicionales más comunes en Python son `if`, `else`, y `elif` (una abreviatura de "else if"). Las condiciones en programación son esenciales para que tu desarrollo tome decisiones y siga distintos caminos de ejecución.

---

## ¿Cuáles son los diferentes tipos de bucles en Python?

En Python, los dos tipos principales de bucles son:

* **`for`**: Este bucle se usa para **iterar** (recorrer los elementos de una secuencia o colección uno por uno) sobre una secuencia (como una lista, tupla, cadena de texto o rango) o cualquier otro objeto que sea "iterable". Ejecuta un bloque de código una vez por cada elemento de la secuencia.
* **`while`**: Este bucle ejecuta un bloque de código **mientras una condición específica sea verdadera**. Es crucial asegurarte de que la condición eventualmente se vuelva falsa para evitar que el bucle se ejecute indefinidamente (un "bucle infinito").

---

### ¿Por qué son útiles?

Los bucles son fundamentales porque te permiten **automatizar tareas repetitivas**. En lugar de escribir el mismo código muchas veces, puedes usar un bucle para realizar una acción sobre múltiples elementos o hasta que se cumpla una cierta condición. Esto hace que tu código sea más eficiente, conciso y fácil de mantener.

---

## ¿Qué es una lista por comprensión en Python?

Una **lista por comprensión** (del inglés, *list comprehension*) es una forma concisa y elegante de crear nuevas listas a partir de listas existentes u otros objetos iterables. Ofrece una sintaxis mucho más corta para construir una lista aplicando una expresión a cada elemento de un iterable y, opcionalmente, filtrando los elementos que cumplen una determinada condición.

Por ejemplo, para crear una lista con los cuadrados de los números del 0 al 4:

---

## ¿Qué es un argumento en Python?

En Python, un argumento es un valor que se pasa a una función (o método) cuando la llamas. Los argumentos son vitales porque permiten que las funciones operen con datos diferentes cada vez que se ejecutan, haciéndolas más flexibles y reutilizables.

Existen varios tipos de argumentos:

**Argumentos posicionales:** Se pasan en el orden en que se definen en la función.

**Argumentos de palabra clave (keyword arguments):** Se pasan especificando el nombre del parámetro al que se asigna el valor (por ejemplo, nombre="Juan"). Esto permite pasar argumentos en cualquier orden y mejora la legibilidad del código.

**Argumentos por defecto:** Son valores preestablecidos para los parámetros en la definición de la función. Si no proporcionas un valor para ese parámetro al llamar a la función, se usa el valor por defecto.

***args (argumentos variables posicionales):** Permite que una función acepte un número variable de argumentos posicionales. Estos se agrupan en una tupla dentro de la función.

****kwargs (argumentos variables de palabra clave):** Permite que una función acepte un número variable de argumentos de palabra clave. Estos se agrupan en un diccionario dentro de la función.

