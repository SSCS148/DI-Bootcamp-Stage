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

// function helloWorld()
// {
//     document.write("Hello ")
//     document.write("World !")
// }

// helloWorld();

// function userInfo (username, userAge) {
//     console.log("My name is " + username + ", my age is " + userAge);
// }
// userInfo();


// function calculus (user,name) {
//     console.log(user+name);
// }

// calculus('The age of sahca is ',12);

// function userInfo(userName, userAge) {
//     console.log("My name is " + userName + ", my age is "  + userAge);
// }

// userInfo("Sarah", 22); //My name is Sarah, my age is 22
// userInfo("Ben", 40); //My name is Ben, my age is 40

// function calculusSecond (a,b,c) {
//     console.log(a+b+c);
// }

// calculusSecond(2,3,1);//6


// function userInfo(userName, userAge=20) {
//     console.log("My name is " + userName + ", my age is " + userAge);
// }

// userInfo("Sarah"); //My name is Sarah, my age is 20
// userInfo("Ben", 40); //My name is Ben, my age is 40

// let eyeColor = "blue"; //local variable 
// function userMoreInfo (userName, userAge) {
//     console.log("My name is " + userName + ", my age is "  + userAge + ", I have " + eyeColor + " eyes");
// }

// userMoreInfo("Sarah", 22); //My name is Sarah, my age is 22, I have blue eyes


// let eyeColor = "blue";

// function userMoreInfo (userName, userAge) {
//     console.log("My name is " + userName + ", my age is " + userAge + ", I have " + eyeColor + " eyes");
// }
// userMoreInfo("Sarah", 22); 
// console.log(eyeColor); 

// function favoriteColor () {
//     console.log("My favorite color is " + eyeColor);
// }
// favoriteColor();

// function calcParentsAge(myAge){
//     var momAge = myAge*2;
//     var dadAge = momAge*1.2;

//     console.log(momAge,dadAge)
// } 

// calcParentsAge(25);

function userInfo(userName, userAge) {
    let result = "My name is " + userName + ", my age is " + userAge;
    return result;
}

let girlInfo = userInfo("Sarah", 22);
console.log(girlInfo); 