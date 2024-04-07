let usernanme;
document.getElementById("mySubmit").onclick = function (){
    usernanme = document.getElementById("myText").value;
    document.getElementById("Myh1").textContent = `Hello my name is ${usernanme} `
}