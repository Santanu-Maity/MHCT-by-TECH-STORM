const chatBox = document.getElementById("chatBox");
const userInput = document.getElementById("userInput");
const sendBtn = document.getElementById("sendBtn");

// ==========================
// Add Message to Chat
// ==========================
function addMessage(message, sender) {

    const messageDiv = document.createElement("div");

    if (sender === "user") {
        messageDiv.className = "user-message";
        messageDiv.innerHTML = "🧑 " + message;
    } else {
        messageDiv.className = "bot-message";
        messageDiv.innerHTML = "🤖 " + message;
    }

    chatBox.appendChild(messageDiv);

    chatBox.scrollTop = chatBox.scrollHeight;
}

// ==========================
// Send Message
// ==========================
async function sendMessage() {

    const message = userInput.value.trim();

    if (message === "") return;

    addMessage(message, "user");

    userInput.value = "";

    try {

        const response = await fetch("/chat", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                message: message
            })
        });

        const data = await response.json();

        if (data.status === "success") {
            addMessage(data.reply, "bot");
        } else {
            addMessage(data.message, "bot");
        }

    } catch (error) {

        addMessage("Unable to connect to the server.", "bot");

        console.error(error);

    }

}

// ==========================
// Events
// ==========================
sendBtn.addEventListener("click", sendMessage);

userInput.addEventListener("keypress", function (event) {

    if (event.key === "Enter") {
        sendMessage();
    }

});