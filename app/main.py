from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    # Use f-strings for easier HTML construction in Python
    # This HTML includes embedded CSS for styling.
    html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <title>Improved Flask App</title>
    <style>
        body {{
            /* Beautiful Background: A subtle gradient or color */
            background-color: #f0f0f0;
            background-image: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
            color: #333;
            font-family: 'Arial', sans-serif;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            text-align: center;
        }}
        .container {{
            background-color: white;
            padding: 40px 60px;
            border-radius: 12px;
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.1);
            max-width: 80%;
        }}
        h1 {{
            color: #d90000; /* Fortinet-like red for emphasis */
            font-size: 3em;
            margin-bottom: 20px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }}
        .fortinet-logo {{
            /* To actually display the Fortinet logo, you need a publicly 
               accessible URL for the image. For this example, I'll use 
               a placeholder image that represents a stylized logo.
               
               NOTE: Replace 'placeholder-logo.png' with the actual URL 
               of the Fortinet logo if you have one hosted publicly.
            */
            width: 150px; 
            height: auto; 
            margin-bottom: 30px;
            content: url('https://upload.wikimedia.org/wikipedia/commons/e/ee/Fortinet_logo_2021.svg');
            /* The image above is the publicly available Fortinet logo from Wikimedia Commons. */
        }}
    </style>
</head>
<body>
    <div class="container">
        <img class="fortinet-logo" alt="Fortinet Logo Placeholder">
        <h1>GOOD ENOUGH!!!!</h1>
    </div>
</body>
</html>
"""
    return html_content

if __name__ == "__main__":
    # Same run configuration as you had
    app.run(host="0.0.0.0", port=5000)
