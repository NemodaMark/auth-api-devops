const API_BASE = "http://localhost:8080"; // or "" if you prefer same-origin

function showResponse(data, status) {
    const box = document.getElementById("responseBox");
    box.innerText = JSON.stringify(
        { status: status, body: data },
        null,
        2
    );
}

async function registerUser() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        showResponse({ error: "Username and password required." }, 0);
        return;
    }

    const res = await fetch(`${API_BASE}/register`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    showResponse(data, res.status);
}

async function loginUser() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        showResponse({ error: "Username and password required." }, 0);
        return;
    }

    const res = await fetch(`${API_BASE}/login`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    showResponse(data, res.status);
}

async function getUsers() {
    const res = await fetch(`${API_BASE}/users`);
    const data = await res.json();
    showResponse(data, res.status);
}

async function changePassword() {
    const username = document.getElementById("username").value.trim();
    const oldPassword = document.getElementById("password").value.trim();
    const newPassword = document.getElementById("newPassword").value.trim();

    if (!username || !oldPassword || !newPassword) {
        showResponse({ error: "Username, old password and new password required." }, 0);
        return;
    }

    const res = await fetch(`${API_BASE}/change-password`, {
        method: "PUT",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            username,
            old_password: oldPassword,
            new_password: newPassword
        })
    });

    const data = await res.json();
    showResponse(data, res.status);
}

async function deleteUserAccount() {
    const username = document.getElementById("username").value.trim();
    const password = document.getElementById("password").value.trim();

    if (!username || !password) {
        showResponse({ error: "Username and password required." }, 0);
        return;
    }

    const res = await fetch(`${API_BASE}/delete-user`, {
        method: "DELETE",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ username, password })
    });

    const data = await res.json();
    showResponse(data, res.status);
}
