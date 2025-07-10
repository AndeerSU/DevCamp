
---

## ¿Qué diferencia a JavaScript de cualquier otro lenguaje de programación?

JavaScript (JS) es un lenguaje de programación de alto nivel que, a primera vista, puede parecer similar a otros lenguajes. Sin embargo, tiene **características únicas** que lo distinguen y lo hacen fundamental en el desarrollo web moderno.

### 1. Es el lenguaje del navegador web (Frontend)

La diferencia más significativa es que **JavaScript es el único lenguaje de programación nativo que entienden todos los navegadores web modernos**. Esto significa que es el motor detrás de la **interactividad** en cualquier sitio web que visitas.

* **¿Por qué se utiliza?** Permite que las páginas web no sean solo contenido estático. Con JS, puedes:
    * Crear animaciones y efectos visuales dinámicos.
    * Validar formularios antes de enviarlos al servidor.
    * Actualizar contenido en una página sin recargarla (como cuando le das "Me gusta" a una publicación y el contador se actualiza al instante).
    * Construir **aplicaciones web interactivas** (Single Page Applications como Gmail, Google Docs).
* **¿Para qué se utiliza?** Para toda la lógica que se ejecuta directamente en el **lado del cliente** (en la computadora del usuario), haciendo que la experiencia de usuario sea mucho más rica y dinámica.

### 2. Es un lenguaje interpretado y de alto nivel

* **Interpretado:** A diferencia de lenguajes como C++ o Java que necesitan ser "compilados" (traducidos a código máquina antes de ejecutarse), JavaScript se **interpreta en tiempo real** por el navegador. El código se lee y ejecuta línea por línea.
    * **Ventaja:** Facilita el desarrollo y la depuración, ya que puedes ver los cambios al instante.
    * **Desventaja (menor):** Puede ser un poco más lento en ejecución que los lenguajes compilados para tareas muy intensivas, aunque los motores JS modernos (como V8 de Chrome) son extremadamente rápidos.
* **Alto Nivel:** Esto significa que JS maneja muchos detalles de bajo nivel (como la gestión de memoria) por ti, permitiéndote concentrarte en la lógica de la aplicación.

### 3. Es multiparadigma

JavaScript no se encasilla en un solo estilo de programación. Soporta **varios paradigmas**, lo que lo hace muy flexible:

* **Programación Orientada a Objetos (POO):** Aunque utiliza un modelo de objetos basado en prototipos (diferente a la POO basada en clases tradicional de Java o C++), permite crear y manipular objetos.
* **Programación Funcional:** Permite tratar las funciones como "ciudadanos de primera clase", lo que significa que puedes pasarlas como argumentos, devolverlas desde otras funciones, etc.
* **Programación Imperativa:** Es el estilo más básico, donde das instrucciones paso a paso sobre cómo debe hacerse algo.

### 4. Su versatilidad: del frontend al backend (Node.js)

Originalmente, JS solo se ejecutaba en el navegador. Pero la llegada de **Node.js** cambió todo. Node.js es un entorno de ejecución que permite a JavaScript ejecutarse en el servidor (backend) o incluso en el escritorio y dispositivos IoT.

* **¿Por qué es importante?** Significa que puedes usar JavaScript para construir **aplicaciones completas de pila completa (full-stack)**, utilizando el mismo lenguaje tanto para el frontend como para el backend. Esto simplifica el desarrollo, ya que los equipos no necesitan cambiar de contexto de lenguaje.
* **Ejemplos:** Construir APIs REST, microservicios, herramientas de línea de comandos.

### 5. Tipado dinámico y débil

* **Tipado Dinámico:** No necesitas declarar el tipo de una variable (`string`, `number`, `boolean`) antes de asignarle un valor. El tipo se determina automáticamente en tiempo de ejecución y puede cambiar.

    ```
    let edad = 30; // 'edad' es un número
    edad = "treinta"; // Ahora 'edad' es una cadena, y JS no se queja
    ```
* **Tipado Débil (o Coerción Implícita):** JavaScript es permisivo con la conversión de tipos entre operaciones.

    ```
    let resultado = "5" + 3; // JavaScript convierte 3 a cadena y concatena: "53"
    let suma = "5" - 3;    // JavaScript convierte "5" a número y resta: 2
    ```
    Esto puede ser conveniente pero también una fuente de errores si no se entiende bien.

### En resumen

Lo que realmente diferencia a JavaScript es su **ubicuidad en la web** (ser el único lenguaje nativo del navegador), su **flexibilidad multiparadigma**, su **versatilidad** (frontend y backend con Node.js), y sus características de **tipado dinámico**. Es un lenguaje diseñado para la interactividad y la agilidad en el desarrollo.

---

## ¿Cuáles son algunos tipos de datos en JavaScript?

En JavaScript, cada valor que manejas tiene un **tipo de dato**. Comprender estos tipos es fundamental para trabajar correctamente con el lenguaje. JavaScript clasifica los tipos de datos en dos grandes categorías: **Primitivos** y **No Primitivos (Objetos)**.

### Tipos de Datos Primitivos

Son los tipos de datos más básicos y fundamentales. Son **inmutables**, lo que significa que una vez creados, su valor no puede ser modificado. Si "cambias" un valor primitivo, en realidad estás creando un nuevo valor.

1.  **`String` (Cadena de Texto)**
    * **¿Qué es?** Representa secuencias de caracteres (texto).
    * **Sintaxis:** Se encierran entre comillas simples (`' '`), comillas dobles (`" "`), o *backticks* (comillas invertidas `` ` ``) para los *template literals*.
    * **Ejemplos:**
        ```
        let nombre = "Alice";
        let mensaje = 'Hola mundo!';
        let direccion = `Calle Mayor, 123`; // Template literal
        ```

2.  **`Number` (Número)**
    * **¿Qué es?** Representa tanto números enteros como números decimales (flotantes). JavaScript no diferencia entre enteros y flotantes, todos son `Number`.
    * **Sintaxis:** Se escriben directamente.
    * **Ejemplos:**
        ```
        let edad = 30;           // Entero
        let precio = 99.99;      // Decimal
        let temperatura = -5;
        let cero = 0;
        ```
    * También incluye valores especiales como `Infinity` (infinito positivo), `-Infinity` (infinito negativo) y `NaN` (Not a Number - no es un número), que resulta de operaciones matemáticas inválidas (ej. `0/0`).

3.  **`Boolean` (Booleano)**
    * **¿Qué es?** Representa un valor lógico que solo puede ser `true` (verdadero) o `false` (falso). Son fundamentales para la lógica condicional.
    * **Sintaxis:** Las palabras clave `true` o `false`.
    * **Ejemplos:**
        ```
        let esMayorDeEdad = true;
        let estaAbierto = false;
        ```

4.  **`Undefined` (Indefinido)**
    * **¿Qué es?** Representa una variable que ha sido declarada pero a la que aún no se le ha asignado un valor. También es el valor que retorna una función si no hay un `return` explícito.
    * **Sintaxis:** El valor `undefined`.
    * **Ejemplos:**
        ```
        let ciudad; // 'ciudad' es undefined
        console.log(ciudad); // Salida: undefined

        function noRetornaNada() {
            // No hay return aquí
        }
        let resultado = noRetornaNada();
        console.log(resultado); // Salida: undefined
        ```

5.  **`Null` (Nulo)**
    * **¿Qué es?** Representa la ausencia intencional de cualquier valor o la ausencia de un objeto. Es un valor que se asigna explícitamente para indicar "ningún valor".
    * **Sintaxis:** La palabra clave `null`.
    * **Ejemplos:**
        ```
        let usuarioLogueado = null; // Indica que no hay usuario logueado
        ```
    * **Dato curioso:** En JavaScript, `typeof null` devuelve `"object"`. Esto es un error histórico del lenguaje, pero `null` es considerado un tipo primitivo.

6.  **`Symbol` (Símbolo)** (Desde ES6/ECMAScript 2015)
    * **¿Qué es?** Representa un identificador único e inmutable. Los símbolos se utilizan principalmente para crear claves de propiedades de objeto que garantizan no colisionar con otras claves.
    * **Sintaxis:** Se crean llamando a la función `Symbol()`.
    * **Ejemplos:**
        ```
        const ID = Symbol('id');
        const OTRO_ID = Symbol('id');
        console.log(ID === OTRO_ID); // Salida: false (cada Symbol es único)

        let obj = {
            [ID]: 123,
            "nombre": "Producto X"
        };
        console.log(obj[ID]); // Salida: 123
        ```

7.  **`BigInt` (Entero Grande)** (Desde ES2020)
    * **¿Qué es?** Representa números enteros de precisión arbitraria. Esto significa que puede manejar números enteros más grandes que los que `Number` puede representar con seguridad (el límite de `Number` es `2^53 - 1`).
    * **Sintaxis:** Se crea añadiendo `n` al final de un número entero.
    * **Ejemplos:**
        ```
        let numeroMuyGrande = 9007199254740991n; // Es un BigInt
        let otroNumero = BigInt(12345);
        ```

### Tipo de Datos No Primitivos (Objetos)

1.  **`Object` (Objeto)**
    * **¿Qué es?** El tipo `Object` es el tipo de dato fundamental no primitivo en JavaScript. Representa colecciones de pares clave-valor.
        * **Mutable:** A diferencia de los primitivos, los objetos son mutables; puedes cambiar sus propiedades después de crearlos.
        * **Pasados por referencia:** Cuando asignas un objeto a una nueva variable, ambas variables apuntan a la misma ubicación en memoria (la misma referencia).
    * **Sintaxis:** Se definen con llaves `{}`.
    * **Ejemplos:**
        ```
        let persona = {
            nombre: "Juan",
            edad: 25,
            ciudad: "Madrid"
        };

        // Arrays también son objetos en JS
        let colores = ["rojo", "verde", "azul"]; // En realidad, es un objeto Array

        // Funciones también son objetos en JS
        function saludar() {
            console.log("Hola");
        }
        ```
    * Arrays, Funciones, Fechas, y `null` (aunque `null` es primitivo, `typeof null` da "object") son todos subtipos de `Object` en JavaScript, lo que demuestra la naturaleza orientada a objetos del lenguaje.

### ¿Por qué es importante conocer los tipos de datos?

* **Comportamiento de las operaciones:** Diferentes tipos de datos se comportan de manera diferente con operadores (ej. `+` con números suma, con cadenas concatena).
* **Comparaciones:** Es crucial entender cómo `==` (comparación débil) y `===` (comparación estricta) manejan los tipos de datos y la coerción.
* **Depuración:** Saber los tipos de datos te ayuda a entender por qué tu código no funciona como esperas.
* **Optimización y buenas prácticas:** Usar el tipo de dato correcto hace tu código más eficiente y legible.

---

## ¿Cuáles son las tres funciones de String en JS?

Cuando hablamos de "funciones de String en JS", generalmente nos referimos a los **métodos** que tienen los objetos de tipo `String` (cadenas de texto) para manipular y trabajar con el texto. JavaScript proporciona una gran cantidad de métodos para cadenas, pero si tu pregunta se refiere a las **tres funciones más fundamentales o comúnmente utilizadas para manipular texto**, estas podrían ser:

1.  **`toUpperCase()` / `toLowerCase()` (Métodos de Transformación)**: Para cambiar el uso de mayúsculas y minúsculas.
2.  **`substring()` / `slice()` (Métodos de Extracción)**: Para extraer partes de una cadena.
3.  **`indexOf()` / `includes()` (Métodos de Búsqueda)**: Para encontrar texto dentro de una cadena.

Me centraré en estos tres grupos de métodos de manipulación de cadenas que son extremadamente comunes: **Transformación de Mayúsculas/Minúsculas, Extracción de Subcadenas y Búsqueda de Texto**.

### 1. `toUpperCase()` y `toLowerCase()`: Transformación de Mayúsculas/Minúsculas

Estos métodos se utilizan para cambiar la capitalización de una cadena.

* **`toUpperCase()`**: Convierte todos los caracteres de una cadena a mayúsculas.
    * **Sintaxis**: `cadena.toUpperCase()`
    * **Retorna**: Una nueva cadena con todos los caracteres en mayúsculas. La cadena original no se modifica (porque las cadenas son inmutables).
    * **Ejemplo**:
        ```
        let mensaje = "Hola Mundo";
        let mensajeMayusculas = mensaje.toUpperCase();
        console.log(mensajeMayusculas); // Salida: "HOLA MUNDO"
        console.log(mensaje);          // Salida: "Hola Mundo" (original sin cambios)
        ```

* **`toLowerCase()`**: Convierte todos los caracteres de una cadena a minúsculas.
    * **Sintaxis**: `cadena.toLowerCase()`
    * **Retorna**: Una nueva cadena con todos los caracteres en minúsculas.
    * **Ejemplo**:
        ```
        let nombre = "Juan PÉREZ";
        let nombreMinusculas = nombre.toLowerCase();
        console.log(nombreMinusculas); // Salida: "juan pérez"
        ```
* **¿Por qué se utilizan?**: Son muy útiles para estandarizar entradas de usuario (ej. convertir un código postal a mayúsculas para que coincida con una base de datos) o para comparaciones de texto que no deben ser sensibles a mayúsculas/minúsculas.

### 2. `substring()` y `slice()`: Extracción de Subcadenas

Estos métodos se utilizan para extraer una parte (subcadena) de una cadena más grande. Aunque tienen algunas diferencias sutiles, su propósito principal es el mismo.

* **`substring(startIndex, endIndex)`**: Extrae caracteres desde `startIndex` hasta (pero sin incluir) `endIndex`.
    * **Sintaxis**: `cadena.substring(inicio, fin)`
    * **Retorna**: Una nueva cadena que contiene la porción extraída.
    * **Notas**:
        * Si `fin` se omite, extrae hasta el final de la cadena.
        * Si `inicio` es mayor que `fin`, o si cualquiera de los argumentos es negativo, `substring` los trata como 0 o los invierte para que el menor sea el inicio y el mayor el fin.
    * **Ejemplo**:
        ```
        let texto = "JavaScript es genial";
        let parte1 = texto.substring(0, 4);  // Extrae de 0 a 3
        let parte2 = texto.substring(14);    // Extrae desde el índice 14 hasta el final
        let parte3 = texto.substring(10, 3); // Invierte los índices a (3, 10)
        console.log(parte1); // Salida: "Java"
        console.log(parte2); // Salida: "genial"
        console.log(parte3); // Salida: "aScript e"
        ```

* **`slice(startIndex, endIndex)`**: Muy similar a `substring`, pero maneja los argumentos negativos de manera diferente.
    * **Sintaxis**: `cadena.slice(inicio, fin)`
    * **Retorna**: Una nueva cadena que contiene la porción extraída.
    * **Notas**:
        * Los índices negativos se cuentan desde el final de la cadena (`-1` es el último carácter, `-2` es el penúltimo, etc.).
        * Si `inicio` es mayor que `fin`, devuelve una cadena vacía.
    * **Ejemplo**:
        ```
        let texto = "JavaScript es genial";
        let parteA = texto.slice(0, 4);   // "Java"
        let parteB = texto.slice(-6);     // Extrae los últimos 6 caracteres: "genial"
        let parteC = texto.slice(0, -7);  // Extrae desde el inicio hasta 7 caracteres antes del final: "JavaScript es"
        console.log(parteA); // Salida: "Java"
        console.log(parteB); // Salida: "genial"
        console.log(parteC); // Salida: "JavaScript es"
        ```
* **¿Por qué se utilizan?**: Son esenciales para analizar y manipular texto, como obtener una parte de una URL, un nombre de archivo sin su extensión, o un fragmento de una frase.

### 3. `indexOf()` y `includes()`: Búsqueda de Texto

Estos métodos se utilizan para buscar la presencia de una subcadena dentro de una cadena más grande.

* **`indexOf(searchValue, fromIndex)`**: Busca la primera ocurrencia de `searchValue` dentro de la cadena y devuelve el índice de la primera posición donde se encuentra.
    * **Sintaxis**: `cadena.indexOf(texto_a_buscar, indice_desde_donde_buscar)`
    * **Retorna**: El índice de la primera ocurrencia de `searchValue`. Si no se encuentra, retorna `-1`.
    * **Ejemplo**:
        ```
        let frase = "El perro corre y el gato duerme.";
        let indicePerro = frase.indexOf("perro");    // Busca "perro"
        let indiceGato = frase.indexOf("gato");      // Busca "gato"
        let indicePato = frase.indexOf("pato");      // Busca "pato" (no está)
        let indiceEl = frase.indexOf("el", 5);       // Busca "el" desde el índice 5
        console.log(indicePerro); // Salida: 3
        console.log(indiceGato);  // Salida: 15
        console.log(indicePato);  // Salida: -1
        console.log(indiceEl);    // Salida: 13 (el segundo "el")
        ```

* **`includes(searchValue, fromIndex)`**: Verifica si una cadena contiene una subcadena específica.
    * **Sintaxis**: `cadena.includes(texto_a_buscar, indice_desde_donde_buscar)`
    * **Retorna**: `true` si la subcadena se encuentra, `false` en caso contrario.
    * **Ejemplo**:
        ```
        let frase = "El perro corre y el gato duerme.";
        let tienePerro = frase.includes("perro");
        let tienePato = frase.includes("pato");
        let tieneGatoDesde20 = frase.includes("gato", 20); // Busca "gato" desde el índice 20
        console.log(tienePerro);       // Salida: true
        console.log(tienePato);        // Salida: false
        console.log(tieneGatoDesde20); // Salida: false (el gato está antes del índice 20)
        ```
* **¿Por qué se utilizan?**: Son cruciales para validar entradas, buscar palabras clave, filtrar texto y controlar el flujo de la aplicación basándose en la presencia de ciertas cadenas. `includes()` es a menudo preferible a `indexOf()` cuando solo necesitas saber si existe o no, ya que su propósito es más claro.

---

## ¿Qué es un condicional?

En programación, un **condicional** es una estructura de control que permite ejecutar diferentes bloques de código basándose en si una condición específica es verdadera o falsa. Es como tomar una decisión en la vida real: "Si llueve, llevo paraguas; si no, no lo llevo".

### ¿Por qué se utilizan?

Los condicionales son el pilar fundamental de la lógica en cualquier programa. Sin ellos, el código se ejecutaría siempre de la misma manera, sin poder adaptarse a diferentes situaciones, entradas de usuario o estados de la aplicación. Se utilizan para:

* **Tomar decisiones:** Controlar el flujo de ejecución del programa.
* **Validar datos:** Verificar si una entrada es correcta antes de procesarla.
* **Controlar el acceso:** Permitir o denegar el acceso a ciertas partes de la aplicación.
* **Responder a eventos:** Ejecutar código específico cuando ocurre algo (ej. clic de un botón).

### Sintaxis Principal: `if`, `else if`, `else`

La forma más común de condicional en JavaScript (y en muchos otros lenguajes) es la declaración `if...else if...else`.

* **`if` (Si)**: El bloque de código dentro del `if` se ejecuta **solo si la condición es verdadera (`true`)**.
    * **Sintaxis:**
        ```
        if (condicion) {
            // Código a ejecutar si la condición es verdadera
        }
        ```
    * **Ejemplo:**
        ```
        let edad = 18;
        if (edad >= 18) {
            console.log("Es mayor de edad."); // Salida: Es mayor de edad.
        }
        ```

* **`else` (Si no / De lo contrario)**: El bloque de código dentro del `else` se ejecuta **solo si la condición del `if` (y de cualquier `else if` anterior) es falsa (`false`)**. Es una alternativa al `if`.
    * **Sintaxis:**
        ```
        if (condicion) {
            // Código si la condición es verdadera
        } else {
            // Código si la condición es falsa
        }
        ```
    * **Ejemplo:**
        ```
        let temperatura = 25;
        if (temperatura < 0) {
            console.log("Hace mucho frío.");
        } else {
            console.log("La temperatura es agradable o alta."); // Salida: La temperatura es agradable o alta.
        }
        ```

* **`else if` (Si no, entonces si...)**: Permite añadir múltiples condiciones. Se evalúa **solo si la condición del `if` anterior (o `else if` anterior) fue falsa**. Si su propia condición es verdadera, se ejecuta su bloque de código y el resto de la cadena `else if`/`else` se ignora.
    * **Sintaxis:**
        ```
        if (condicion1) {
            // Código si condicion1 es verdadera
        } else if (condicion2) {
            // Código si condicion2 es verdadera (y condicion1 fue falsa)
        } else if (condicion3) {
            // Código si condicion3 es verdadera (y condicion1 y condicion2 fueron falsas)
        } else {
            // Código si ninguna de las condiciones anteriores fue verdadera
        }
        ```
    * **Ejemplo:**
        ```
        let calificacion = 85;
        if (calificacion >= 90) {
            console.log("Excelente");
        } else if (calificacion >= 80) { // calificacion es 85, así que esta es verdadera
            console.log("Muy bien");    // Salida: Muy bien
        } else if (calificacion >= 70) {
            console.log("Bien");
        } else {
            console.log("Necesita mejorar");
        }
        ```

### Valores "Truthy" y "Falsy" en JavaScript

En JavaScript, no solo los valores `true` y `false` puros se evalúan como booleanos en los condicionales. Hay valores que se consideran "**falsy**" (falsos) y el resto son "**truthy**" (verdaderos).

**Valores Falsy:**
* `false` (el booleano puro)
* `0` (el número cero)
* `-0` (el número cero negativo)
* `""` (cadena vacía)
* `null`
* `undefined`
* `NaN` (Not a Number)
* `document.all` (una peculiaridad histórica)

**Todos los demás valores son Truthy.** Esto incluye:
* `true`
* Cualquier número diferente de cero (positivo o negativo)
* Cualquier cadena no vacía (incluyendo `" "` con un espacio)
* Objetos vacíos `{}`
* Arrays vacíos `[]`
* Funciones
* Símbolos, BigInts

**Ejemplo de Truthy/Falsy:**
```
let nombreUsuario = ""; // Falsy
if (nombreUsuario) {
    console.log("Bienvenido, " + nombreUsuario);
} else {
    console.log("Por favor, ingrese su nombre de usuario."); // Salida: Por favor, ingrese su nombre de usuario.
}

let listaItems = []; // Truthy (aunque el array esté vacío)
if (listaItems) {
    console.log("La lista existe."); // Salida: La lista existe.
}
```

### Otras estructuras condicionales: `switch`

Para múltiples condiciones basadas en un solo valor, `switch` puede ser más legible que una larga cadena de `if...else if`.

* **Sintaxis:**
    ```
    switch (expresion) {
        case valor1:
            // Código si expresion === valor1
            break; // Importante para salir del switch
        case valor2:
            // Código si expresion === valor2
            break;
        default: // Opcional: si ningún caso coincide
            // Código por defecto
    }
    ```
* **Ejemplo:**
    ```
    let diaSemana = "martes";
    switch (diaSemana) {
        case "lunes":
            console.log("Es el primer día laboral.");
            break;
        case "martes":
            console.log("Martes de trabajo."); // Salida: Martes de trabajo.
            break;
        case "viernes":
            console.log("¡Casi fin de semana!");
            break;
        default:
            console.log("Día no reconocido.");
    }
    ```
Los condicionales son herramientas esenciales para construir programas que puedan adaptarse y responder de manera inteligente a diversas situaciones.

---

## ¿Qué es un operador ternario?

El **operador ternario** (también conocido como operador condicional ternario) es una forma concisa de escribir una declaración `if-else` simple en una sola línea. Es el único operador en JavaScript que toma tres operandos.

### Sintaxis

La sintaxis del operador ternario es la siguiente:

```
condicion ? expresionSiVerdadero : expresionSiFalso;
```
* **`condicion`**: Es una expresión que se evalúa como `true` o `false`.
* **`?`**: El operador ternario en sí mismo, que separa la condición de las expresiones resultantes.
* **`expresionSiVerdadero`**: Es la expresión que se ejecuta y cuyo resultado se devuelve si la `condicion` es `true`.
* **`:`**: Separa la expresión verdadera de la expresión falsa.
* **`expresionSiFalso`**: Es la expresión que se ejecuta y cuyo resultado se devuelve si la `condicion` es `false`.

### ¿Por qué se utiliza?

El operador ternario se utiliza para:

* **Concisión y legibilidad (para condiciones simples):** Reduce el código de un `if-else` de varias líneas a una sola. Esto puede hacer el código más compacto y fácil de leer para decisiones sencillas.
* **Asignación de valores condicionales:** Es ideal para asignar un valor a una variable basándose en una condición. Es su uso más común y recomendado.
* **Expresiones dentro de otras expresiones:** Al ser una expresión (que devuelve un valor), puedes incrustar un operador ternario dentro de otras expresiones, como una asignación o un argumento de función.

### Ejemplos de uso:

**Asignar un mensaje basado en una edad:**

```
let edad = 20;
let mensaje = (edad >= 18) ? "Eres mayor de edad." : "Eres menor de edad.";
console.log(mensaje); // Salida: Eres mayor de edad.

edad = 16;
mensaje = (edad >= 18) ? "Eres mayor de edad." : "Eres menor de edad.";
console.log(mensaje); // Salida: Eres menor de edad.
```

Comparado con un `if-else` tradicional:

```
let edad = 20;
let mensaje;
if (edad >= 18) {
    mensaje = "Eres mayor de edad.";
} else {
    mensaje = "Eres menor de edad.";
}
console.log(mensaje);
```

Como puedes ver, el ternario es mucho más compacto para este caso.

### Determinar el estado de un botón:

```
let estaAutenticado = true;
let textoBoton = estaAutenticado ? "Cerrar Sesión" : "Iniciar Sesión";
console.log(textoBoton); // Salida: Cerrar Sesión
```
Devolver un valor condicionalmente desde una función:

```
function obtenerSaludo(hora) {
    return (hora < 12) ? "Buenos días" : "Buenas tardes";
}
console.log(obtenerSaludo(10)); // Salida: Buenos días
console.log(obtenerSaludo(15)); // Salida: Buenas tardes
```

Uso en template literals:

```
let esPremium = false;
let precio = `El costo es de $${esPremium ? '19.99' : '9.99'}.`;
console.log(precio); // Salida: El costo es de $9.99.
```

### ¿Cuándo usarlo y cuándo no?

**Úsalo cuando:**

* Necesitas asignar condicionalmente un valor a una variable.
* La condición es simple y las expresiones resultantes son concisas.
* Quieres hacer tu código más compacto y legible para casos triviales.

**Evita usarlo cuando:**

* La lógica condicional es compleja o involucra múltiples condiciones anidadas. Anidar ternarios (`condicion1 ? (condicion2 ? valA : valB) : valC`) puede hacer el código muy difícil de leer y depurar.
* Las expresiones `expresionSiVerdadero` o `expresionSiFalso` son bloques de código largos o realizan múltiples operaciones. En esos casos, un `if-else` tradicional es mucho más claro.
* Necesitas ejecutar múltiples sentencias basadas en la condición (el ternario solo evalúa una expresión).

El **operador ternario** es una herramienta poderosa para simplificar el código en JavaScript, pero como toda herramienta, debe usarse con discernimiento para mantener la **legibilidad** y la **mantenibilidad**.

---

## ¿Cuál es la diferencia entre una declaración de función y una expresión de función?

En JavaScript, hay dos formas principales de definir una función, y aunque ambas crean una función, tienen diferencias clave en cómo se manejan en el "hospedaje" (hoisting) y cuándo están disponibles para ser llamadas.

### 1. Declaración de Función (Function Declaration)

Una declaración de función se define utilizando la palabra clave `function`, seguida del nombre de la función, sus parámetros entre paréntesis, y el cuerpo de la función entre llaves.

* **Sintaxis:**
    ```
    function nombreDeLaFuncion(parametro1, parametro2) {
        // Cuerpo de la función
        return algo;
    }
    ```

* **Hoisting (Hospedaje):** Esta es la diferencia más importante. Las declaraciones de función son "hospedadas" (hoisted). Esto significa que el intérprete de JavaScript "eleva" la declaración completa de la función (su nombre y su cuerpo) al inicio del ámbito actual (sea global o de otra función) antes de que se ejecute el código.

    * **¿Qué significa esto?** Que puedes llamar a una declaración de función antes de que sea definida en el código.

* **Ejemplo de Declaración de Función:**
    ```
    // ✅ ¡Puedes llamar a esta función antes de su definición!
    saludar("Ana"); // Salida: Hola, Ana

    function saludar(nombre) {
        console.log(`Hola, ${nombre}`);
    }

    // Y también puedes llamarla después, por supuesto.
    saludar("Pedro"); // Salida: Hola, Pedro
    ```

### 2. Expresión de Función (Function Expression)

Una expresión de función se define asignando una función (que puede ser anónima o tener un nombre) a una variable.

* **Sintaxis:**
    ```
    const nombreDeLaVariable = function(parametro1, parametro2) {
        // Cuerpo de la función
        return algo;
    };
    ```
    O con un nombre (menos común, para recursión interna o depuración):
    ```
    const nombreDeLaVariable = function nombreInterno(parametro1, parametro2) {
        // Cuerpo de la función
        return algo;
    };
    ```

* **Hoisting:** A diferencia de las declaraciones, las expresiones de función no son hospedadas de la misma manera. Solo la declaración de la variable (por ejemplo, `const miFuncion;`) es hospedada, pero la asignación del valor de la función a esa variable no lo es.

    * **¿Qué significa esto?** No puedes llamar a una expresión de función antes de la línea en la que ha sido definida y asignada a la variable. Si intentas hacerlo, obtendrás un `ReferenceError` (si la variable no ha sido declarada) o un `TypeError` (si la variable fue declarada pero la función aún no ha sido asignada).

* **Ejemplo de Expresión de Función:**
    ```
    // ❌ Error: TypeError: calcularArea is not a function
    // Esto sucede porque la variable 'calcularArea' existe (por hoisting de 'let'),
    // pero el valor de la función no ha sido asignado aún.
    // console.log(calcularArea(5, 10));

    let calcularArea = function(ancho, alto) {
        return ancho * alto;
    };

    // ✅ Ahora sí puedes llamarla
    console.log(calcularArea(5, 10)); // Salida: 50

    // Si usaras 'const', sería un ReferenceError si la llamas antes de la línea de declaración/asignación
    // console.log(multiplicar(2, 3)); // ReferenceError: Cannot access 'multiplicar' before initialization
    const multiplicar = function(a, b) {
        return a * b;
    };
    ```

### Tabla Comparativa de Diferencias:

| Característica   | Declaración de Función (`function nombre() { ... }`) | Expresión de Función (`const variable = function() { ... };`) |
| :--------------- | :--------------------------------------------------- | :------------------------------------------------------------ |
| **Hoisting** | Sí (la función completa se eleva)                    | No (solo la variable se eleva, la asignación no)              |
| **Disponibilidad** | Se puede llamar antes de su definición en el código  | Solo se puede llamar después de su definición y asignación  |
| **Nombre** | Siempre tienen un nombre                             | Pueden ser anónimas (sin nombre) o nombradas                  |
| **Uso común** | Funciones independientes, globales, métodos de objeto | Funciones pasadas como argumentos, IIFEs, closures            |

### ¿Cuándo usar una u otra?

* **Declaraciones de Función:** Son ideales para definir funciones "generales" o de utilidad que esperas que estén disponibles en todo el ámbito. A menudo se utilizan para funciones que son parte de la API pública de un módulo o script.

* **Expresiones de Función:** Son muy flexibles y se utilizan en escenarios donde una función necesita ser tratada como un valor.
    * Cuando pasas funciones como argumentos a otras funciones (callbacks).
    * Cuando defines funciones dentro de otras funciones (closures).
    * Para crear *Immediately Invoked Function Expressions* (IIFEs) que se ejecutan una vez y luego se descartan.
    * Cuando quieres que una función solo esté disponible después de que ciertas condiciones se cumplan o ciertos cálculos se realicen.

Ambas formas son válidas y tienen sus propios casos de uso óptimos. Comprender sus diferencias es clave para escribir código JavaScript robusto y predecible.

## ¿Qué es la palabra clave "this" en JS?

La palabra clave **`this`** en JavaScript es uno de los conceptos más flexibles (y a menudo confusos) del lenguaje. Su valor no es estático; en cambio, el valor de `this` depende del **contexto en el que la función es invocada (llamada)**, no de dónde la función fue definida.

Piensa en `this` como una referencia al "objeto actual" en un momento dado, pero ese "objeto actual" cambia según cómo se activa la función.

### ¿Por qué es tan particular y se utiliza?

`this` es crucial para la programación orientada a objetos en JavaScript, especialmente cuando trabajas con métodos de objetos o constructores. Permite que las funciones reutilizables operen sobre los datos específicos del objeto que las invocó. Sin `this`, sería muy difícil referirse a las propiedades del propio objeto dentro de sus métodos.

### Contextos de `this` (Reglas Principales)

El valor de `this` se determina por cómo se llama la función. Vamos a ver los escenarios más comunes:

#### 1. Contexto Global (Fuera de cualquier función)

* **Regla:** En el ámbito global (fuera de cualquier función o clase), `this` se refiere al **objeto global**.
    * En navegadores, el objeto global es `window`.
    * En Node.js, el objeto global es `global` (o un objeto vacío si no estás en un módulo de Node.js).
* **Ejemplo:**
    ```
    console.log(this === window); // En un navegador: true
    this.nombre = "Global";
    console.log(window.nombre); // En un navegador: Global
    ```

#### 2. Contexto de Método (Función como método de un objeto)

* **Regla:** Cuando una función se llama como un método de un objeto, `this` se refiere al **objeto que posee el método**.
* **Ejemplo:**
    ```
    const persona = {
        nombre: "Carlos",
        saludar: function() {
            console.log(`Hola, mi nombre es ${this.nombre}`);
        },
        presentar: function() {
            console.log(this); // Aquí 'this' es el objeto 'persona'
        }
    };

    persona.saludar();   // Salida: Hola, mi nombre es Carlos (this es 'persona')
    persona.presentar(); // Salida: { nombre: 'Carlos', saludar: [Function: saludar], presentar: [Function: presentar] }
    ```

#### 3. Contexto de Constructor (Función como constructor de objetos)

* **Regla:** Cuando una función se invoca con la palabra clave `new` (como una función constructora para crear una nueva instancia), `this` se refiere a la **nueva instancia que se está creando**.
* **Ejemplo:**
    ```
    function Coche(marca, modelo) {
        this.marca = marca;   // 'this' es la nueva instancia del Coche
        this.modelo = modelo; // 'this' es la nueva instancia del Coche
        this.mostrarInfo = function() {
            console.log(`Coche: ${this.marca} ${this.modelo}`);
        };
    }
    const miCoche = new Coche("Toyota", "Corolla"); // 'new' invoca el constructor
    miCoche.mostrarInfo(); // Salida: Coche: Toyota Corolla (this en mostrarInfo es 'miCoche')
    ```

#### 4. Contexto de Función "Simple" (Función regular no como método ni constructor)

* **Regla:** En el **modo no estricto** (`strict mode` desactivado), `this` se refiere al **objeto global** (`window` en navegadores). En el **modo estricto** (`'use strict';`), `this` es `undefined`.
* **Ejemplo:**
    ```
    // Modo no estricto (comportamiento por defecto en muchos entornos de navegador antiguos)
    function funcionRegular() {
        console.log(this === window); // En un navegador: true
    }
    funcionRegular();

    // Modo estricto
    function funcionEstricta() {
        'use strict';
        console.log(this); // Salida: undefined
    }
    funcionEstricta();
    ```
    Es una buena práctica usar el modo estricto para evitar este comportamiento confuso y por otros beneficios.

#### 5. Contexto de Función de Flecha (Arrow Functions)

* **Regla:** Las funciones de flecha **no tienen su propio `this`**. Heredan el valor de `this` de su **contexto léxico** (es decir, del ámbito donde fueron definidas, no donde fueron llamadas). Esto las hace muy predecibles.
* **Ejemplo:**
    ```
    const persona = {
        nombre: "Ana",
        saludarNormal: function() {
            // 'this' aquí se refiere a 'persona' (contexto de método)
            console.log(`Normal: ${this.nombre}`);
            setTimeout(function() {
                // 'this' aquí es window (o undefined en strict mode) porque es una función regular
                console.log(`Callback Normal: ${this.nombre}`); // 'this.nombre' es undefined o global.nombre
            }, 100);
        },
        saludarFlecha: function() {
            // 'this' aquí se refiere a 'persona' (contexto de método)
            console.log(`Flecha: ${this.nombre}`);
            setTimeout(() => {
                // 'this' aquí ES 'persona' porque la función de flecha hereda el 'this' de 'saludarFlecha'
                console.log(`Callback Flecha: ${this.nombre}`); // 'this.nombre' es Ana
            }, 100);
        }
    };

    persona.saludarNormal();
    // Salida:
    // Normal: Ana
    // Callback Normal: (quizás un error o undefined)

    persona.saludarFlecha();
    // Salida:
    // Flecha: Ana
    // Callback Flecha: Ana
    ```
    Las funciones de flecha resuelven un problema común con `this` en los callbacks.

#### 6. Métodos `call()`, `apply()`, `bind()`

* **Regla:** Estos métodos permiten **establecer explícitamente el valor de `this`** para una función.
    * **`call()`:** Llama a la función con un `this` especificado y argumentos pasados individualmente.
    * **`apply()`:** Llama a la función con un `this` especificado y argumentos pasados como un *array*.
    * **`bind()`:** Devuelve una nueva función con un `this` permanentemente ligado al valor especificado.
* **Ejemplo:**
    ```
    function saludarConContexto() {
        console.log(`Hola, soy ${this.nombre || 'alguien'}.`);
    }
    const obj1 = { nombre: "María" };
    const obj2 = { nombre: "Luis" };

    saludarConContexto.call(obj1);   // Salida: Hola, soy María.
    saludarConContexto.apply(obj2);  // Salida: Hola, soy Luis.
    const saludarDeAna = saludarConContexto.bind({ nombre: "Ana" });
    saludarDeAna(); // Salida: Hola, soy Ana.
    ```

### Conclusión sobre `this`

`this` es un concepto dinámico en JavaScript que depende fuertemente de cómo se invoca una función. Entender estos diferentes contextos es crucial para depurar código, escribir métodos de objeto efectivos y utilizar funciones de flecha de manera apropiada. Cuando te encuentres con `this`, siempre pregúntate: "¿Cómo se está llamando esta función?".