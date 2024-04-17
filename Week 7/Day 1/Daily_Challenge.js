// function makeAllCaps(words) {
//     return new Promise((resolve, reject) => {
//       if (words.every(word => typeof word === 'string')) {
//         const uppercasedWords = words.map(word => word.toUpperCase());
//         resolve(uppercasedWords);
//       } else {
//         reject("Array contains non-string elements");
//       }
//     });
//   }
  
//   function sortWords(words) {
//     return new Promise((resolve, reject) => {
//       if (words.length > 4) {
//         const sortedWords = words.sort();
//         resolve(sortedWords);
//       } else {
//         reject("Array length is not bigger than 4");
//       }
//     });
//   }
  
//   // Test cases
//   makeAllCaps([1, "pear", "banana"])
//     .then((arr) => sortWords(arr))
//     .then((result) => console.log(result))
//     .catch(error => console.log(error));
  
//   makeAllCaps(["apple", "pear", "banana"])
//     .then((arr) => sortWords(arr))
//     .then((result) => console.log(result))
//     .catch(error => console.log(error));
  
//   makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
//     .then((arr) => sortWords(arr))
//     .then((result) => console.log(result))
//     .catch(error => console.log(error));
  