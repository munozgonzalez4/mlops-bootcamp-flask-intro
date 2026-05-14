# mlops-bootcamp-flask-intro
A simple Flask exploration for building web applications with Python.

This repository is a small Flask introduction, with examples of routing, templates, and dynamic pages.

Flask is used to develop end-to-end web applications. Other popular Python web frameworks include FastAPI and Django.

Key components in this project:
- Web Server Gateway Interface (WSGI)
- Jinja2 template engine

What this means:

Web Server
- Deploys the application
- Runs on an instance such as AWS, Azure, Apache, etc.
- Receives requests from users and forwards them to the Flask app
- Communicates with the app using the WSGI protocol

Jinja2
- A web template engine
- Combines HTML templates with data sources like SQL, CSV, MongoDB, or ML models
- Generates dynamic pages based on the data
- Example: a page with an upload button for a dog/cat image, where the app returns whether the image is a dog or a cat
- In short, it merges page layout and data to create dynamic web pages

---

Environment setup:

```bash
conda create -p venv python==3.12
conda activate venv/
```

If you see issues, clean Conda with:

```bash
conda clean --all
```

To deactivate:

```bash
conda deactivate
```

Useful commands:

```bash
cd ..
pip install -r requirements.txt
python app.py
```
