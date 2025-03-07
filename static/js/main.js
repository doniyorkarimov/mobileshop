"use strict";

// Header Scripts
let header = document.getElementById("header");

window.addEventListener("scroll", function() {
    header.classList.toggle("sticky", window.scrollY > 0);
});


// Off-canvas Scripts
let offCanvas = document.getElementById("offCanvas");
let offCanvasBtn = document.getElementById("offCanvasBtn");
let offCanvasClose = document.getElementById("offCanvasClose");

offCanvasBtn.addEventListener("click", function() {
    offCanvas.classList.toggle("open")
});

function removeClass() {
    offCanvas.classList.remove("open");
}

offCanvasClose.addEventListener("click", removeClass);
// document.addEventListener("click", function(evn) {
//     if (evn.target.id !== "offCanvas" && evn.target.id !== "offCanvasBtn") {
//         removeClass();
//         console.log(evn.target.classList.value.split(" "));
//         console.log("close-passive" in evn.target.classList.value.split());
//     }
// });