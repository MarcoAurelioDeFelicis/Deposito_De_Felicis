gsap.registerPlugin(ScrollTrigger);

// Animazione Titolo Hero all'avvio
window.addEventListener('load', () => {
    gsap.to("#hero-main", {
        duration: 2,
        y: 0,
        opacity: 1,
        ease: "power4.out",
        startAt: { y: 50, opacity: 0 }
    });
    
    gsap.to("#hero-sub", {
        duration: 1.5,
        y: 0,
        opacity: 1,
        ease: "power3.out",
        delay: 0.5,
        startAt: { y: 20, opacity: 0 }
    });
});

// Reveal delle sezioni allo scroll
const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
        if (entry.isIntersecting) {
            entry.target.classList.add('active');
        }
    });
}, { threshold: 0.15 });

// Osserva tutti gli elementi con classe 'reveal'
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

// Effetto parallasse sfondo al movimento mouse
document.addEventListener('mousemove', (e) => {
    const x = (e.clientX - window.innerWidth / 2) / 50;
    const y = (e.clientY - window.innerHeight / 2) / 50;
    gsap.to("#hero-bg", { x: x, y: y, duration: 2, ease: "power2.out" });
});