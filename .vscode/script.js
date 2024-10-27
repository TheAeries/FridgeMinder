// Predefined credentials (for demonstration purposes)
const validEmail = "vaishnavi";
const validPassword = "password123";

// Function to toggle password visibility
function togglePassword() {
    const passwordInput = document.getElementById('password');
    const eyeIcon = document.getElementById('eye');
    if (passwordInput.type === "password") {
        passwordInput.type = "text";
        eyeIcon.setAttribute("name", "eye");
    } else {
        passwordInput.type = "password";
        eyeIcon.setAttribute("name", "eye-off");
    }
}

// Function to handle login
function login(event) {
    event.preventDefault(); // Prevent the form from submitting

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const messageDiv = document.getElementById('message');

    // Check credentials
    if (email === validEmail && password === validPassword) {
        messageDiv.textContent = "Login successful!";
        messageDiv.style.color = "green";
    } else {
        messageDiv.textContent = "Invalid email or password.";
        messageDiv.style.color = "red";
    }

    return false; // Prevent form submission
}

// Attach the login function to the form submission
document.getElementById('loginForm').onsubmit = login;

// (Optional) Attach the togglePassword function to the eye icon
document.querySelector('.eye-icon').onclick = togglePassword;
