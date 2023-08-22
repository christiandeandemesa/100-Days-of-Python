from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
import csv
from form import CafeForm

app = Flask(__name__)
app.secret_key = "Starbucks"
Bootstrap5(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/add', methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()

    if form.validate_on_submit():
        with open("cafe-data.csv", mode="a", encoding='utf-8') as csv_file:
            csv_file.write(f"\n{form.name.data},"
                           f"{form.location.data},"
                           f"{form.openTime.data},"
                           f"{form.closeTime.data},"
                           f"{form.coffee.data},"
                           f"{form.wifi.data},"
                           f"{form.power.data}")
        return redirect(url_for('cafes'))
    
    return render_template('add.html', form=form)

@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='', encoding='utf-8') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
            
    return render_template('cafes.html', cafes=list_of_rows)

if __name__ == '__main__':
    app.run(debug=True, port=5002)
