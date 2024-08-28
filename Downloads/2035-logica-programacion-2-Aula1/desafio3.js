/*
Desafíos
1. Crea una lista vacía llamada "listaGenerica".
2. Crea una lista de lenguajes de programación llamada "lenguagesDeProgramacion con los siguientes elementos: 'JavaScript', 'C', 'C++', 'Kotlin' y 'Python'.
3. Agrega a la lista "lenguagesDeProgramacion los siguientes elementos: 'Java', 'Ruby' y 'GoLang'.
4. Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion.
5. Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion en orden inverso.
6. Crea una función que calcule el promedio de los elementos en una lista de números.
7. Crea una función que muestre en la consola el número más grande y el número más pequeño en una lista.
8. Crea una función que devuelva la suma de todos los elementos en una lista.
9. Crea una función que devuelva la posición en la lista donde se encuentra un elemento pasado como parámetro, o -1 si no existe en la lista.
10. Crea una función que reciba dos listas de números del mismo tamaño y devuelva una nueva lista con la suma de los elementos uno a uno.
11. Crea una función que reciba una lista de números y devuelva una nueva lista con el cuadrado de cada número.

*/

// 1. Crea una lista vacía llamada "listaGenerica".

let listaGenerica = [];

// 2. Crea una lista de lenguajes de programación llamada "lenguagesDeProgramacion".

let lenguagesDeProgramacion = ['JavaScript', 'C', 'C++', 'Kotlin', 'Python'];

// 3. Agrega a la lista "lenguagesDeProgramacion" los siguientes elementos: 'Java', 'Ruby' y 'GoLang'.

lenguagesDeProgramacion.push('Java', 'Ruby', 'GoLang');

// 4. Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion".

function mostrarLenguajesDeProgramacion() {
    for (let i = 0; i < lenguagesDeProgramacion.length; i++) {
        console.log(lenguagesDeProgramacion[i]);
    }
}

mostrarLenguajesDeProgramacion();

// 5. Crea una función que muestre en la consola todos los elementos de la lista "lenguagesDeProgramacion" en orden inverso.

function mostrarLenguajesDeProgramacionEnOrdenInverso() {
    for (let i = lenguagesDeProgramacion.length - 1; i >= 0; i--) {
        console.log(lenguagesDeProgramacion[i]);
    }
}

mostrarLenguajesDeProgramacionEnOrdenInverso();

// 6. Crea una función que calcule el promedio de los elementos en una lista de números.

function calcularPromedio(numeros) {
    let suma = 0;
    for (let i = 0; i < numeros.length; i++) {
        suma += numeros[i];
    }
    return suma / numeros.length;
}

console.log(calcularPromedio([1, 2, 3, 4, 5])) // Deberia arrojar 3

// 7. Crea una función que muestre en la consola el número más grande y el número más pequeño en una lista.

function obtenerMaximoMinimo(numeros) {
    let maximo = numeros[0];
    let minimo = numeros[0];
    for (let i = 1; i < numeros.length; i++) {
        if (numeros[i] > maximo) {
            maximo = numeros[i];
        }
        if (numeros[i] < minimo) {
            minimo = numeros[i];
        }
    }
    return { maximo, minimo };
}

console.log(obtenerMaximoMinimo([1, 2, 3, 4, 5])) // Deberia arrojar { maximo: 5, minimo: 1 }

// 8. Crea una función que devuelva la suma de todos los elementos en una lista.

function sumarElementos(numeros) {
    let suma = 0;
    for(let i = 0; i < numeros.length; i++) {
        suma += numeros[i];
    }
    return suma;
}

console.log(sumarElementos([1, 2, 3, 4, 5])) // Deberia arrojar 15


//9. Crea una función que devuelva la posición en la lista donde se encuentra un elemento pasado como parámetro, o -1 si no existe en la lista.

function buscarElemento(numeros, elemento) {
    for(let i = 0; i < numeros.length; i++) {
        if (numeros[i] === elemento){
            return i;
        }
    }
    return -1;
}

console.log(buscarElemento([1, 2, 3, 4, 5], 3)) // Deberia arrojar 2

// 10. Crea una función que reciba dos listas de números del mismo tamaño y devuelva una nueva lista con la suma de los elementos uno a uno.

function sumarListas(lista1, lista2) {
    if (lista1.length !== lista2.length) {
        throw new Error("Las listas deben tener el mismo tamaño");
    }
    let sumarListas = [];
    for(let i =0; i < lista1.length; i++) {
        sumarListas.push(lista1[i] + lista2[i]);
    }
    return sumarListas;
}

console.log(sumarListas([1, 2, 3], [4, 5, 6])) // Deberia arrojar [5, 7, 9]

// 11. Crea una función que reciba una lista de números y devuelva una nueva lista con el cuadrado de cada número.

function calcularCuadrados(numeros) {
    let cuadrados = [];
    for(let i =0; i < numeros.length; i++) {
        cuadrados.push(numeros[i] * numeros[i]); 
    }
    return cuadrados;
}

console.log(calcularCuadrados([1, 2, 3])) // Deberia arrojar [1, 4, 9]