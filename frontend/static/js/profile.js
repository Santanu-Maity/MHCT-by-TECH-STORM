async function loadProfile() {

    try {

        const response = await fetch("/profile-data");
        const data = await response.json();

        if (data.status !== "success") {
            alert(data.message);
            window.location.href = "/login";
            return;
        }

        document.getElementById("fullName").textContent =
            data.user.full_name;

        document.getElementById("email").textContent =
            data.user.email;

        document.getElementById("userId").textContent =
            data.user.id;

        document.getElementById("createdAt").textContent =
            new Date(data.user.created_at).toLocaleDateString();

    }

    catch (error) {

        console.error(error);
        alert("Failed to load profile.");

    }

}

loadProfile();