document.addEventListener('DOMContentLoaded', function () {
    console.log("Script.js loaded successfully!");

    // --- Mobile Menu Toggle ---
    const mobileMenuButton = document.querySelector('.mobile-menu-button');
    const mobileMenu = document.querySelector('.mobile-menu');
    if (mobileMenuButton && mobileMenu) {
        mobileMenuButton.addEventListener('click', function () {
            mobileMenu.classList.toggle('hidden');
        });
    }

    // --- Smooth Scrolling ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (event) {
            event.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

    // --- Particle Animation ---
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

    // --- Contact Modal Functionality (if applicable) ---
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
    if (contactModal) {
        contactModal.addEventListener("click", function (event) {
            if (event.target === contactModal) {
                contactModal.classList.add("hidden");
            }
        });
    }

    // --- AJAX Form Submission (Reusable Setup) ---
    function setupAjaxForm(formId) {
        const form = document.getElementById(formId);
        if (form) {
            form.addEventListener('submit', function (event) {
                event.preventDefault();

                // Check that all required fields are filled
                const requiredFields = form.querySelectorAll('[required]');
                for (let field of requiredFields) {
                    if (!field.value.trim()) {
                        field.reportValidity();
                        return;
                    }
                }

                // Validate phone if exists
                const phoneInput = form.querySelector('input[type="tel"]');
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

                const formData = new FormData(form);
                console.log("Submitting form", formId, "via AJAX with data:", [...formData.entries()]);
                fetch(form.action, {
                    method: 'POST',
                    headers: { 'X-Requested-With': 'XMLHttpRequest' },
                    body: formData
                })
                    .then(response => {
                        if (!response.ok) {
                            return response.json().then(data => { throw data; });
                        }
                        return response.json();
                    })
                    .then(data => {
                        if (data.status === "success") {
                            showPopup(data.message, false);
                            form.reset();
                        } else {
                            showPopup(data.message, true);
                        }
                    })
                    .catch(errorData => {
                        const errorMsg = errorData.message || "An error occurred. Please try again later.";
                        showPopup(errorMsg, true);
                    });
            });
        }
    }
    // Setup AJAX for both contact and investing forms
    setupAjaxForm('contactForm');
    setupAjaxForm('investingForm');

    // --- Popup Function ---
    function showPopup(message, isError = false) {
        // Remove existing popup if it exists
        const existingPopup = document.getElementById('popup-message');
        if (existingPopup) {
            existingPopup.remove();
        }

        // Create a new popup element
        const popup = document.createElement('div');
        popup.id = 'popup-message';
        popup.className = 'fixed inset-0 flex items-center justify-center bg-black bg-opacity-50 z-50';
        popup.innerHTML = `
            <div class="bg-white p-8 rounded shadow-lg max-w-md mx-auto">
                <p class="text-xl font-semibold ${isError ? 'text-red-700' : 'text-purple-700'}">${message}</p>
                <button id="close-popup" class="mt-4 block px-6 py-3 bg-purple-950 text-white font-semibold rounded shadow hover:bg-purple-900">
                    Close
                </button>
            </div>
        `;

        document.body.appendChild(popup);

        // Attach event listener to the close button
        const closeBtn = popup.querySelector('#close-popup');
        if (closeBtn) {
            closeBtn.addEventListener('click', function () {
                popup.remove();
            });
        }

        // Auto-remove the popup after 6000ms
        setTimeout(function () {
            if (document.body.contains(popup)) {
                popup.remove();
            }
        }, 6000);
    }


    // --- Three.js Rotating Globe ---
    if (typeof THREE === 'undefined') {
        console.error("Three.js is not loaded. Please check your CDN link.");
        return;
    }
    const globeContainer = document.getElementById('globe-canvas');
    if (globeContainer) {
        globeContainer.style.width = '100vw';
        globeContainer.style.height = '100vh';
        const width = globeContainer.clientWidth;
        const height = globeContainer.clientHeight;
        const scene = new THREE.Scene();
        const camera = new THREE.PerspectiveCamera(75, width / height, 0.1, 1000);
        const renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setSize(width, height);
        globeContainer.appendChild(renderer.domElement);
        const geometry = new THREE.SphereGeometry(5, 64, 64);
        const textureLoader = new THREE.TextureLoader();
        const earthTexture = textureLoader.load('https://threejs.org/examples/textures/earth_atmos_2048.jpg');
        const material = new THREE.MeshPhongMaterial({ map: earthTexture });
        const sphere = new THREE.Mesh(geometry, material);
        scene.add(sphere);
        const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
        scene.add(ambientLight);
        const directionalLight = new THREE.DirectionalLight(0xffffff, 0.5);
        directionalLight.position.set(5, 5, 5);
        scene.add(directionalLight);
        camera.position.z = 10;
        window.addEventListener('resize', function () {
            const newWidth = globeContainer.clientWidth;
            const newHeight = globeContainer.clientHeight;
            renderer.setSize(newWidth, newHeight);
            camera.aspect = newWidth / newHeight;
            camera.updateProjectionMatrix();
        });
        function animate() {
            requestAnimationFrame(animate);
            sphere.rotation.y += 0.005;
            renderer.render(scene, camera);
        }
        animate();
    }
});
