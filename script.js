// JavaScript for contact form submission
document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contactForm");
    const successMessage = document.getElementById("successMessage");

    form.addEventListener("submit", function(event) {
        event.preventDefault();

        // Show the success message with an animation
        successMessage.style.display = "block";
        successMessage.style.opacity = "0";
        
        setTimeout(() => {
            successMessage.style.transition = "opacity 0.5s ease";
            successMessage.style.opacity = "1";
        }, 50);

        // Clear the form inputs
        form.reset();

        // Hide the success message after a few seconds
        setTimeout(() => {
            successMessage.style.opacity = "0";
            setTimeout(() => {
                successMessage.style.display = "none";
            }, 500);
        }, 3000);
    });
});


// ----------------------------------------mission

// function showMissionPopup() {
//     const popup = document.getElementById("missionPopup");
//     popup.style.display = "flex";
//     popup.style.opacity = "0";
//     setTimeout(() => {
//         popup.style.transition = "opacity 0.3s ease";
//         popup.style.opacity = "1";
//     }, 50);
// }

// function closeMissionPopup() {
//     const popup = document.getElementById("missionPopup");
//     popup.style.transition = "opacity 0.3s ease";
//     popup.style.opacity = "0";
//     setTimeout(() => {
//         popup.style.display = "none";
//     }, 300);
// }
