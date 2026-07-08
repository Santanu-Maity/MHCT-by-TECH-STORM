// ======================================
// SIGNUP
// ======================================

const signupForm = document.getElementById("signupForm");
const messageBox = document.getElementById("message");

if (signupForm) {

    signupForm.addEventListener("submit", async (e) => {

        e.preventDefault();

        const full_name = document.getElementById("full_name").value.trim();
        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;
        const confirm_password = document.getElementById("confirm_password").value;

        messageBox.className = "message";
        messageBox.style.display = "none";

        if (password !== confirm_password) {

            messageBox.classList.add("error");
            messageBox.style.display = "block";
            messageBox.innerText = "Passwords do not match.";

            return;
        }

        try {

            const response = await fetch("/signup", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    full_name,
                    email,
                    password
                })

            });

            const result = await response.json();
                        if (response.ok) {

                messageBox.classList.add("success");
                messageBox.style.display = "block";
                messageBox.innerText = result.message;

                signupForm.reset();

                setTimeout(() => {
                    window.location.href = "/login";
                }, 2000);

            } else {

                messageBox.classList.add("error");
                messageBox.style.display = "block";
                messageBox.innerText = result.message;
            }

        } catch (error) {

            messageBox.classList.add("error");
            messageBox.style.display = "block";
            messageBox.innerText =
                "Unable to connect to the server.";
        }

    });

}


// ======================================
// LOGIN
// ======================================

const loginForm = document.getElementById("loginForm");

if (loginForm) {

    loginForm.addEventListener("submit", async (e) => {

        e.preventDefault();

        const email = document.getElementById("email").value.trim();
        const password = document.getElementById("password").value;

        messageBox.className = "message";
        messageBox.style.display = "none";

        try {

            const response = await fetch("/login", {

                method: "POST",

                headers: {
                    "Content-Type": "application/json"
                },

                body: JSON.stringify({
                    email,
                    password
                })

            });

            const result = await response.json();

            if (response.ok) {

                messageBox.classList.add("success");
                messageBox.style.display = "block";
                messageBox.innerText = result.message;

                // We will replace this with the dashboard later
                setTimeout(() => {
                    window.location.href = "/dashboard";
                }, 1500);

            } else {

                messageBox.classList.add("error");
                messageBox.style.display = "block";
                messageBox.innerText = result.message;
            }

        } catch (error) {

            messageBox.classList.add("error");
            messageBox.style.display = "block";
            messageBox.innerText =
                "Unable to connect to the server.";
        }

    });

}