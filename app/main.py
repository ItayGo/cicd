from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Use f-strings for easier HTML construction in Python
    # This HTML includes embedded CSS for styling.
    html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo - Good Enough!</title>
    
    <style>
        /* --- CSS STYLES --- */
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f7f6; /* Light gray-blue background */
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden; /* Hide potential overflow from animation */
        }

        /* Fortinet Logo Container & Rotation Animation */
        .logo-container {
            width: 150px;
            height: 150px;
            margin-bottom: 20px;
            animation: rotateLogo 10s linear infinite; /* Apply rotation */
        }

        .logo-container img {
            width: 100%;
            height: 100%;
            object-fit: contain;
        }

        @keyframes rotateLogo {
            from {
                transform: rotate(0deg);
            }
            to {
                transform: rotate(360deg);
            }
        }

        /* Text Styling & Initial/Final State for Animation */
        #status-text {
            font-size: 4em; /* Large text */
            font-weight: bold;
            color: #d90f1d; /* Fortinet-like red */
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            opacity: 0; /* Start invisible */
            transform: scale(0.8); /* Start slightly smaller */
            transition: opacity 1s ease-out, transform 1s ease-out; /* Smooth transitions */
        }

        /* Class added by JavaScript to trigger the animation */
        .show-text {
            opacity: 1 !important;
            transform: scale(1) !important;
        }
    </style>
</head>
<body>
    <div class="logo-container">
        <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/e0/Fortinet_Shield_logo.svg/1200px-Fortinet_Shield_logo.svg.png" 
             alt="Fortinet Shield Logo"
             title="Fortinet CI/CD Demo">
    </div>

    <h1 id="status-text">good enough!</h1>

    <script>
        // --- JAVASCRIPT ANIMATION ---
        
        // Function to trigger the fade-in/scale-up animation
        function animateText() {
            const statusText = document.getElementById('status-text');
            
            // Wait a moment (e.g., 500ms) before starting the animation 
            // to ensure the logo is visible first and CSS transition works smoothly.
            setTimeout(() => {
                statusText.classList.add('show-text');
                
                // Optional: Console log to confirm JS is running
                console.log('Text animation triggered. CI/CD Pipeline successful.');
            }, 500); 
        }

        // Run the function when the page loads
        window.onload = animateText;
    </script>
</body>
</html>

"""
    return html_content

if __name__ == "__main__":
    # Same run configuration as you had
    app.run(host="0.0.0.0", port=5000)
