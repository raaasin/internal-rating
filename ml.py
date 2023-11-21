import csv
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# List of people to rate
people = [
    "KARRI DRUVA TARAK", 
    "N S M Sampath Srinivas",
    "Mohammed Nisar Ahmed",
    "Sunkara Deepak Sai Surya Chakradhar",
    "Konathala Seshu",
    "K.V.S.Praneeth",
    "Gandham Sandeep",
    "BHEESETTI ANAND",
    "Ambati Kavitha",
    "Jetti Vasantha Laxmi",
    "Konada Narendra Neeraj",
    "Dheeraj Surakasula"
]

csv_filename = 'data/ml.csv'

with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(people)

@app.route('/')
def index():
    return render_template('index.html', people=people)

@app.route('/submit', methods=['POST'])
def submit():
    ratings = {person: int(request.form[person]) for person in people}
    with open(csv_filename, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(ratings.values())
    return """
    <html>
        <body>
            <p>Thanks for rating!</p>
            <form action='{}'>
                <input type='submit' value='Go back to index'>
            </form>
        </body>
    </html>
    """.format(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
