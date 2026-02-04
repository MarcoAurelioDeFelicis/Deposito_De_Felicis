// Registra il plugin GSAP
gsap.registerPlugin(ScrollTrigger);

// Animazione Titolo Hero
gsap.from("#hero-text", {
    duration: 1.5,
    y: 50,
    opacity: 0,
    ease: "power4.out",
    delay: 0.5
});

// Reveal delle sezioni allo scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.2 });

document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Micro-interazione al movimento mouse
document.addEventListener('mousemove', (e) => {
    const depth = 20;
    const moveX = (e.clientX - window.innerWidth / 2) / depth;
    const moveY = (e.clientY - window.innerHeight / 2) / depth;
    gsap.to(".absolute", { x: moveX, y: moveY, duration: 2, ease: "power2.out" });
});