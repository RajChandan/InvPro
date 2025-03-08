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

    // ✅ Particle Animation (runs only if .particles-container exists)
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
    createParticles();

    // ✅ Contact Modal Functionality
    const contactModal = document.getElementById("contact-modal");
    const openContactButton = document.querySelector("[data-open-contact]");
    const closeContactButton = document.querySelector("[data-close-contact]");

    if (openContactButton && contactModal) {
        openContactButton.addEventListener("click", function () {
            contactModal.classList.remove("hidden");
            contactModal.classList.add("animate-fade-in");
        });
    }
    if (closeContactButton && contactModal) {
        closeContactButton.addEventListener("click", function () {
            contactModal.classList.add("hidden");
        });
    }
    // Close modal when clicking outside the modal content
    if (contactModal) {
        contactModal.addEventListener("click", function (event) {
            if (event.target === contactModal) {
                contactModal.classList.add("hidden");
            }
        });
    }
});
