from flask import Flask, jsonify
from faker import Faker
from webargs.flaskparser import use_kwargs
from webargs import fields, validate
import requests
import csv


app = Flask(__name__)
fake = Faker()


@app.route("/generating-students")
@use_kwargs(
    {
        'count': fields.Int(
            missing=15,
            validate=[validate.Range(max_inclusive=True, max=1000)]
        )
    },
    location='query'
)
def generate_students(count: int):
    students = []
    for i in range(count):
        first_name = fake.first_name()
        last_name = fake.last_name()
        email = fake.free_email()
        password = fake.password(length=10)
        date_birthday = fake.date_of_birth(minimum_age=18, maximum_age=60)
        students.append({
            'firstname': first_name,
            'lastname': last_name,
            'email': email,
            'password': password,
            'date_birthday': date_birthday
        })
    with open('students.csv', mode='w', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=students[0].keys())
        writer.writeheader()
        writer.writerows(students)
    return jsonify(students)


@app.route("/bitcoin-value")
@use_kwargs({
        'currency': fields.Str(
            missing='USD'
        ),
        'count': fields.Int(
            missing=1,
            validate=[validate.Range(max_inclusive=True, max=100)]
        )
}, location='query'
)
def get_bitcoin_value(currency: str, count: int):
    url = 'https://bitpay.com/api/rates'
    response = requests.get(url)
    list_dicts = response.json()
    for data in list_dicts:
        if data['code'] == currency:
            value = data['rate'] * count
    return f"<p>value: {value}</p>"


if __name__ == '__main__':
    app.run(port=8000, debug=True)
