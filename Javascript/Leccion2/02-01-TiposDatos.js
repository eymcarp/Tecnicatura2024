// Tipos de datos en JavaScript
/*
La sintaxis es muy similar a JAVA
*/
var nombre = "Mauro";
console.log(typeof nombre);
nombre = 7;
console.log(typeof nombre);
nombre = 12.7;
console.log(typeof nombre)

var numero = 3000;
console.log(numero);

var objeto = {
    nombre : "Mauro",
    apellido: "Ulloa",
    telefono: "2613434343"
}

console.log(objeto);

//Tipo de dato boolean
var bandera = true;
console.log(typeof bandera);

//Tipo de dato funcion (Nos permite reutilizar lineas de codigo)
function miFuncion(){}
console.log(typeof miFuncion);

//Tipo de dato symbol
var simbolo = Symbol("Mi simbolo");
console.log(typeof simbolo);

//Tipo de dato clase
class Persona{
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
    }
}
console.log(typeof Persona);

//Tipo de dato undefined
var x;
console.log(typeof x);

x = undefined;
console.log(typeof x);

//null : significa ausencia de valor
var y = null; //null no es un tipo de dato, pero su origen es object
console.log(typeof y);

//Tipo de dato array y empty string
var autos = ['Citroen','Audi','BMW','Ford'] // ARREGLO
console.log(autos);
console.log(typeof autos);

var z = '';// EMPTY STRING CADENA VACIA
console.log(z);
console.log(typeof z);






