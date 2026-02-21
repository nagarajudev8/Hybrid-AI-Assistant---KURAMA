async function sendMessage() {
    const inputField = document.getElementById("userInput");
    const chatBox = document.getElementById("chatBox");
    const userMessage = inputField.value;

    if (!userMessage) return;

    chatBox.innerHTML += `<div class="message user">You: ${userMessage}</div>`;

    const response = await fetch("/ask", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ query: userMessage })
    });

    const data = await response.json();

    chatBox.innerHTML += `<div class="message bot">Kurama: ${data.response}</div>`;
    inputField.value = "";
    chatBox.scrollTop = chatBox.scrollHeight;
}
