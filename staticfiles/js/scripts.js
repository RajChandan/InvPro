document.addEventListener('DOMContentLoaded', function () {
    console.log("Scripts.js loaded successfully!");

    // ✅ Mobile menu toggle functionality
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');

    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // ✅ Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (event) {
            event.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // ✅ Particle Animation (Fix: Check if `.particles-container` exists before running)
    function createParticles() {
        const container = document.querySelector('.particles-container');

        if (!container) {
            console.warn("Particles container not found. Skipping particle creation.");
            return;
        }

        for (let i = 0; i < 50; i++) {
            const particle = document.createElement('div');
            particle.className = 'particle';
            particle.style.left = Math.random() * 100 + '%';
            particle.style.animationDelay = Math.random() * 15 + 's';
            container.appendChild(particle);
        }
    }

    createParticles(); // ✅ Runs only if `.particles-container` exists
});
