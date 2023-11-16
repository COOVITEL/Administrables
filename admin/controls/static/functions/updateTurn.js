let turns = document.querySelectorAll(".update_turn");
let modalTurns = document.querySelectorAll(".modal_turn");
let closeModals = document.querySelectorAll(".close-modal");

turns.forEach(turn => {
   turn.addEventListener("click", () => {
       let modalId = "modal_turn_" + turn.dataset.id;
       document.getElementById(modalId).style.display="block";
   });
});

closeModals.forEach(turn => {
   turn.addEventListener("click", () => {
       let modalId = "modal_turn_" + turn.dataset.id;
       document.getElementById(modalId).style.display="none";
   });
});
