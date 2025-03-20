document.addEventListener('DOMContentLoaded', () => {
    const messageInput = document.getElementById('messageInput');
    const sendButton = document.getElementById('sendButton');
    const chatBox = document.getElementById('chatBox');

    function appendMessage(text, sender) {
        const messageDiv = document.createElement('div');
        messageDiv.className = `message ${sender}-message`; // Corrected this line
        messageDiv.innerHTML = `<span class="message-text">${text}</span>`; // Corrected this line
        chatBox.appendChild(messageDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Scroll to the bottom
    }

    sendButton.addEventListener('click', () => {
        const messageText = messageInput.value.trim();
        if (messageText) {
            appendMessage(messageText, 'user');
            messageInput.value = ''; // Clear the input
            // Simulate a bot reply
            setTimeout(() => {
                appendMessage("This is a bot reply.", 'bot');
            }, 1000);
        }
    });

    messageInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') {
            sendButton.click();
        }
    });
});

