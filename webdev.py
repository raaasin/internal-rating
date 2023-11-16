import csv
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

# List of people to rate
people = [
    "Sanjana Mandarapu", 
    "Bhuvan satya",
    "Vyakaranam sowmya",
    "B. Chandra Sidhardha",
    "Deekshith Kandregula",
    "M Hruthik Ram",
    "Pavan Kumar Dokku",
]

# File to store ratings
csv_filename = 'data/webdev.csv'

# Initialize CSV file with people names as headers
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(people)

# Render the HTML template with the list of people
@app.route('/')
def index():
    return render_template('index.html', people=people)

# Handle form submission with ratings
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
