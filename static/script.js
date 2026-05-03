// Add a subtle entrance animation for cards
document.addEventListener("DOMContentLoaded", () => {
    const cards = document.querySelectorAll('.glass-card');
    cards.forEach((card, index) => {
        card.style.opacity = "0";
        card.style.transform = "translateY(30px)";
        setTimeout(() => {
            card.style.transition = "all 0.6s ease";
            card.style.opacity = "1";
            card.style.transform = "translateY(0)";
        }, 200 * index);
    });
});

function runSimulation(btn) {
    const valA = document.getElementById('f1').value;
    const valB = document.getElementById('f2').value;
    const display = document.getElementById('simValue');

    if (!valA || !valB) return alert("Please enter simulation values");

    // UI Feedback: Button state
    const originalText = btn.innerText;
    btn.innerText = "Processing Logic...";
    btn.disabled = true;
    display.innerText = "Analyzing...";

    // Mock API Call
    setTimeout(() => {
        const prediction = (parseFloat(valA) * 1.5 + parseFloat(valB) * 0.8).toFixed(2);
        display.innerText = `$${parseFloat(prediction).toLocaleString()}`;
        
        // Reset Button
        btn.innerText = originalText;
        btn.disabled = false;
        
        // Success Animation
        display.style.animation = "none";
        setTimeout(() => display.style.animation = "pulse 0.5s ease", 10);
    }, 1500);
}

// Helper for UI feel
function uploadFile(btn) {
    btn.innerText = "Reading Data Structure...";
    setTimeout(() => {
        btn.innerText = "Dataset Processed ✅";
        btn.style.background = "#10b981";
    }, 1200);
}