// // 🌟 Exercise 1: Find The Numbers Divisible By 23

// // Function to display numbers divisible by 23
// function displayNumbersDivisible(divisor = 23) {
//     let sum = 0;
//     for (let i = 0; i <= 500; i++) {
//         if (i % divisor === 0) {
//             console.log(i);
//             sum += i;
//         }
//     }
//     console.log('Sum:', sum);
// }

// // Example usage:
// displayNumbersDivisible(); // Display numbers divisible by 23 and their sum

// 🌟 Exercise 2: Shopping List

// const stock = { 
//     "banana": 6, 
//     "apple": 0,
//     "pear": 12,
//     "orange": 32,
//     "blueberry":1
// };  

// const prices = {    
//     "banana": 4, 
//     "apple": 2, 
//     "pear": 1,
//     "orange": 1.5,
//     "blueberry":10
// };

// // Shopping list array
// const shoppingList = ["banana", "orange", "apple"];

// // Function to calculate total bill
// function myBill() {
//     let total = 0;
//     for (let item of shoppingList) {
//         if (item in stock && stock[item] > 0) {
//             total += prices[item];
//             stock[item]--;
//         }
//     }
//     return total;
// }

// // Example usage:
// console.log("Total Bill:", myBill());

// 🌟 Exercise 3: What’s In My Wallet ?

// function changeEnough(itemPrice, amountOfChange) {
//     const denominations = [0.25, 0.10, 0.05, 0.01];
//     let totalChange = 0;
//     for (let i = 0; i < amountOfChange.length; i++) {
//         totalChange += amountOfChange[i] * denominations[i];
//     }
//     return totalChange >= itemPrice;
// }

// // Example usage:
// console.log(changeEnough(4.25, [25, 20, 5, 0])); // Should return true
// console.log(changeEnough(14.11, [2, 100, 0, 0])); // Should return false
// console.log(changeEnough(0.75, [0, 0, 20, 5])); // Should return true


// 🌟 Exercise 4: Vacations Costs

// Function to calculate hotel cost
// function hotelCost() {
//     let numNights = parseInt(prompt("Enter the number of nights you would like to stay:"));
//     while (isNaN(numNights)) {
//         numNights = parseInt(prompt("Invalid input! Please enter a number:"));
//     }
//     return numNights * 140;
// }

// // Function to calculate plane ride cost
// function planeRideCost() {
//     let destination = prompt("Enter your destination (London, Paris, or others):").toLowerCase();
//     let price;
//     switch (destination) {
//         case "london":
//             price = 183;
//             break;
//         case "paris":
//             price = 220;
//             break;
//         default:
//             price = 300;
//             break;
//     }
//     return price;
// }

// // Function to calculate rental car cost
// function rentalCarCost() {
//     let numDays = parseInt(prompt("Enter the number of days you would like to rent the car:"));
//     while (isNaN(numDays)) {
//         numDays = parseInt(prompt("Invalid input! Please enter a number:"));
//     }
//     let totalCost = numDays * 40;
//     if (numDays > 10) {
//         totalCost *= 0.95; // Apply 5% discount
//     }
//     return totalCost;
// }

// // Function to calculate total vacation cost
// function totalVacationCost() {
//     const hotel = hotelCost();
//     const plane = planeRideCost();
//     const rentalCar = rentalCarCost();
//     const totalCost = hotel + plane + rentalCar;
//     console.log(`The hotel cost: $${hotel}, the plane tickets cost: $${plane}, the car rental cost: $${rentalCar}.`);
//     console.log(`Total vacation cost: $${totalCost}`);
// }

// // Example usage:
// totalVacationCost();


// 🌟 Exercise 6: Change The Navbar

// Change the value of the id attribute from navBar to socialNetworkNavigation
// const navBar = document.getElementById('navBar');
// navBar.setAttribute('id', 'socialNetworkNavigation');

// // Add a new <li> to the <ul>
// const newListItem = document.createElement('li');
// newListItem.innerHTML = '<a href="#">Logout</a>';
// navBar.firstElementChild.appendChild(newListItem);

// // Retrieve the first and last <li> elements and display their text
// const firstLi = navBar.firstElementChild.firstElementChild;
// const lastLi = navBar.firstElementChild.lastElementChild;
// console.log(firstLi.textContent, lastLi.textContent);



