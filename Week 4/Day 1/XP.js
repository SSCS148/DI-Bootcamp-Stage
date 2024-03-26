//Exercise 1

// // Part I - Review About Arrays
// const people = ["Greg", "Mary", "Devon", "James"];

// people.shift();

// const jamesIndex = people.indexOf("James");
// if (jamesIndex !== -1) {
//     people[jamesIndex] = "Jason";
// }

// const myName = "Sacha";
// people.push(myName);

// console.log(people.indexOf("Mary"));

// const copyOfPeople = people.slice(1, -1);

// console.log(people.indexOf("Foo")); // Returns -1 because "Foo" doesn't exist in the array

// const last = people[people.length - 1];

// // Part II - Loops
// for (let person of people) {
//     console.log(person);
// }
// for (let person of people) {
//     console.log(person);
//     if (person === "Devon") {
//         break;
//     }
// }

// //Exercise 2

// const colors = ["blue", "red", "green", "yellow", "purple"];

// const suffixes = ["st", "nd", "rd", "th", "th"];
// for (let i = 0; i < colors.length; i++) {
//     let suffixIndex = i;
//     if (i >= 3 && i <= 20) {
//         suffixIndex = 3;
//     } else {
//         suffixIndex = i % 10;
//         if (suffixIndex >= suffixes.length) {
//             suffixIndex = 4;
//         }
//     }
//     console.log(`My ${i + 1}${suffixes[suffixIndex]} choice is ${colors[i]}`);
// }

//Exercise 3

// let number;
// do {
//     number = Number(prompt("Please enter a number:"));
// } while (number < 10);

// console.log("Number is greater than or equal to 10.");

//EXERCISE 4

// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }

// // Console.log the number of floors in the building
// console.log("Number of floors in the building:", building.numberOfFloors);

// // Console.log how many apartments are on floors 1 and 3
// console.log("Number of apartments on first floor:", building.numberOfAptByFloor.firstFloor);
// console.log("Number of apartments on third floor:", building.numberOfAptByFloor.thirdFloor);

// // Console.log the name of the second tenant and the number of rooms he has in his apartment
// const secondTenant = building.nameOfTenants[1];
// const roomsForSecondTenant = building.numberOfRoomsAndRent[secondTenant][0];
// console.log("Name of the second tenant:", secondTenant);
// console.log("Number of rooms he has:", roomsForSecondTenant);

// // Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, then increase Dan’s rent to 1200.
// const sarahRent = building.numberOfRoomsAndRent.sarah[1];
// const davidRent = building.numberOfRoomsAndRent.david[1];
// const danRent = building.numberOfRoomsAndRent.dan[1];

// if ((sarahRent + davidRent) > danRent) {
//     console.log("The sum of Sarah's and David's rent is bigger than Dan's rent.");
//     console.log("Increasing Dan's rent to 1200.");
//     building.numberOfRoomsAndRent.dan[1] = 1200;
// } else {
//     console.log("The sum of Sarah's and David's rent is not bigger than Dan's rent.");
// }

// console.log("Updated Dan's rent:", building.numberOfRoomsAndRent.dan[1]);

//Exercise 5
// const family = {
//     father: 'John',
//     mother: 'Jane',
//     son: 'Tom',
//     daughter: 'Emily'
//   };

//   console.log("Keys of the family object:");
//   for (let key in family) {
//     console.log(key);
//   }

//   console.log("\nValues of the family object:");
//   for (let key in family) {
//     console.log(family[key]);
//   }


//Exercise 6

// const details = {
//     my: 'name',
//     is: 'Rudolf',
//     the: 'raindeer'
//   };

//   let sentence = '';
//   for (let key in details) {
//     sentence += key === 'my' ? 'My ' : '';
//     sentence += details[key] + ' ';
//   }  
//   console.log(sentence.trim()); 

//Exercise 7

// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

// const initials = names.map(name => name[0]).sort();

// const secretSocietyName = initials.join('');

// console.log("The name of their secret society:", secretSocietyName); 