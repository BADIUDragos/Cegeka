import json

from flask import Flask, jsonify

from extract_cv_data import extract_and_structure_cv_data

app = Flask(__name__)

cv_data = extract_and_structure_cv_data('Dragos_Badiu_CV_RO-1.pdf')


@app.route('/personal', methods=['GET'])
def personal():
    return jsonify(cv_data['personal'])


@app.route('/experience', methods=['GET'])
def experience():
    return jsonify(cv_data['experience'])


@app.route('/education', methods=['GET'])
def education():
    return jsonify(cv_data['education'])


@app.cli.command("show-cv", methods=['GET'])
def show_cv():
    print(json.dumps(cv_data, indent=4))


if __name__ == '__main__':
    app.run(debug=True)
