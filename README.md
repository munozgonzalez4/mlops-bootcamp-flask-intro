# mlops-bootcamp-flask-intro
Introduction to Flask Framework

Flask: used to develop end to end web app aplications.
Other framework like FastAPI or Django.

Two important components:
    - Web Server Gateway Interface (WSGI)
    - Jinja 2 Template Engine

Definition: complete web framework which is created with Python programming.

Concept: Web Server.
- Where we deploy the applications
- It's located in an instance (AWS, Azure, Apache, ...)
- Web App is created in Flask framework
- Request from users arrive to Web Server -> Server communicates with the Web App to get the response back. Everything happens via a Protocol: WSGI

Concept: Jinja 2.
- It's a Web Template Engine
- Combines a Web Template (pages) with a Data Source (SQL, csv, Mongo, ML Model...)
- Web Pages gets loaded
- Example: Web Page with a "upload" button of an image of a dog/cat, then Web Page interacts with ML Model that will return if it's a dog or a cat
- Summary: combine a layout of a page with creating dynamic web pages.  


---

Steps to create the environment:

conda create -p venv python==3.12
If facing error, to clean use: conda clean --all
conda activate venv/
To deactivate: conda deactivate

Useful commands:
To go back in the path: cd ..
To install requirements: pip install -r requirements.txt
To run the app: python app.py
