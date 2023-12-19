# CV Application

## Setup

1. Clone this repository.
2. Create a python virtual environment (venv), `Python 3.11` was used for this project.
3. Install all requirements by running the command: `pip install -r requirements.txt` (from project root in terminal)


## Running the REST API

1. Navigate to the project directory.
2. Run `python app.py`.
3. Access the endpoints via browser or something similar to Postman `/personal`, `/experience`, and `/education` for respective CV data.

## Using the CLI Command

1. With the Flask app running, open a new terminal.
2. Run `flask show-cv` to print the CV's data to the console.