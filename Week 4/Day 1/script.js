// let name = value
// let name2;
// name2 = 5

// let str = 'test'
// let num = 5
// let bool = 4 > 5
// let void = null
// let un = undefined
// let arr : []
// let obj = {}

// let greeting = 'hello'
// let name3 = 'Nadav'
// let fullGreeting = greeting + name3
// console.log(fullGreeting)
// console.log(greeting,name3);
// let lonString = "LOremloremloremloremloremlor\
// loremloremloremloRemloremloremloremlorem\
// loremloremloremloremloremloremloremlorem";

// console.log(lonString.length);
// console.log(lonString.split(''));
// console.log(lonString.substring(0,20));
// let small = lonString.toLowerCase()

// let compare = 13 == 12

// let str = "Hello Everyone, please say hello to the class";
// let posUppercaseHello = str.indexOf("Hello"); // case sensitive
// let posLowercaseHello = str.indexOf("hello");
// console.log(posUppercaseHello) // 0
// console.log(posLowercaseHello) // 27

// let secondstr = "hello Everyone, please say hello to the class";
// let secondStrPosHello = secondstr.indexOf("hello"); 
// console.log(secondStrPosHello) // 0

// 1. Create these variables and give them values:

// addressNumber
// addressStreet
// country
// 2. Write a variable named globalAddress, and concatenate inside, the variables:

// addressNumber
// addressStreet
// country
// In order to create a sentence
// 3. Display globalAddress Example: globalAddress should display « I live in BenYehuda 5, in Israel »

// let addressNumber = 202
// let addressStreet = 'Yaffo'
// let country = 'Israel'

//  let globalAddress = `I live in ${addressStreet} ${addressNumber}, in ${country}`
// console.log(globalAddress)
// 1. Store your birth year in a variable.

// 2. Store a future year in a variable.

// 3. Calculate your possible ages for that year based on the stored values.

// 4. Display : "I will be NN in YYYY", substituting the values.

// let birth = 1999
// let future = 2032
// let calAge = `I will be ${future - birth} in ${future}`
// console.log(calAge)

// alert ('hello bro')
// confirm('hi')
// prompt('are you ok' )
// let isBoss = confirm("Are you the boss?");
// alert(isBoss); // true if OK is pressed

// let sampleArray = [
//     [1, 2, 5],
//     [7, 6, 10, 11, 12],
//     [3]
// ]
// console.log(sampleArray[2][0])
// sampleArray[2][0] = 0
// console.log(sampleArray)
// console.log(sampleArray[2].length)

// let colors = ["blue", "yellow", "green" ]; 
// colors.splice(0, 1, 45, 23); 
// console.log(colors) 

// let age = 2

// if (age > 18) {
//     console.log("We can go to a pub together !!")
// } else {
//     console.log("Sorry...You have to stay at home tonight")
// }

// let age = 20

// if (age === 18) {
//     console.log("It's your birthday !!") 
// } else if (age > 18) {
//     console.log("We can go to a pub together !!")
// } else {
//     console.log("Sorry...You have to stay at home tonight")
// }


// let age = prompt("How old are you ?")
// if (age < 18){
//     console.log("Sorry, you are too young to drive this car. Powering off")
// }else if (age == 18){
//     console.log("Congratulations on your first year of driving. Enjoy the ride!")
// }else if (age >= 18){
//     console.log("Powering On. Enjoy the ride!")
// }

// let fruit = prompt("Please enter your fruit");

// switch (fruit) {
//   case 'Oranges':
//     console.log('Oranges are $0.59 a pound.');
//     break;
//   case 'Mangoes':
//   case 'Papayas':
//     console.log('Mangoes and papayas are $2.79 a pound.');
//     // expected output: "Mangoes and papayas are $2.79 a pound."
//     break;
//   default:
//     console.log('Sorry, we are out of ' + fruit + '.');
// }

// let a = 2 + 2;

// switch (a) {
//   case 3:
//     alert( 'Too small' );
//     break;
//   case 4:
//     alert( 'Exactly!' );
//     break;
//   case 5:
//     alert( 'Too large' );
//     break;
//   default:
//     alert( "I don't know such values" );
// }


// let a = 2 + 2;

// switch (a) {
//   case 4:
//     alert('Right!');
//     break;

//   case 3: // (*) grouped two cases
//   case 5:
//     alert('Wrong!');
//     alert("Why don't you take a math class?");
//     break;

//   default:
//     alert('The result is strange. Really.');
// }

// let age = [13,1,6,56,45,30,98]
// for (ages in age){
//     console.log(age[ages])
// }

// for (let i = 0; i <= 11; i++) {
//     console.log("the current number is " + i)
// }
// let arr = [1,4,7,10,98]
// for (let i=0; i<arr.length; i++) {
//     console.log(arr[i])
// }

// for (i=0; i<=15; i++){
//     if (i%2==0){
//         console.log(" This number " + i +" is even")
//     } else {
//         console.log(" This number " + i +" is odd")
//         }
    
// }

// let person = {fname:"John", lname:"Doe", age:25};
// for (let x in person) {
//   console.log(x) //fname lname age
//   console.log(person[x]) // John Doe 25
// }

// let car = {
//     owner: 'Sacha',
//     year: 2024,
//     model: '4x4',
//     options: {
//         key: 'chauffage'
//     }
// }
// for (const key in car){
//     let value = car[key]
//     console.log(car[key])
// }

// let n = -1;
// while (n <= 15) {
//     n++;
//     if (n%2==0){
//         console.log(n+" EVEN")
//     } else{
//         console.log(n+" ODD")
//     }
// }



// let n = 16;
// do {
//     n++;
//     if (n%2==0){
//         console.log(n+" EVEN")
//     } else{
//         console.log(n+" ODD")
//     }
// } while (n < 15)


// let i = 0;
// do {
//     console.log("The number is " + i)
//     i++;
// }
// while (i < 10);


// for (let i = 0; i < 10; i++) {
//     if (i === 3) { 
//         continue;
//     }
//     console.log("The number is " + i); // 0 1 2
// }

let names= ["john", "sarah", 23, "Rudolf",34]
if (names == []){
    while
}