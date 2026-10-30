# Hello, Docker!

A tiny beginner project: a Flask web page running inside a Docker container.

## Run it

1. Install and start Docker Desktop.
2. In this folder, run:

   ```powershell
   docker compose up --build
   ```

3. Open [http://localhost:5000](http://localhost:5000) in your browser.
4. Stop it with **Ctrl+C** in the terminal. To remove the container, run:

   ```powershell
   docker compose down
   ```

## What to try

- Edit the text in `app.py`, then run `docker compose up --build` again.
- Change the host port in `compose.yaml` from `5000:5000` to `8080:5000`, then visit `http://localhost:8080`.
- Look at the `Dockerfile` to see how Docker installs Python, copies the app, and starts it.
