from flask import Flask, render_template

existing_models = ['Beedle', 'Crossroads', 'M2', 'Panique']

app = Flask(__name__)

@app.route('/')
def home_page():
    return "Welcome to Flatiron Cars"

@app.route('/<string:existing_models>')
def display_model(existing_models):
    return f"Flatiron { existing_models } is in out fleet!"
