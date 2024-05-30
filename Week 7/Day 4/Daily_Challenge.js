// // Task 1: Basic Module System (greeting.js)
// function greet(name) {
//     return `Hello, ${name}!`;
//   }
  
//   module.exports = greet;
  
//   // Task 2: Using an NPM Module (colorful-message.js)
//   const chalk = require('chalk');
  
//   function colorfulMessage(message) {
//     console.log(chalk.blue(message));
//   }
  
//   module.exports = colorfulMessage;
  
//   // Task 3: Advanced File Operations (read-file.js)
//   const fs = require('fs');
  
//   function readFile(fileName) {
//     const content = fs.readFileSync(fileName, 'utf8');
//     console.log(content);
//   }
  
//   module.exports = readFile;
  
//   // Challenge Task: Integrating Everything (challenge.js)
//   const greet = require('./greeting');
//   const colorfulMessage = require('./colorful-message');
//   const readFile = require('./read-file');
  
//   const userName = 'Alice';
//   const message = 'This is a colorful message!';
//   const fileName = './files/file-data.txt';
  
//   console.log(greet(userName));
//   colorfulMessage(message);
//   readFile(fileName);
  