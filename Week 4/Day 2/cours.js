// console.time("MyTimer");

// let car1 = { name : "Audi", model : "A4" }
// let car2 = { name : "Volvo", model : "XC90" }
// let car3 = { name : "Ford", model : "Fusion" }
// console.table([car1, car2, car3]);

// console.timeEnd("MyTimer");

// const person = { firstName : "Dave", surname: "Smith", age: 34 };
// 'firstName' in person  // returns true
// 'surname' in person    // returns true
// 'age' in person        // returns true
// 'gendar' in person     // returns false
// console.log(person)


// let name = "Sarah";
// var greeting = "Hello";
// console.log(greeting + " " + name);
// // Hello Sarah

// const age = 1;
// console.log("You're " + age);
// // You're 1

// function doSomething() {
//     var someVar = "Something";
// }

// console.log(doSomething)

// function listFruits () {
//     if(true) {
//         const fruit1 = "orange"; //it exists in block scope
//         let fruit2 = "avocado"; //it exists in block scope
//         var fruit3 = "banana"; // it exists in function scope
//     }

//     // console.log(fruit1);
//     // console.log(fruit2);
//     console.log(fruit3);
// }

// listFruits();

// var name = "Sarah";
// const greeting = "Hello ";
// console.log(greeting + name);

// // greeting = "Hi";
// name = "Patience";
// console.log(greeting + name)

// let age = 1;
// console.log("You're " + age);

// age = 5; // we reset the age but no error
// console.log("You're " + age);

// function helloWorld(){
//   console.log("Hello World");
// }

// helloWorld();


function func() {
  // x is known here but not defined.
  console.log('value of x here: ', x)
  {
    var x = 10;
    x = x + 5;
  }
  // x is still known here and has a value.
  console.log('value of x after for block: ', x)
}
// x is NOT known here.
func()