// 🌟 Exercise 1 : Location
// Output: I am John Doe from Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

// 🌟 Exercise 2: Display Student Info
// function displayStudentInfo(objUser){
//     const { first, last } = objUser;
//     return `Your full name is ${first} ${last}`;
// }
// console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));

// 🌟 Exercise 3: User & Id
// const users = { user1: 18273, user2: 92833, user3: 90315 };
// Convert object to array
// const usersArray = Object.entries(users);
// console.log(usersArray);
// Multiply the user's ID by 2
// const updatedUsersArray = usersArray.map(([user, id]) => [user, id * 2]);
// console.log(updatedUsersArray);

// Exercise 4 : Person Class
// Output: 'object' because 'member' is an instance of the Person class.

// 🌟 Exercise 5 : Dog Class
// Option 2: Correct constructor for extending the Dog class.

// 🌟 Exercise 6 : Challenges
// Evaluate these (ie True or False)
// [2] === [2] -> False (Arrays are reference types and each array instance is distinct)
// {} === {} -> False (Objects are reference types and each object instance is distinct)

// Value of property number:
// const object1 = { number: 5 };
// const object2 = object1; 
// const object3 = object2; 
// const object4 = { number: 5};

// object1.number = 4;
// console.log(object2.number); // Output: 4 (object2 points to the same object as object1)
// console.log(object3.number); // Output: 4 (object3 also points to the same object as object1)
// console.log(object4.number); // Output: 5 (object4 is a new object with its own property)

// Class Animal
// class Animal {
//     constructor(name, type, color) {
//         this.name = name;
//         this.type = type;
//         this.color = color;
//     }
// }

// // Class Mammal
// class Mammal extends Animal {
//     sound(sound) {
//         return `Moooo I'm a ${this.type}, named ${this.name} and I'm ${this.color}.\n${sound}`;
//     }
// }

// // Create a farmerCow object
// const farmerCow = new Mammal('Lily', 'cow', 'brown and white');
// console.log(farmerCow.sound('Moooo'));
