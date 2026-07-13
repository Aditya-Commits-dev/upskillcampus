from flask import Flask, request, redirect, render_template_string
import sqlite3
import random
import string
import validators

app = Flask(__name__)

DATABASE = "url_shortener.db"


# -----------------------------
# Database Initialization
# -----------------------------
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            original_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()


# -----------------------------
# Generate Short Code
# -----------------------------
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits

    while True:
        code = ''.join(random.choice(characters) for _ in range(length))

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM urls WHERE short_code=?",
            (code,)
        )

        exists = cursor.fetchone()
        conn.close()

        if not exists:
            return code


# -----------------------------
# Home Page
# -----------------------------
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>URL Shortener</title>

<style>

body{
font-family:Arial;
background:#f4f4f4;
margin:0;
padding:0;
}

.container{
width:600px;
margin:60px auto;
background:white;
padding:30px;
border-radius:10px;
box-shadow:0px 0px 10px gray;
}

h1{
text-align:center;
color:#2c3e50;
}

input[type=text]{
width:100%;
padding:12px;
margin-top:10px;
}

button{
margin-top:15px;
padding:12px;
width:100%;
background:#3498db;
color:white;
border:none;
cursor:pointer;
font-size:16px;
}

button:hover{
background:#2980b9;
}

.result{
margin-top:25px;
background:#eafaf1;
padding:15px;
border-radius:6px;
}

.error{
margin-top:20px;
background:#ffe6e6;
padding:12px;
color:red;
}

</style>

</head>

<body>

<div class="container">

<h1>URL Shortener</h1>

<form method="POST">

<input
type="text"
name="url"
placeholder="Enter Long URL"
required>

<button type="submit">
Generate Short URL
</button>

</form>

{% if short_url %}

<div class="result">

<b>Original URL</b><br>

{{original}}<br><br>

<b>Short URL</b><br>

<a href="{{short_url}}">
{{short_url}}
</a>

</div>

{% endif %}

{% if error %}

<div class="error">

{{error}}

</div>

{% endif %}

</div>

</body>

</html>

"""


@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        original_url = request.form["url"]

        if not validators.url(original_url):

            return render_template_string(
                HTML,
                error="Invalid URL!"
            )

        code = generate_short_code()

        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()

        cursor.execute(
            "INSERT INTO urls(original_url,short_code) VALUES(?,?)",
            (original_url, code)
        )

        conn.commit()
        conn.close()

        short_url = request.host_url + code

        return render_template_string(
            HTML,
            short_url=short_url,
            original=original_url
        )

    return render_template_string(HTML)


# -----------------------------
# Redirect
# -----------------------------
@app.route("/<code>")
def redirect_url(code):

    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT original_url FROM urls WHERE short_code=?",
        (code,)
    )

    result = cursor.fetchone()

    conn.close()

    if result:
        return redirect(result[0])

    return "<h2>404 - URL Not Found</h2>"


# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":

    init_db()

    app.run(debug=True)
