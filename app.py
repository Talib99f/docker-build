from flask import Flask

app = Flask(__name__)


@app.get("/")
def home():
    return """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Hello, Docker!</title>
    <style>
      body { font: 1.2rem system-ui, sans-serif; max-width: 42rem; margin: 12vh auto; padding: 0 1.5rem; color: #183153; }
      h1 { color: #1677c8; }
      code { background: #eef5fb; padding: .2rem .4rem; border-radius: .3rem; }
    </style>
  </head>
  <body>
    <h1>Hello from Docker! 🐳</h1>
    <p>Your Flask app is running inside a container.</p>
    <p>Try changing <code>app.py</code>, then rebuild the image.</p>
  </body>
</html>"""


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
