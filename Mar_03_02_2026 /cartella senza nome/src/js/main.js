// Importazione di Lenis per lo Smooth Scroll (assumendo l'uso di un modulo o CDN)
// Se usi una CDN, assicurati di averla inclusa nell'HTML.

document.addEventListener('DOMContentLoaded', () => {
    
    // 1. INIZIALIZZAZIONE SMOOTH SCROLL (Lenis)
    const lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)), // Easing fluido
        direction: 'vertical',
        gestureDirection: 'vertical',
        smooth: true,
        mouseMultiplier: 1,
        smoothTouch: false,
        touchMultiplier: 2,
        infinite: false,
    });

    function raf(time) {
        lenis.raf(time);
        requestAnimationFrame(raf);
    }
    requestAnimationFrame(raf);

    // 2. CURSORE PERSONALIZZATO
    const cursor = document.getElementById('custom-cursor');
    document.addEventListener('mousemove', (e) => {
        gsap.to(cursor, {
            x: e.clientX,
            y: e.clientY,
            duration: 0.5,
            ease: "power2.out"
        });
    });

    // 3. HERO ANIMATION (Caricamento iniziale)
    const heroTimeline = gsap.timeline({ defaults: { ease: "power4.out" } });

    heroTimeline
        .to("#hero-title", { opacity: 1, y: 0, duration: 1.5, delay: 0.5 })
        .to("#hero-subtitle", { opacity: 1, duration: 1, letterSpacing: "0.5em" }, "-=0.8")
        .from("header", { y: -100, opacity: 0, duration: 1 }, "-=1");

    // 4. SCROLL ANIMATIONS (Reveal sezioni)
    
    // Animazione Sezione Heritage
    gsap.from("#heritage img", {
        scrollTrigger: {
            trigger: "#heritage",
            start: "top 80%",
            end: "bottom 20%",
            scrub: true
        },
        scale: 1.2,
        filter: "grayscale(100%)",
        duration: 2
    });

    gsap.from("#heritage div:first-child", {
        scrollTrigger: {
            trigger: "#heritage",
            start: "top 60%",
        },
        x: -50,
        opacity: 0,
        duration: 1.5,
        ease: "power3.out"
    });

    // 5. PARALLASSE PER IL "CANVAS CONTAINER" (3D Section)
    gsap.to("#canvas-container", {
        scrollTrigger: {
            trigger: "#innovation",
            start: "top bottom",
            end: "bottom top",
            scrub: true
        },
        y: 100,
        ease: "none"
    });

    // 6. LOGICA INTERAZIONE CTA (Hover magnetico opzionale)
    const ctas = document.querySelectorAll('button');
    ctas.forEach(cta => {
        cta.addEventListener('mouseenter', () => {
            gsap.to(cursor, { scale: 4, backgroundColor: "rgba(197, 160, 134, 0.2)", mixBlendMode: "normal" });
        });
        cta.addEventListener('mouseleave', () => {
            gsap.to(cursor, { scale: 1, backgroundColor: "#C5A086", mixBlendMode: "difference" });
        });
    });

    // 7. SINCRONIZZAZIONE GSAP CON LENIS
    lenis.on('scroll', ScrollTrigger.update);
    gsap.ticker.add((time) => {
        lenis.raf(time * 1000);
    });
    gsap.ticker.lagSmoothing(0);
});