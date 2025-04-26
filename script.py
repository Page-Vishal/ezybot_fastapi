import subprocess

# Name of your app module — e.g., "main:app" if your app is in main.py
uvicorn_app = "main:app"

# Run the Uvicorn server
subprocess.run([
    "uvicorn", uvicorn_app, "--reload"
])