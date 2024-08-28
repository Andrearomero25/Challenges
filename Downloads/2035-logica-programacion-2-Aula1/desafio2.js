/*
Desafíos:
1. Crea una función que calcule el índice de masa corporal (IMC) de una persona a partir de su altura en metros y peso en kilogramos, que se recibirán como parámetros.
2. Crea una función que calcule el valor del factorial de un número pasado como parámetro.
3. Crea una función que convierta un valor en dólares, pasado como parámetro, y devuelva el valor equivalente en reales(moneda brasileña,si deseas puedes hacerlo con el valor del dólar en tu país). Para esto, considera la cotización del dólar igual a R$4,80.
4. Crea una función que muestre en pantalla el área y el perímetro de una sala rectangular, utilizando la altura y la anchura que se proporcionarán como parámetros.
5. Crea una función que muestre en pantalla el área y el perímetro de una sala circular, utilizando su radio que se proporcionará como parámetro. Considera Pi = 3,14.
6. Crea una función que muestre en pantalla la tabla de multiplicar de un número dado como parámetro.

*/

// 1. Crea una función que calcule el índice de masa corporal (IMC) de una persona a partir de su altura en metros y peso en kilogramos, que se recibirán como parámetros.

function calcularIMC(altura, peso) {
    const imc = peso / (altura * altura);
    return imc;
}

console.log(calcularIMC(1.75, 70)); // Debe devolver 22.99

// 2. Crea una función que calcule el valor del factorial de un número pasado como parámetro.

function calcularFactorial(numero) {
    if (numero === 0 || numero === 1) {
        return 1;
    } else {
        let factorial = 1;
        for (let i = 2; i <= numero; i++) {
            factorial *= i;
        }
        return factorial;
    }
}

console.log(calcularFactorial(5)); // Debe devolver 120


// 3. Crea una función que convierta un valor en dólares, pasado como parámetro, y devuelva el valor equivalente en reales(moneda brasileña, si deseas puedes hacerlo con el valor del dólar en tu país). Para esto, considera la cotización del dólar igual a R$4,80.

function convertirDolaresReales(dolares) {
    const reales = dolares * 4.80;
    return reales;
}

console.log(convertirDolaresReales(100)); // Debe devolver 480

// 4. Crea una función que muestre en pantalla el área y el perímetro de una sala rectangular, utilizando la altura y la anchura que se proporcionarán como parámetros.

function calcularAreaPerimetroRectangulo(altura, anchura) {
    const area = altura * anchura;
    const perimetro = 2 * (altura + anchura);
    return { area, perimetro };
}

const { area, perimetro } = calcularAreaPerimetroRectangulo(5, 10);

console.log(`Área: ${area}, Perímetro: ${perimetro}`); // Debe devolver área: 50, Perímetro: 30

// 5. Crea una función que muestre en pantalla el área y el perímetro de una sala circular, utilizando su radio que se proporcionará como parámetro. Considera Pi = 3,14.

function calcularAreaPerimetroCirculo(radio) {
    const area1 = Math.PI * Math.pow(radio, 2);
    const perimetro1 = 2 * Math.PI * radio;
    return { area1, perimetro1 };
}

const { area1, perimetro1 } = calcularAreaPerimetroCirculo(5);

console.log(`Área: ${area1}, Perímetro: ${perimetro1}`); // Debe devolver área: 78.53981633974483, Perímetro: 31.41592653589793

// 6. Crea una función que muestre en pantalla la tabla de multiplicar de un número dado como parámetro.

function mostrarTablaMultiplicar(numero) {
    for (let i = 1; i <= 10; i++) {
        console.log(`${numero} x ${i} = ${numero * i}`);
    }
}

// Pruebas

mostrarTablaMultiplicar(5); // Debe imprimir la tabla de multiplicar de 5 hasta el 10

// Nota: La función `mostrarTablaMultiplicar` no está implementada en este código, pero puedes usarla para mostrar la tabla de multiplicar de un número que desees.

// 7. Crea una función que calcule la raíz cuadrada de un número y devuelva el resultado redondeado a dos decimales.

function calcularRaizCuadrada(numero) {
    const raiz = Math.sqrt(numero);
    return Number(raiz.toFixed(2));
}

console.log(calcularRaizCuadrada(25)); // Debe devolver 5


