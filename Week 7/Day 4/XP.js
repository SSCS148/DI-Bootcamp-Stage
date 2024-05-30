// // Exercise 1: Multiple Exports And Import Using CommonJS Syntax (products.js)
// const products = [
//     { name: "Product 1", price: 10, category: "Category 1" },
//     { name: "Product 2", price: 20, category: "Category 2" },
//     { name: "Product 3", price: 30, category: "Category 3" }
//   ];
  
//   module.exports = products;
  
//   // shop.js
//   const products = require('./products');
  
//   function findProduct(productName) {
//     return products.find(product => product.name === productName);
//   }
  
//   console.log(findProduct("Product 1"));
//   console.log(findProduct("Product 2"));
//   console.log(findProduct("Product 3"));
  
//   // Exercise 2: Advanced Module Usage Using ES6 Module Syntax (data.js)
//   const persons = [
//     { name: "John", age: 30, location: "City 1" },
//     { name: "Jane", age: 25, location: "City 2" },
//     { name: "Doe", age: 35, location: "City 3" }
//   ];
  
//   export default persons;
  
//   // app.js
//   import persons from './data';
  
//   function calculateAverageAge() {
//     const totalAge = persons.reduce((sum, person) => sum + person.age, 0);
//     return totalAge / persons.length;
//   }
  
//   console.log(`Average age: ${calculateAverageAge()}`);
  
//   // Exercise 3: File Management Using CommonJS Syntax (fileManager.js)
//   const fs = require('fs');
  
//   module.exports = {
//     readFile: function(fileName) {
//       return fs.readFileSync(fileName, 'utf8');
//     },
//     writeFile: function(fileName, data) {
//       fs.writeFileSync(fileName, data);
//     }
//   };
  
//   // app.js
//   const { readFile, writeFile } = require('./fileManager');
  
//   const content = readFile('Hello World.txt');
//   writeFile('Bye World.txt', 'Writing to the file');
  
//   // Exercise 4: Todo List Using ES6 Module Syntax (todo.js)
//   export class TodoList {
//     constructor() {
//       this.tasks = [];
//     }
  
//     addTask(task) {
//       this.tasks.push(task);
//     }
  
//     markTaskComplete(taskIndex) {
//       this.tasks[taskIndex].complete = true;
//     }
  
//     listTasks() {
//       return this.tasks;
//     }
//   }
  
//   // app.js
//   import { TodoList } from './todo';
  
//   const todoList = new TodoList();
  
//   todoList.addTask({ description: "Task 1", complete: false });
//   todoList.addTask({ description: "Task 2", complete: false });
//   todoList.addTask({ description: "Task 3", complete: true });
  
//   console.log(todoList.listTasks());
  
//   // Exercise 5: Creating And Using A Custom Module (math.js)
//   export function add(a, b) {
//     return a + b;
//   }
  
//   export function multiply(a, b) {
//     return a * b;
//   }
  
//   // app.js
//   const math = require('./math');
//   const _ = require('lodash');
  
//   console.log(math.add(5, 3));
//   console.log(math.multiply(5, 3));
//   console.log(_.random(1, 100));
  
//   // Exercise 6: Simple NPM Package Usage (app.js)
//   const chalk = require('chalk');
  
//   console.log(chalk.blue('Hello world!'));
  
//   // Exercise 7: Reading And Copying Files (copy-file.js)
//   const fs = require('fs');
  
//   const sourceContent = fs.readFileSync('source.txt', 'utf8');
//   fs.writeFileSync('destination.txt', sourceContent);
  
//   // read-directory.js
//   const fs = require('fs');
  
//   fs.readdir('.', (err, files) => {
//     if (err) {
//       console.error('Error reading directory:', err);
//       return;
//     }
//     console.log('Files in the directory:', files);
//   });
  