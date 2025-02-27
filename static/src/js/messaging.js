document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.send-message').forEach(button => {
        button.addEventListener('click', function () {
            let contactId = this.getAttribute('contact-id');
            let message = prompt("Enter your message:");
            if (message) {
                fetch('/my/send_message', {
                    method: 'POST',
                    headers: {'Content-Type': 'application/json'},
                    body: JSON.stringify({ contact_id: contactId, message: message })
                }).then(response => response.json()).then(data => {
                    if (data) alert("Message sent successfully!");
                    else alert("Failed to send message.");
                });
            }
        });
    });
});