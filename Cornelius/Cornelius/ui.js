document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input').value;
    if (userInput.trim() !== '') {
        addMessage('User', userInput);
        document.getElementById('user-input').value = '';
        // Simulate Cornelius response
        setTimeout(() => {
            addMessage('Cornelius', 'This is a response from Cornelius.');
        }, 1000);
    }
});

function addMessage(sender, message) {
    const messagesDiv = document.getElementById('messages');
    const messageElement = document.createElement('div');
    messageElement.textContent = `${sender}: ${message}`;
    messagesDiv.appendChild(messageElement);
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function enhanceUI() {
    // Add a more intuitive layout
    // ...existing code...
    // Improve button accessibility
    document.querySelectorAll('button').forEach(button => {
        button.setAttribute('aria-label', button.innerText);
    });
    // ...existing code...
}

// Call the enhanceUI function on page load
window.onload = function() {
    enhanceUI();
    // ...existing code...
};
