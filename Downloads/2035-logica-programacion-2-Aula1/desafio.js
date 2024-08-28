/*
Desafíos:
1. Crear una función que muestre "¡Hola, mundo!" en la consola.
2. Crear una función que reciba un nombre como parámetro y muestre "¡Hola, [nombre]!" en la consola.
3. Crear una función que reciba un número como parámetro y devuelva el doble de ese número.
4. Crear una función que reciba tres números como parámetros y devuelva su promedio.
5. Crear una función que reciba dos números como parámetros y devuelva el mayor de ellos.
6. Crear una función que reciba un número como parámetro y devuelva el resultado de multiplicar ese número por sí mismo.
*/

// 1. Crear una función que muestre "¡Hola, mundo!" en la consola.
function holaMundo() {
    console.log("¡Hola, mundo!");
}

holaMundo(); // Llamar a la función para ejecutarla

// 2. Crear una función que reciba un nombre como parámetro y mueste "¡Hola, [nombre]!" en la consola.
function holaNombre(nombre) {
    console.log(`¡Hola, ${nombre}!`);
}

holaNombre("Juan"); // Llamar a la función para ejecutarla

// 3. Crear una función que reciba un número como parámetro y devuelva el doble de ese número.
function numeroDoble(numeroDoble) {
    return numeroDoble * 2;
}
// Llamar a la función para ejecutarla
console.log(numeroDoble(5)); // Devuelve 10

// 4. Crear una función que reciba tres números como parámetros y devuelva su promedio.
function promedioNumeros(num1, num2, num3) {
    return (num1 + num2 + num3) / 3;
}
// Llamar a la función para ejecutarla
console.log(promedioNumeros(10, 20, 30)); // Devuelve 20

// 5. Crear una función que reciba dos números como parámetros y devuelva el mayor de ellos.

function mayorNumero(num1, num2) {
    if (num1 > num2) {
        return num1;
    }
    return num2;
}
// Llamar a la función para ejecutarla
console.log(mayorNumero(10, 20)); // Devuelve 20

// 6. Crear una función que reciba un número como parámetro y devuelva el resultado de multiplicar ese número por sí mismo.
function numeroAlCuadrado(numero) {
    return numero * numero;
}
// Llamar a la función para ejecutarla
console.log(numeroAlCuadrado(5)); // Devuelve 25