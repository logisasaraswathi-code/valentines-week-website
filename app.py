from flask import Flask, render_template_string, redirect, url_for

app = Flask(__name__)

# ✨ PERSONALIZATION ✨
YOUR_NAME = "Your Name"
PARTNER_NAME = "Partner Name"

base_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Valentine's Week 💖</title>
    <style>
        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #ff758c, #ff7eb3);
            color: white;
            text-align: center;
        }
        .card {
            margin: 20px;
            padding: 25px;
            background: rgba(255,255,255,0.25);
            border-radius: 20px;
        }
        a, button {
            display: block;
            width: 100%;
            padding: 12px;
            margin: 10px 0;
            background: rgba(255,255,255,0.3);
            border-radius: 12px;
            color: white;
            text-decoration: none;
            font-weight: bold;
            border: none;
            cursor: pointer;
        }
        a:hover, button:hover {
            background: rgba(255,255,255,0.4);
        }
        footer {
            margin-top: 20px;
            font-size: 0.9rem;
        }
    </style>
</head>
<body>
    <div class="card">
        {{ content }}
        <hr>
        <a href="/">🏠 Home</a>
        <a href="/rose">🌹 Rose Day</a>
        <a href="/propose">💍 Propose Day</a>
        <a href="/chocolate">🍫 Chocolate Day</a>
        <a href="/teddy">🧸 Teddy Day</a>
        <a href="/promise">🤝 Promise Day</a>
        <a href="/hug">🤗 Hug Day</a>
        <a href="/kiss">😘 Kiss Day</a>
        <a href="/valentine">❤️ Valentine's Day</a>
        <a href="/question">💌 Special Question</a>
        <footer>Made with ❤️ by {{ your_name }}</footer>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(
        base_template,
        your_name=YOUR_NAME,
        content=f"<h1>💝 Happy Valentine's Week 💝</h1><p>Dear {PARTNER_NAME}, every day with you is special.</p>"
    )

@app.route('/rose')
def rose():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>🌹 Rose Day</h2><p>This rose is for you, {PARTNER_NAME}.</p>")

@app.route('/propose')
def propose():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>💍 Propose Day</h2><p>{PARTNER_NAME}, my heart chooses you.</p>")

@app.route('/chocolate')
def chocolate():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>🍫 Chocolate Day</h2><p>Life is sweeter with you, {PARTNER_NAME}.</p>")

@app.route('/teddy')
def teddy():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>🧸 Teddy Day</h2><p>A warm teddy hug for you!</p>")

@app.route('/promise')
def promise():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>🤝 Promise Day</h2><p>I promise to always stand by you.</p>")

@app.route('/hug')
def hug():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>🤗 Hug Day</h2><p>Sending you a big hug!</p>")

@app.route('/kiss')
def kiss():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>😘 Kiss Day</h2><p>All my kisses are for you.</p>")

@app.route('/valentine')
def valentine():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h2>❤️ Valentine's Day</h2><p>{PARTNER_NAME}, you are my forever.</p>")

@app.route('/question')
def question():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"""
        <h2>💌 A Special Question</h2>
        <p>{PARTNER_NAME}, will you be my Valentine? 💖</p>
        <form action="/yes"><button>YES 😍</button></form>
        <form action="/no"><button>NO 🙈</button></form>
        """)

@app.route('/yes')
def yes():
    return render_template_string(base_template, your_name=YOUR_NAME,
        content=f"<h1>🎉 YAY 🎉</h1><p>{PARTNER_NAME}, you made me the happiest! 💕</p>")

@app.route('/no')
def no():
    return redirect(url_for('question'))

if __name__ == "__main__":
    app.run(debug=True)
