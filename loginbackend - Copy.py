from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "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"  # Change this in production

# Dummy users database
users = {
    "shaurya": "password123",
    "guest": "1234"
}

# Login page HTML
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Login — Finance & Productivity</title>
<style>
:root{
--bg:#f0fdf4; --card:#ffffff; --accent:#166534; --accent-light:#22c55e;
--radius:12px; --shadow:0 6px 20px rgba(0,0,0,0.08);
}
*{box-sizing:border-box;}
body{margin:0;font-family:Inter,ui-sans-serif,system-ui,Segoe UI,Roboto,Helvetica,Arial;background:var(--bg);color:#0f172a;line-height:1.5;min-height:100vh;display:flex;flex-direction:column;}
header{display:flex;align-items:center;padding:16px;}
header img{height:60px;width:60px;margin-right:12px;}
header h2{margin:0;font-size:22px;color:var(--accent);}
main{flex:1;display:flex;align-items:center;justify-content:center;}
.card{background:var(--card);padding:32px;border-radius:var(--radius);box-shadow:var(--shadow);width:100%;max-width:360px;}
h1{margin:0 0 20px;font-size:24px;text-align:center;color:var(--accent);}
label{display:block;margin-bottom:6px;font-weight:600;color:#374151;}
input{width:100%;padding:10px 12px;margin-bottom:16px;border:1px solid #d1d5db;border-radius:8px;font-size:15px;}
input:focus{outline:none;border-color:var(--accent);box-shadow:0 0 0 3px rgba(34,197,94,0.25);}
button{width:100%;padding:12px;border:none;border-radius:8px;background:var(--accent);color:white;font-weight:600;font-size:15px;cursor:pointer;}
button:hover{background:var(--accent-light)}
.footer-text{text-align:center;margin-top:16px;font-size:14px;color:#374151;}
.footer-text a{color:var(--accent);text-decoration:none;font-weight:600;}
.footer-text a:hover{text-decoration:underline;}
</style>
</head>
<body>
  
<header>
  <img src="./logo.png" alt="SelfCatalyser">
  <h2>SelfCatalyser</h2>
</header>

<main>
  <div class="card">
    <h1>Login</h1>
    <form method="POST">
      <label for="username">Username</label>
      <input type="text" id="username" name="username" placeholder="Enter username" required>

      <label for="password">Password</label>
      <input type="password" id="password" name="password" placeholder="••••••••" required>

      <button type="submit">Sign In</button>
    </form>
    {% if error %}
      <p style="color:red; text-align:center;">{{ error }}</p>
    {% endif %}
    <div class="footer-text">
      <p>Don’t have an account? <a href="SCsignup.html">Sign up</a></p>
    </div>
  </div>
</main>
</body>
</html>
"""

# Dashboard page HTML
dashboard_page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Dashboard</title>
</head>
<body style="font-family:Arial; text-align:center; margin-top:50px;">
  <h1>Welcome, {{ user }}!</h1>
  <p>You are logged in successfully.</p>
  <a href="{{ url_for('logout') }}">Logout</a>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    error = None
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username in users and users[username] == password:
            session["user"] = username
            return redirect(url_for("dashboard"))
        else:
            error = "Invalid username or password!"
    return render_template_string(login_page, error=error)

@app.route("/dashboard")
def dashboard():
    if "user" in session:
        return render_template_string(dashboard_page, user=session["user"])
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
