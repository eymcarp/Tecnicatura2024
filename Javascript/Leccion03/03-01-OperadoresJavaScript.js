// Ejercicio para encontrar numeros pares
let parInpar = 5;
if(parInpar  % 2 == 0){
    console.log("Es un numero PAR")
}
else{
    console.log("Es un numero IMPAR")
}
//Ejercicio es mayor de edad
var edad = 18
if(edad >= 18){
    console.log("Es MAYOR de edad")
}
else{
    console.log("Es MENOR de edad")
}
// Ejercicio dentro de un rango
let dentrorango = 5;
let valMin = 0, valMax = 10;
if(dentrorango >= valMin && dentrorango <= valMax){
    console.log('Esta dentro del rango establecido')
} 
else{
    console.log('Esta fuera del rango establecito')
}

//Ejercicio si el padre puede asistri al juego de su hijo
let vacaciones = false, diaDescanso = false;
if(vacaciones||diaDescanso){
    console.log("El padre puede asistir al juego de su hijo ")
}
else{
    console.log("El padre no puede asistir al juego de su hijo ")
}

//Operador ternario
let resultado2 = 3 > 2 ? "Verdadero" : "Falso";
console.log(resultado2)
let numero = 9;
resultado2 = numero % 2 == 0 ? "Es un numero PAR" : "Es un numero IMPAR";
console.log(resultado2)

//Convertir String a Numbre
let miNumero = "10"; //Es una cadena
console.log(typeof miNumero);
let edad2 = Number(miNumero);
console.log(typeof edad2);
//Funcion isNaN
if(isNaN(edad2)){
    console.log("Esta variable no contiene solo numeros")
 }
else{
}
    if(edad2 >= 18){
        console.log("Puede votar");
    }
    else{
        console.log("Muy joven para votar")
    }

//Operador ternario
let resultado3 = edad2 >= 18 ? "Puede votar" : "Muy joven para votar";
console.log(resultado3);


