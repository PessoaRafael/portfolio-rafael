const bars = document.querySelectorAll(".bar");

bars.forEach((bar, index) => {
    const value = bar.getAttribute("data-value");
    bar.style.setProperty('--scale', value / 100);

    // delay sequencial
    bar.style.animationDelay = `${index * 0.2}s`;
});

// Optional: animação dinâmica contínua
setInterval(() => {
    bars.forEach(bar => {
        const randomValue = Math.floor(Math.random() * 80) + 20;
        bar.setAttribute("data-value", randomValue);
        bar.style.setProperty('--scale', randomValue / 100);
    });
}, 2000);

document.addEventListener("DOMContentLoaded", () => {
    const bars = document.querySelectorAll(".bar");

    bars.forEach((bar, index) => {
        const value = bar.getAttribute("data-value");
        bar.style.setProperty('--scale', value / 100);

        // delay sequencial para efeito de subida
        bar.style.animationDelay = `${index * 0.2}s`;
    });
});
