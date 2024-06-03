var nombre = 'Jose';
var apellido = 'Montes';
var nombreCompleto = nombre+''+apellido; // Primera Concatenacion
console.log(nombreCompleto);
var nombreCompleto2 = 'Ariel'+' '+'Bentancud'; // Segunda concatenacion
console.log(nombreCompleto2);
var juntos = nombre + 219; //Lee de izq a derec siguiendo la cadena lee el numero como string
console.log(juntos);
juntos = nombre + (78 + 17);
console.log(juntos);
juntos = 78 + 17 + nombre;
console.log(juntos);

nombre += apellido;// Tercera concatenacion usando el operador simplifcado
console.log(nombre);

// Hoy ya no se usa var, se utiliza let y const
let nombre2 = "Pedro";
console.log(nombre2)

const apellido2 = "Gimenez";
//apellido2 = "Peres" una const no puede ser modificada
console.log(apellido2)


