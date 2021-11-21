from flask import Flask
from flask import request
import os
import csv
from greenhouse import Greenhouse
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


__location__ = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))
jobs = [x for x in csv.DictReader(open('backend/jobList.csv'))]


@app.route('/', methods=['GET'])
def apply_to_jobs() -> str:
    return 'Hack western'


@app.route('/api/application', methods=["POST"])
@cross_origin()
def apply_to_the_jobs() -> str:
    submission_data = request.form
    submission_files = request.files

    resume = submission_files['resume']
    cover_letter = submission_files['cover_letter']
    resume.save(os.path.join(
        __location__, resume.filename))
    cover_letter.save(os.path.join(
        __location__, cover_letter.filename))
    # first_name = submission_data['first_name']
    # last_name = submission_data['last_name']
    # email = submission_data['email']
    # phone = submission_data['phone']
    # position = submission_data['position']
    # linkedin = submission_data['linkedin']
    # website = submission_data['website']
    # github = submission_data['github']
    # twitter = submission_data['twitter']
    # location = submission_data['location']
    # grad_month = submission_data['graduation_date']
    # grad_year = submission_data['graduation_year']
    # university = submission_data['university']

    print(submission_data)
    for job in jobs:

        greenhouse = Greenhouse(
            job["Link"], job["Title"], job["Location"], job["Company"])
        greenhouse.open_window()
        greenhouse.apply(submission_data, resume.filename,
                         cover_letter.filename)
    return 'Application sent'


if __name__ == '__main__':
    app.run(debug=True, port=5000)
