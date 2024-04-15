// function areAnagrams(str1, str2) {
//     // Remove non-alphanumeric characters and convert to lowercase
//     const cleanStr1 = str1.replace(/[^A-Za-z0-9]/g, '').toLowerCase();
//     const cleanStr2 = str2.replace(/[^A-Za-z0-9]/g, '').toLowerCase();

//     // Check if the lengths of the cleaned strings are different
//     if (cleanStr1.length !== cleanStr2.length) {
//         return false;
//     }

//     // Sort the characters in both strings and compare them
//     const sortedStr1 = cleanStr1.split('').sort().join('');
//     const sortedStr2 = cleanStr2.split('').sort().join('');

//     return sortedStr1 === sortedStr2;
// }

// // Example usage:
// const string1 = "Astronomer";
// const string2 = "Moon starer";
// console.log(areAnagrams(string1, string2)); // Output: true

// const string3 = "School master";
// const string4 = "The classroom";
// console.log(areAnagrams(string3, string4)); // Output: true

// const string5 = "The Morse Code";
// const string6 = "Here come dots";
// console.log(areAnagrams(string5, string6)); // Output: true
