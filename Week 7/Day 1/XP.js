// Exercise 1 :

// function compareToTen(num) {
//     return new Promise((resolve, reject) => {
//       if (num <= 10) {
//         resolve(`${num} is less than or equal to 10`);
//       } else {
//         reject(`${num} is greater than 10`);
//       }
//     });
//   }
  
//    Test case where the promise should reject
//   compareToTen(15)
//     .then(result => console.log(result))
//     .catch(error => console.log(error));
  
//    Test case where the promise should resolve
//   compareToTen(8)
//     .then(result => console.log(result))
//     .catch(error => console.log(error));
  
// Exercise 2 : 

// const promise = new Promise((resolve, reject) => {
//     setTimeout(() => {
//       resolve("success");
//     }, 4000);
//   });
  
//   promise.then(result => {
//     console.log(result); // Output: success
//   });

// // Exercise 3 :

// const promise1 = Promise.resolve(3);
// promise1.then(value => {
//   console.log(value); // Output: 3
// });

// const promise2 = Promise.reject("Boo!");
// promise2.catch(error => {
//   console.log(error); // Output: Boo!
// });

