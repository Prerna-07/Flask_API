from flask import  Flask,jsonify
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Prerna@7",
  database="test_db"
  
)
mycursor = mydb.cursor()  

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
@app.route('/put')
def put_income():
    description = input("Enter description")
    amount = input("Enter amount")
    name = input("Enter name")
    Dict = {'description': description, 'amount': amount, 'name': name}
    incomes.append(Dict)
    return "done"

@app.route('/post/<name>')
def post_income(name):
    for i in range (len(incomes)):
        if incomes[i].get('name')==name:
            del incomes[i]
            print("Enter Updated Value")
            description = input("Enter description")
            amount = input("Enter amount")
            name = input("Enter name")
            Dict = {'description': description, 'amount': amount, 'name': name}
            incomes.append(Dict)
            return "done"
    return "not found"        

     
@app.route('/delete/<name>')
def delete_income(name):
    for i in range (len(incomes)):
        if incomes[i].get('name')==name:
            del incomes[i]
            return "done"
    return "not found"

@app.route('/database/get')
def get():
    mycursor.execute("SELECT * FROM Employee")
    myresult = mycursor.fetchall()
        
    for i in myresult:    
      name=i[0]  
      salary=i[1]  
     
      print(name,salary)
    return "done"    

@app.route('/database/put')
def put():
    sql = "INSERT INTO Employee (name, salary) VALUES (%s, %s)"
    name = input("Enter name")
    salary = input("ENTER salary")
    val = (name,salary)
    mycursor.execute(sql, val)
    mydb.commit()

    
    return "data inserted"

@app.route('/database/delete/<name>')
def delete(name):
    sql = "DELETE FROM Employee WHERE name = %s"
    n = (name,)
    try:
        mycursor.execute(sql, n)
        mydb.commit()
        return "data deleted" 
    except:
        return "data dne" 

       
@app.route('/database/post/<name>')
def post(name):
    sql = "update Employee set salary=%s where name=%s;"
    salary = input("Enter Salary")
    n = (name,salary)
    try:
        mycursor.execute(sql, n)
        mydb.commit()
        return "data updated" 
    except:
        return "data dne"
   


  




if __name__ == '__main__':
    app.run(debug=True)
