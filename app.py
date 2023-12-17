from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='template')

JOBS = [{
    'id': 1,
    'title': 'Data Analyst',
    'Location': 'Bengaluru, India',
    'Salary': 'Rs. 10,00,000'
}, {
    'id': 2,
    'title': 'Data Engineer',
    'Location': 'Chennai, India',
    'Salary': 'Rs. 15,00,000'
}, {
    'id': 3,
    'title': 'Full Stack Developer',
    'Location': 'Delhi, India',
    'Salary': 'Rs. 10,00,000'
}]


@app.route('/')
def hello_world():
  return render_template('index.html', jobs=JOBS)


@app.route('/jobs')
def list_of_jobs():
  return jsonify(JOBS)


if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True)
