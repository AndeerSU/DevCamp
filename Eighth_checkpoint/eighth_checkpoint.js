const miLista = ["velma", "exploradora", "jane", "john", "harry"];

console.log("--- Bucle 'for' ---");
for (let i = 0; i < miLista.length; i++) {
  console.log(miLista[i]);
}

console.log("\n--- Bucle 'while' ---");
let contador = 0;
while (contador < miLista.length) {
  console.log(miLista[contador]);
  contador++; // Se incrementa el contador en cada iteración
}

console.log("\n--- Función de flecha ---");
const saludar = () => "Hola mundo";

console.log(saludar());