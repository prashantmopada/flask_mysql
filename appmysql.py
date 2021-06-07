from flask import Flask, request, jsonify
import mysql.connector as connection
import csv

app = Flask(__name__)

@app.route('/connect_to_db', methods=['POST'])
def establish_mysql_connection():
    if request.method=='POST':
       connection.connect(host="localhost", user="root", passwd="root",use_pure=True)
       return "Welcome hello Mysql"

@app.route('/create_database',methods=['POST'])
def create_database():
    if request.method=='POST':
        my_db=connection.connect(host="localhost", user="root", passwd="root",use_pure=True)
        cursor = my_db.cursor()
        try:
            query = "Create database Test123;"
            cursor.execute(query)
            print("Database Created Successfully")
            my_db.close()
        except Exception as e: print(e)
        return "hello create database"

@app.route('/create_table', methods=['POST'])
def create_table():
    if request.method=='POST':
        my_db=connection.connect(host="localhost", user="root", passwd="root",database ="test123",use_pure=True)
        try:
            query = "CREATE TABLE IF NOT EXISTS carbontubes(Chiral_indice_n int(20),\
                                                            Chiral_indice_m int(20),\
                                                            Initial_atomic_coordinate_u varchar(20),\
                                                            Initial_atomic_coordinate_v varchar(20),\
                                                            Initial_atomic_coordinate_w varchar(20),\
                                                            Calculated_atomic_coordinates_u varchar(20),\
                                                            Calculated_atomic_coordinates_v varchar(20),\
                                                            Calculated_atomic_coordinates_w varchar(20));"
            cursor = my_db.cursor()
            cursor.execute(query)
            print("Table Created. Now You Can insert values into table")
            my_db.close()
        except Exception as e: print(e)
        return "hello create table"

@app.route('/insert_values_table',methods=['POST'])
def insert_values_table():
    if request.method=='POST':
        my_db=connection.connect(host="localhost", user="root", passwd="root",database ="test123",use_pure=True)

        with open('C:/Users/prash/PycharmProjects/flask_mysql/carbon_nanotubes2.csv','r') as data:
            data_csv=csv.reader(data,delimiter=";")
            next(data_csv)

            for row in data_csv:
                query="INSERT INTO carbontubes VALUES({});".format(",".join([f"{val}" for val in row]))
                cursor=my_db.cursor()
                cursor.execute(query)
                my_db.commit()
            print("All values inserted successfully")
        return "hello inserted values"




if __name__ == "__main__":
    app.run(debug=True)

