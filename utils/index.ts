// utils.js
export const invertirCadena = (cadena) => {
    console.log(cadena);
    let newString = '';
    for (let i = cadena.length - 1; i >= 0; i--) {
      //console.log(i, cadena[i]);
      newString += cadena[i];
      
    }
    console.log("New String: ", newString);
  };

  export const sumArray = (arreglo) => {
    let sum = 0
    for(let i = 0; i < arreglo.length; i++){
        console.log(i)
        sum += arreglo[i]
    }
    return sum
  }

export const deleteDuplicate = (array) => {
    if (!Array.isArray(array)) {
        throw new Error("Input must be an array");
    }
    const newArray = []; // Arreglo para almacenar elementos únicos
    const temporal = {}; // Objeto para rastrear elementos ya vistos

    for (let i = 0; i < array.length; i++) {
        const elemento = array[i];
        console.log(`Elemento(${i}): `, elemento)
        if(!temporal[elemento]){
            temporal[elemento] = true
            newArray.push(elemento)
        }else{
            console.log("Duplicated: ", elemento)
        }
    }

    return newArray;
};