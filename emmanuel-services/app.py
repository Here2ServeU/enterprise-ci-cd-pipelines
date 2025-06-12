from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        inquiry = request.form.get("message")
        message = f"Thank you, {name}! We'll get back to you at {email} soon."

    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Emmanuel Services</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background-color: #f4f6f9;
                color: #333;
                text-align: center;
                padding: 50px;
            }
            .container {
                max-width: 750px;
                margin: auto;
                background-color: white;
                padding: 40px;
                border-radius: 10px;
                box-shadow: 0 0 15px rgba(0, 0, 0, 0.1);
            }
            h1 {
                color: #007acc;
            }
            ul {
                list-style: none;
                padding: 0;
            }
            li {
                background: #e8f0fe;
                margin: 10px 0;
                padding: 12px;
                border-radius: 8px;
                font-size: 1.1em;
            }
            form {
                margin-top: 30px;
                text-align: left;
            }
            input, textarea {
                width: 100%;
                padding: 10px;
                margin-top: 10px;
                border: 1px solid #ccc;
                border-radius: 6px;
            }
            button {
                margin-top: 15px;
                padding: 10px 20px;
                background-color: #007acc;
                color: white;
                border: none;
                border-radius: 5px;
                cursor: pointer;
            }
            .links {
                margin-top: 25px;
            }
            .links a {
                margin: 0 10px;
                color: #007acc;
                text-decoration: none;
                font-weight: bold;
            }
            footer {
                margin-top: 30px;
                font-size: 0.9em;
                color: #777;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>Welcome to Emmanuel Services</h1>
            <p>We help companies modernize tech operations with automation, resilience, and security.</p>
            <ul>
                <li>DevOps Automation</li>
                <li>SRE Best Practices</li>
                <li>AI-Powered Infrastructure Optimization</li>
                <li>CI/CD Pipeline Design</li>
                <li>Cloud Security & DevSecOps</li>
            </ul>

            {% if message %}
            <p><strong>{{ message }}</strong></p>
            {% endif %}

            <form method="POST">
                <h3>Contact Us</h3>
                <label for="name">Your Name</label>
                <input type="text" name="name" required>
                <label for="email">Your Email</label>
                <input type="email" name="email" required>
                <label for="message">Message</label>
                <textarea name="message" rows="4" required></textarea>
                <button type="submit">Send</button>
            </form>

            <div class="links">
                <a href="https://www.linkedin.com/in/ready2assist/" target="_blank">LinkedIn</a>
                <a href="https://github.com/Here2ServeU" target="_blank">GitHub</a>
            </div>

            <footer>&copy; 2025 Emmanuel Naweji. All rights reserved.</footer>
        </div>
    </body>
    </html>
    """
    return render_template_string(html_content, message=message)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
