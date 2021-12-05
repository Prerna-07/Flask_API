from flask import  Flask,jsonify

app = Flask(__name__)

incomes = [{
    'description': 'salary','amount':5000,'name':'ayush'
},{
    'description': 'salary','amount':15000,'name':'gaurav'
},
{
    'description': 'salary','amount':1000,'name':'abhijith'
},
    {}


]

@app.route("/<name>")
def hello_world(name):
    return f"Hello {name}"

@app.route('/incomes')
def get_incomes():
    return jsonify(incomes)

@app.route('/income/<name>')
def filter_income(name):
    for income in incomes:
        if income.get('name') == name:
            return jsonify(income)
    return "Not Found"


if __name__ == '__main__':
    app.run(host='0.0.0.0',debug=True)
