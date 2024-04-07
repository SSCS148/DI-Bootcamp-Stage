// // Exercise 1
// // #1
// function funcOne() {
//     let a = 5;
//     if (a > 1) {
//         a = 3;
//     }
//     alert(`inside the funcOne function ${a}`);
// }
// // Prediction for #1: The value of 'a' inside funcOne will be 3 because it's reassigned to 3 inside the if block.

// // #1.1
// // If the variable is declared with const instead of let:
// // Since 'a' is reassigned inside the function, using const will result in an error because const variables cannot be reassigned.

// //#2
// let a = 0;
// function funcTwo() {
//     a = 5;
// }

// function funcThree() {
//     alert(`inside the funcThree function ${a}`);
// }

// // #2.1
// // Prediction for #2.1: funcThree will alert "inside the funcThree function 0" and then "inside the funcThree function 5" because 'a' is modified by funcTwo.

// // #2.2
// // If 'a' is declared with const instead of let:
// // Using const will result in an error because 'a' is being reassigned.

// //#3
// function funcFour() {
//     window.a = "hello";
// }

// function funcFive() {
//     alert(`inside the funcFive function ${a}`);
// }

// // #3.1
// // Prediction for #3.1: funcFive will alert "inside the funcFive function hello" because 'a' is assigned to the global object window by funcFour.

// //#4
// let a = 1;
// function funcSix() {
//     let a = "test";
//     alert(`inside the funcSix function ${a}`);
// }

// // #4.1
// // Prediction for #4.1: funcSix will alert "inside the funcSix function test" because 'a' is locally scoped inside funcSix.

// // #4.2
// // If 'a' is declared with const instead of let:
// // Using const will not affect the behavior because 'a' is already being locally scoped within funcSix.

// //#5
// let a = 2;
// if (true) {
//     let a = 5;
//     alert(`in the if block ${a}`);
// }
// alert(`outside of the if block ${a}`);

// // #5.1
// // Prediction for #5.1: It will alert "in the if block 5" and then "outside of the if block 2" because the inner 'a' is scoped to the if block and the outer 'a' is scoped globally.

// // #5.2
// // If 'a' is declared with const instead of let:
// // Using const will not affect the behavior as the scoping remains the same.


// //Exercise 2 : 

// const winBattle = () => true; // Converted to an arrow function

// const experiencePoints = winBattle() ? 10 : 1; // Using ternary operator to assign value based on winBattle()
// console.log(experiencePoints);


// //Exercise 3 : 

// const isString = (value) => typeof value === 'string'; // Arrow function to check if value is a string

// console.log(isString('hello')); // Output: true
// console.log(isString([1, 2, 4, 0])); // Output: false

// // Exercise 4 :

// const sum = (a, b) => a + b; // Arrow function to return sum of two numbers


// //Exercise 5 : 

// // Function declaration
// function kgToGramsDeclaration(kg) {
//     return kg * 1000;
// }
// // Invoking the function declaration
// console.log(kgToGramsDeclaration(2));

// // Function expression
// const kgToGramsExpression = function(kg) {
//     return kg * 1000;
// };
// // Invoking the function expression
// console.log(kgToGramsExpression(2));

// // Difference between function declaration and expression:
// // Function declaration is hoisted, meaning it can be called before it's defined in the code, whereas function expressions are not hoisted and must be defined before they are called.

// // One line arrow function
// const kgToGramsArrow = kg => kg * 1000;
// // Invoking the one line arrow function
// console.log(kgToGramsArrow(2));

// Exercise 6 : 
// <!-- HTML -->
// <div id="fortune"></div>
// // Self-invoking function
// (function(numberOfChildren, partnerName, geographicLocation, jobTitle) {
//     const sentence = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnerName} with ${numberOfChildren} kids.`;
//     document.getElementById('fortune').innerText = sentence;
// })(3, 'Alice', 'New York', 'Software Engineer');

// Exercise 7: 
// <!-- HTML -->
// <nav id="navbar"></nav>
// // Self-invoking function
// (function(userName) {
//     const navbar = document.getElementById('navbar');
//     const div = document.createElement('div');
//     div.innerText = `Welcome, ${userName}`;
//     // Assume profilePictureUrl is the URL of the user's profile picture
//     div.innerHTML += `<img src="${profilePictureUrl}" alt="Profile Picture">`;
//     navbar.appendChild(div);
// })('John');

// Exercise 8 : 
// // Part I
// function makeJuice(size) {
//     function addIngredients(ingredient1, ingredient2, ingredient3) {
//         console.log(`The client wants a ${size} juice, containing ${ingredient1}, ${ingredient2}, ${ingredient3}`);
//     }
//     addIngredients('apple', 'banana', 'orange');
// }
// makeJuice('small');

// // Part II
// function makeJuice(size) {
//     const ingredients = [];

//     function addIngredients(ingredient1, ingredient2, ingredient3) {
//         ingredients.push(ingredient1, ingredient2, ingredient3);
//     }

//     function displayJuice() {
//         console.log(`The client wants a ${size} juice, containing ${ingredients.join(', ')}`);
//     }

//     addIngredients('apple', 'banana', 'orange');
//     addIngredients('strawberry', 'kiwi', 'pineapple');
//     displayJuice();
// }

// makeJuice('medium');
