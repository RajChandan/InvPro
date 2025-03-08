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

document.addEventListener("DOMContentLoaded", function () {
    console.log("Scripts loaded successfully!");

    // ✅ Mobile Menu Toggle
    const mobileMenuButton = document.querySelector(".mobile-menu-button");
    const mobileMenu = document.querySelector(".mobile-menu");

    if (mobileMenuButton) {
        mobileMenuButton.addEventListener("click", function () {
            mobileMenu.classList.toggle("hidden");
        });
    }

    // ✅ Contact Modal Functionality
    const contactModal = document.getElementById("contact-modal");
    const openContactButton = document.querySelector("[data-open-contact]");
    const closeContactButton = document.querySelector("[data-close-contact]");
    const modalOverlay = document.getElementById("contact-modal");

    if (openContactButton) {
        openContactButton.addEventListener("click", function () {
            contactModal.classList.remove("hidden");
            contactModal.classList.add("animate-fade-in");
        });
    }

    if (closeContactButton) {
        closeContactButton.addEventListener("click", function () {
            contactModal.classList.add("hidden");
        });
    }

    // ✅ Close Modal When Clicking Outside
    if (modalOverlay) {
        modalOverlay.addEventListener("click", function (event) {
            if (event.target === modalOverlay) {
                contactModal.classList.add("hidden");
            }
        });
    }
});
