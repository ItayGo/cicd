from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # CHANGE: We are now using a regular triple-quoted string instead of an f-string (f"""...""")
    # This prevents Python from attempting to parse the JavaScript keywords like 'const'.
    html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD Demo - Good Enough!</title>
    
    <style>
        /* --- CSS STYLES --- */
        /* Note: Braces are back to single { } because this is no longer an f-string */
        body {
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f4f7f6;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            overflow: hidden;
        }

        /* Fortinet Logo Container & Rotation Animation */
        .logo-container {
            width: 150px;
            height: 150px;
            margin-bottom: 20px;
            animation: rotateLogo 10s linear infinite;
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
            font-size: 4em;
            font-weight: bold;
            color: #d90f1d;
            text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.2);
            opacity: 0;
            transform: scale(0.8);
            transition: opacity 1s ease-out, transform 1s ease-out;
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
        <img src="https://static.wixstatic.com/media/c4d23b_e491b1504ef449468acb4bca99792321~mv2.jpg/v1/fill/w_420,h_280,al_c,q_90/file.jpg" 
             alt="Fortinet Shield Logo"
             title="Fortinet CI/CD Demo">
    </div>

    <h1 id="status-text">good enough!!!</h1>

    <script>
        // --- JAVASCRIPT ANIMATION ---
        
        // Function to trigger the fade-in/scale-up animation
        function animateText() {
            const statusText = document.getElementById('status-text');
            
            setTimeout(() => {
                statusText.classList.add('show-text');
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
    app.run(host="0.0.0.0", port=5000)
