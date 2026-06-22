document.addEventListener('DOMContentLoaded', () => {
    // Mobile menu toggle
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            navLinks.classList.toggle('nav-active');
            const icon = menuToggle.querySelector('i');
            if (icon) {
                if (navLinks.classList.contains('nav-active')) {
                    icon.classList.remove('ph-list');
                    icon.classList.add('ph-x');
                } else {
                    icon.classList.remove('ph-x');
                    icon.classList.add('ph-list');
                }
            }
        });
    }

    // Number counters animation (simple version)
    const stats = document.querySelectorAll('.stat-number');
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                e.preventDefault();
                targetElement.scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });
});

// Chatbot Logic
document.addEventListener('DOMContentLoaded', () => {
    // Create Chatbot HTML
    const chatbotHTML = `
        <button class="chatbot-toggler">
            <i class="ph ph-chats"></i>
        </button>
        <div class="chatbot">
            <header>
                <h3>Assistant Yafatel</h3>
                <span class="close-btn"><i class="ph ph-x"></i></span>
            </header>
            <ul class="chatbox">
                <li class="chat incoming">
                    <p>Bonjour 👋 !<br>Comment puis-je vous aider avec vos études ou livrables télécom ?</p>
                </li>
            </ul>
            <div class="chat-input">
                <input type="text" placeholder="Écrivez votre message..." required>
                <button id="send-btn"><i class="ph ph-paper-plane-right"></i></button>
            </div>
        </div>
    `;
    
    document.body.insertAdjacentHTML('beforeend', chatbotHTML);

    const chatbotToggler = document.querySelector('.chatbot-toggler');
    const closeBtn = document.querySelector('.close-btn');
    const chatbox = document.querySelector('.chatbox');
    const chatInput = document.querySelector('.chat-input input');
    const sendChatBtn = document.querySelector('#send-btn');

    if(chatbotToggler) {
        chatbotToggler.addEventListener('click', () => document.body.classList.toggle('show-chatbot'));
    }
    if(closeBtn) {
        closeBtn.addEventListener('click', () => document.body.classList.remove('show-chatbot'));
    }

    const createChatLi = (message, className) => {
        const chatLi = document.createElement("li");
        chatLi.classList.add("chat", className);
        let chatContent = className === "outgoing" ? `<p></p>` : `<p></p>`;
        chatLi.innerHTML = chatContent;
        chatLi.querySelector("p").textContent = message;
        return chatLi;
    }

    const handleChat = async () => {
        const userMessage = chatInput.value.trim();
        if (!userMessage) return;

        chatInput.value = "";
        
        // Append user message
        chatbox.appendChild(createChatLi(userMessage, "outgoing"));
        chatbox.scrollTo(0, chatbox.scrollHeight);

        // Show "Typing..." indicator
        const typingLi = createChatLi("L'assistant rédige...", "incoming");
        chatbox.appendChild(typingLi);
        chatbox.scrollTo(0, chatbox.scrollHeight);

        try {
            // Call our Vercel Serverless Function backend
            const response = await fetch("/api/chat", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ message: userMessage })
            });
            
            const data = await response.json();
            
            // Remove typing indicator and show real response
            chatbox.removeChild(typingLi);
            
            if (data.reply) {
                // If it's the demo message with HTML, we can use innerHTML, but for safety textContent is default.
                // However, our demo mode has an <a> tag. Let's use innerHTML for incoming messages to allow links to work.
                const incomingChatLi = document.createElement("li");
                incomingChatLi.classList.add("chat", "incoming");
                incomingChatLi.innerHTML = `<p>${data.reply}</p>`;
                chatbox.appendChild(incomingChatLi);
            } else {
                chatbox.appendChild(createChatLi("Une erreur est survenue.", "incoming"));
            }
        } catch (error) {
            chatbox.removeChild(typingLi);
            chatbox.appendChild(createChatLi("Erreur de connexion. Veuillez réessayer.", "incoming"));
        }
        
        chatbox.scrollTo(0, chatbox.scrollHeight);
    }

    if(sendChatBtn) {
        sendChatBtn.addEventListener("click", handleChat);
    }
    if(chatInput) {
        chatInput.addEventListener("keydown", (e) => {
            if(e.key === "Enter" && !e.shiftKey) {
                e.preventDefault();
                handleChat();
            }
        });
    }
});


// Initialize Vanta.js AI-like Animated Network Background
document.addEventListener('DOMContentLoaded', () => {
    if (typeof VANTA !== 'undefined' && document.querySelector('#vanta-hero')) {
        VANTA.NET({
            el: "#vanta-hero",
            mouseControls: true,
            touchControls: true,
            gyroControls: false,
            minHeight: 200.00,
            minWidth: 200.00,
            scale: 1.00,
            scaleMobile: 1.00,
            color: 0x0066FF, // Accent Blue
            backgroundColor: 0x0A192F, // Primary Deep Blue
            points: 15.00,
            maxDistance: 22.00,
            spacing: 16.00,
            showDots: true
        });
    }
});
