document.addEventListener('DOMContentLoaded', function () {
    console.log("Scripts.js loaded successfully!");

    // Mobile menu toggle functionality
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (event) {
            event.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // Particle Animation (runs only if .particles-container exists)
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

    // Contact Modal Functionality (if applicable)
    const contactModal = document.getElementById("contactForm");
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
    if (contactModal) {
        contactModal.addEventListener("click", function (event) {
            if (event.target === contactModal) {
                contactModal.classList.add("hidden");
            }
        });
    }

    // AJAX submission for the contact form with custom phone validation
    const contactForm = document.getElementById('contactForm');
    console.log(contactForm, "contact xsx");
    if (contactForm) {
        contactForm.addEventListener('submit', function (event) {
            console.log("Form submit intercepted");
            event.preventDefault(); // Prevent full-page reload

            const phoneInput = document.getElementById('phone');
            if (phoneInput && phoneInput.value) {
                const pattern = /^\+?[0-9\s\-()]+$/;
                if (!pattern.test(phoneInput.value)) {
                    phoneInput.setCustomValidity("Please enter a valid phone number (numbers, spaces, dashes, parentheses, and an optional leading +).");
                    phoneInput.reportValidity();
                    return;
                } else {
                    phoneInput.setCustomValidity("");
                }
            }

            const formData = new FormData(contactForm);
            console.log("Submitting via AJAX with data:", [...formData.entries()]);

            fetch(contactForm.action, {
                method: 'POST',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                },
                body: formData
            })
                .then(response => {
                    console.log("Response received:", response);
                    if (!response.ok) {
                        return response.json().then(data => { throw data; });
                    }
                    return response.json();
                })
                .then(data => {
                    console.log("AJAX submission successful:", data);
                    if (data.status === "success") {
                        showPopup(data.message, false);
                        contactForm.reset();
                    } else {
                        showPopup(data.message, true);
                    }
                })
                .catch(errorData => {
                    console.error("AJAX submission error:", errorData);
                    const errorMsg = errorData.message || "An error occurred. Please try again later.";
                    showPopup(errorMsg, true);
                });
        });
    }

    function showPopup(message, isError = false) {
        const popup = document.createElement('div');
        popup.id = 'popup-message';
        popup.className = 'fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50';
        popup.innerHTML = `
            <div class="bg-white p-8 rounded shadow-lg max-w-md mx-auto">
                <p class="text-xl font-semibold ${isError ? 'text-red-700' : 'text-green-700'}">${message}</p>
                <button id="close-popup" class="mt-4 px-4 py-2 bg-purple-950 text-white rounded hover:bg-purple-900">Close</button>
            </div>
        `;
        document.body.appendChild(popup);
        document.getElementById('close-popup').addEventListener('click', function () {
            document.body.removeChild(popup);
        });
        setTimeout(function () {
            if (document.body.contains(popup)) {
                document.body.removeChild(popup);
            }
        }, 5000);
    }
});
