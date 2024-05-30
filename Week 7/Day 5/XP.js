// // Exercise 1: Building A RESTful API (server.js)
// const express = require('express');
// const app = express();
// const PORT = 3000;

// // Data array simulating a database
// let data = [
//   { id: 1, title: 'First Post', content: 'This is the first blog post.' },
//   { id: 2, title: 'Second Post', content: 'This is the second blog post.' }
// ];

// app.use(express.json());

// // GET all posts
// app.get('/posts', (req, res) => {
//   res.json(data);
// });

// // GET specific post by id
// app.get('/posts/:id', (req, res) => {
//   const postId = parseInt(req.params.id);
//   const post = data.find(post => post.id === postId);
//   if (!post) {
//     res.status(404).json({ error: 'Post not found' });
//   } else {
//     res.json(post);
//   }
// });

// // POST a new post
// app.post('/posts', (req, res) => {
//   const newPost = req.body;
//   newPost.id = data.length + 1;
//   data.push(newPost);
//   res.status(201).json(newPost);
// });

// // PUT update post by id
// app.put('/posts/:id', (req, res) => {
//   const postId = parseInt(req.params.id);
//   const updatedPost = req.body;
//   const index = data.findIndex(post => post.id === postId);
//   if (index === -1) {
//     res.status(404).json({ error: 'Post not found' });
//   } else {
//     data[index] = { ...data[index], ...updatedPost };
//     res.json(data[index]);
//   }
// });

// // DELETE post by id
// app.delete('/posts/:id', (req, res) => {
//   const postId = parseInt(req.params.id);
//   data = data.filter(post => post.id !== postId);
//   res.sendStatus(204);
// });

// // Error handling for invalid routes
// app.use((req, res, next) => {
//   res.status(404).json({ error: 'Invalid route' });
// });

// // Error handling for server errors
// app.use((err, req, res, next) => {
//   console.error(err.stack);
//   res.status(500).json({ error: 'Internal server error' });
// });

// // Start server
// app.listen(PORT, () => {
//   console.log(`Server is running on port ${PORT}`);
// });


// // Exercise 2: Building A Basic CRUD API With Express.js (app.js)
// const express = require('express');
// const app = express();
// const PORT = 5000;

// // Basic data array containing book objects
// let books = [
//   { id: 1, title: 'Book 1', author: 'Author 1', publishedYear: 2000 },
//   { id: 2, title: 'Book 2', author: 'Author 2', publishedYear: 2010 }
// ];

// app.use(express.json());

// // Read all books
// app.get('/api/books', (req, res) => {
//   res.json(books);
// });

// // Read book by id
// app.get('/api/books/:bookId', (req, res) => {
//   const bookId = parseInt(req.params.bookId);
//   const book = books.find(book => book.id === bookId);
//   if (!book) {
//     res.status(404).json({ error: 'Book not found' });
//   } else {
//     res.json(book);
//   }
// });

// // Create a new book
// app.post('/api/books', (req, res) => {
//   const newBook = req.body;
//   newBook.id = books.length + 1;
//   books.push(newBook);
//   res.status(201).json(newBook);
// });

// // Start server
// app.listen(PORT, () => {
//   console.log(`Server is running on port ${PORT}`);
// });


// // Exercise 3: Building A Basic CRUD API With Express And Axios Using A Data Module (app.js and dataService.js)
// const express = require('express');
// const app = express();
// const PORT = 5000;
// const dataService = require('./data/dataService');

// app.use(express.json());

// // Route to fetch posts using dataService
// app.get('/posts', async (req, res) => {
//   try {
//     const posts = await dataService.fetchPosts();
//     res.json(posts);
//   } catch (error) {
//     console.error(error);
//     res.status(500).json({ error: 'Internal server error' });
//   }
// });

// // Start server
// app.listen(PORT, () => {
//   console.log(`Server is running on port ${PORT}`);
// });

// // data/dataService.js
// const axios = require('axios');

// // Function to fetch posts from JSONPlaceholder API
// async function fetchPosts() {
//   try {
//     const response = await axios.get('https://jsonplaceholder.typicode.com/posts');
//     return response.data;
//   } catch (error) {
//     throw new Error('Error fetching posts');
//   }
// }

// module.exports = { fetchPosts };
