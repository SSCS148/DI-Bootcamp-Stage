console.time("MyTimer");

let car1 = { name : "Audi", model : "A4" }
let car2 = { name : "Volvo", model : "XC90" }
let car3 = { name : "Ford", model : "Fusion" }
console.table([car1, car2, car3]);

console.timeEnd("MyTimer");

const person = { firstName : "Dave", surname: "Smith", age: 34 };
'firstName' in person  // returns true
'surname' in person    // returns true
'age' in person        // returns true
'gendar' in person     // returns false
console.log(person)

