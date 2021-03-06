from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

print(__name__)

@app.route("/")
def my_home():
    return render_template('index.html')

@app.route("/index.html")
def home():
    return render_template('index.html')

@app.route("/<string:page_name>")
def all_pages(page_name):
    return render_template(page_name)

def write_to_file(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'\n {email}, {subject}, {message}')

def write_to_csv(data):
    with open('database.csv', newline='', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',')
        csv_writer.writerow([email, subject, message])

@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        data = request.form.to_dict()
        write_to_file(data)
        write_to_csv(data)
        print(data)
        return redirect('/thankyou.html')
    else:
        return 'Something went wrong. Try again'


