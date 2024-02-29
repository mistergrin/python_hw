import random
import string
import pandas
from flask import Flask

app = Flask(__name__)


@app.route("/generating-password")
def generate_password():
    password_length = random.randint(10, 20)
    password_symbols = string.ascii_letters + string.digits + string.punctuation
    list_password = []
    while True:
        for i in range(password_length):
            password_choice = random.choice(password_symbols)
            list_password.append(password_choice)
        if any(symbol.isdigit() for symbol in list_password) and any(symbol in string.ascii_letters for symbol in list_password) and any(symbol in string.punctuation for symbol in list_password):
            break
        else:
            list_password.clear()
    password = ''.join(list_password)
    return f"<p>password: {password}</p>"


@app.route("/students-average")
def calculate_average():
    data_frame = pandas.read_csv('input_data/hw.csv')
    average_height = data_frame[' Height(Inches)'].mean()
    average_weight = data_frame[' Weight(Pounds)'].mean()
    return f"<p>average height: {average_height} inches, average_weight: {average_weight} pounds</p>"


if __name__ == '__main__':
    app.run(port=9000, debug=True)
