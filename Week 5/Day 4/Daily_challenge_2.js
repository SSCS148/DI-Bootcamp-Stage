// Part I 

// setTimeout(function() {
//     alert("Hello World");
//   }, 2000);


// Part II

// setTimeout(function() {
//     var container = document.getElementById("container");
//     var paragraph = document.createElement("p");
//     paragraph.textContent = "Hello World";
//     container.appendChild(paragraph);
//   }, 2000);

  
// Part II

// var interval = setInterval(function() {
//     var container = document.getElementById("container");
//     var paragraphCount = container.getElementsByTagName("p").length;
//     if (paragraphCount < 5) {
//       var paragraph = document.createElement("p");
//       paragraph.textContent = "Hello World";
//       container.appendChild(paragraph);
//     } else {
//       clearInterval(interval);
//     }
//   }, 2000);
  
//   document.getElementById("clear").addEventListener("click", function() {
//     clearInterval(interval);
//   });

  
//   Exercice 2 

//   function myMove() {
//     var elem = document.getElementById("animate");   
//     var pos = 0;
//     var id = setInterval(frame, 1);
//     function frame() {
//       if (pos == 350) {
//         clearInterval(id);
//       } else {
//         pos++; 
//         elem.style.left = pos + 'px'; 
//       }
//     }
//   }
  