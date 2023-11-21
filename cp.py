import pandas as pd
from flask import Flask, render_template, request, url_for

app = Flask(__name__)

people = [
    "Shivram Rambhatla", 
    "Purijala Venkata Prabhath"
]


csv_filename = 'data/cp.csv'

ratings = pd.DataFrame(columns=people)
ratings.to_csv(csv_filename, index=False)


@app.route('/')
def index():
    return render_template('index.html', people=people)

@app.route('/submit', methods=['POST'])
def submit():
    global ratings
    new_ratings = pd.DataFrame([list(map(int, request.form.values()))], columns=people)
    ratings = pd.concat([ratings, new_ratings], ignore_index=True)
    ratings.to_csv(csv_filename, index=False)
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
