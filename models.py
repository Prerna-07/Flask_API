from sqlalchemy import create_engine,Column, Integer, String,ForeignKey
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import session, sessionmaker, relationship
from flask import  Flask,jsonify
from flask import request



app = Flask(__name__)

Base = declarative_base()
class Department(Base):
    __tablename__ = "department"
    id = Column('id',Integer,primary_key=True)
    name = Column('name',String,unique=True)
    manager= Column('manager',String,nullable=True)
    
    



class Employee(Base):
    __tablename__ = "employee"
    id = Column('id',Integer,primary_key=True)
    name = Column('name',String,unique=True)
    salary= Column('salary',Integer,nullable=True)
    dept_id = Column('dept_id', Integer,nullable=True)
    

    

engine = create_engine('sqlite:///user.db',echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind = engine)

session= Session()

@app.route('/Model/adddept',methods=['POST'])
def add_department():
    data=request.get_json()
    try:
        dep=Department(**data)
        session.add(dep)
        session.commit()
        return jsonify({'message':'Department added successfully'})   
    except Exception as e:     
        return jsonify({'error':str(e)})

@app.route('/Model/getdept', methods=['GET'])
def get_department():
    try:
        dep = session.query(Department).all()
        
        data_set = {}
        c=1
        for e in dep:
            emp = session.query(Employee).filter_by(dept_id=e.id)
            u=[]
            k=1
            for i in emp:
                u.append(i.name)
            
            d = {}
            d['id']=e.id
            d['name'] = e.name
            d['manager'] = e.manager
            d['employee']=u
            data_set[c]=d
            c=c+1
        return data_set 
    except:
        return "sorry you got an error"    
    
  


@app.route('/Model/addemp',methods=['POST'])
def addEmp():
    data=request.get_json()
    try:
        emp=Employee(**data)
        session.add(emp)
        session.commit()
        return jsonify({'message':'Employee added successfully'})   
    except Exception as e:     
        return jsonify({'error':str(e)})

@app.route('/Model/getemp',methods=['GET'])
def get_employee():
    try:
        emp = session.query(Employee).all()
        data_set = {}
        dep = session.query(Department).all()
        c=1
        for e in emp:
            d = {}
            for i in dep:
                if(i.id==e.dept_id):
                    d['department']=i.name
                    d['manager']= i.manager
            
            d['id']=e.id
            d['name'] = e.name
            d['salary'] = e.salary
            d['dept_id']= e.dept_id
            
            data_set[c]=d
            c=c+1
        return data_set    
    except Exception as e:     
        return jsonify({'error':str(e)})    

    

session.close()

if __name__ == '__main__':
    app.run(debug=True)


