
import sqlite3
from sqlite3 import Error
import os

# Import date class from datetime module
from datetime import date, datetime

current_path = os.path.dirname(os.path.realpath(__file__))
dbpath = current_path + "/data/calorietracker_db.sqlite3"

class sqllitecalls():
    def __init__(self):
        # establish SQL Connection
        self.sqlcursor()
                
        sql = "Select user_id, first_name, last_name from user;"
        self.cursor.execute(sql)
        fetch= self.cursor.fetchall()
     
    def getcalorietrackerdata(self, mealid, dt_entry=date.today()):
        sql = "Select meal_id, meal_date, calories from calorie_tracker where meal_date=? and meal_id=?;"
        self.cursor.execute(sql,(dt_entry, mealid))
        fetch= self.cursor.fetchall()
        if len(fetch)==0:
            #insert data since data does not exist
            self.insert_calories(dt_entry=dt_entry)
        else:
            print(fetch)
            fmt= "{0},{1},{2}"
            for row in fetch:  
                print(row)
                meal_id, meal_date, calories = row

            return meal_id, meal_date, calories
    
    def updatecalories(self):
        pass
    
    def insert_calories(self, dt_entry=date.today(), bfast_cals = 0, lunch_cals = 0, din_cals = 0, snack_cals = 0):
        # establish SQL Connection
        self.sqlcursor()
        print(dt_entry)
        # populates data in the calorietracker table        
        sql = """insert into calorie_tracker (user_id, meal_id, meal_date, calories) VALUES(?,?,?,?)"""
        self.cursor.execute(sql,(1,1,dt_entry,bfast_cals))
        self.cursor.execute('commit;') 
        
        sql = """insert into calorie_tracker (user_id, meal_id, meal_date, calories) VALUES(?,?,?,?)"""
        self.cursor.execute(sql,(1,2,dt_entry,lunch_cals))
        self.cursor.execute('commit;')        
        
        sql = """insert into calorie_tracker (user_id, meal_id, meal_date, calories) VALUES(?,?,?,?)"""
        self.cursor.execute(sql,(1,3,dt_entry,din_cals))
        self.cursor.execute('commit;')             
         
        sql = """insert into calorie_tracker (user_id, meal_id, meal_date, calories) VALUES(?,?,?,?)"""
        self.cursor.execute(sql,(1,4,dt_entry,snack_cals))
        self.cursor.execute('commit;') 

    def getuser(self):
        sql = "Select first_name, last_name from user;"
        #passing the query to the cursor function
        self.cursor.execute(sql)
        fetch= self.cursor.fetchall()
        print(fetch)
        fmt= "{0},{1}"
        for row in fetch:  
            first_name, last_name = row

        return first_name, last_name

    def updateuser(self, fname, lname):
        sql = """UPDATE user
                set first_name = ?,
                last_name = ?"""
        self.cursor.execute(sql, (fname, lname))
        self.cursor.execute('commit;')
        self.cursor.close
    
    def sqlcursor(self):
        self.cursor = sqlite3.connect(dbpath).cursor()
    
    def get_cursor(self):
        conn = sqllite3.connect(dbpath).cursor()
        return conn.cursor()


# establish SQL Connection
# current_path = os.path.dirname(os.path.realpath(__file__))
# dbpath = current_path + "/data/calorietracker_db.sqlite3"

# connection = sqlite3.connect(dbpath)

# cursor= connection.cursor() 

# # sql = "drop table calorie_tracker; "
# sql = "select * from calorie_tracker;"

# cursor.execute(sql)

# fetch= cursor.fetchall()
# print(fetch)

#sql = """insert into calorie_tracker (user_id, meal_id, meal_date, calories) VALUES(?,?,?,?)"""

# cursor.execute("CREATE TABLE calorie_tracker (user_id INTEGER NOT NULL, meal_id integer NOT NULL ,meal_date date NOT NULL, calories INTEGER, PRIMARY KEY(user_id, meal_id, meal_date));")
# cursor.execute('commit;')

# #creating the database and preloading the database tables that won't change

# cursor.execute("CREATE TABLE calorie_tracker (user_id INTEGER NOT NULL, meal_id integer NOT NULL ,meal_date date NOT NULL, calories INTEGER);")


# cursor.execute("create unique index UX_calorie_tracker on calorie_tracker(user_id, meal_id, meal_date)")
# cursor.close


# cursor.execute("CREATE TABLE user (user_id INTEGER PRIMARY KEY,	first_name TEXT NOT NULL,	last_name TEXT NOT NULL);")
# cursor.execute("CREATE TABLE meals (meal_id INTEGER PRIMARY Key, meal_name TEXT Not Null, meal_definition TEXT);")

# populates data in the meals table
# mylist = ('Breakfast', 'Lunch', 'Dinner', 'Snack')
# for item in mylist:
#        cursor.execute("Insert into meals (meal_name) values(?)",(item,))  
#        cursor.execute('commit;')
# cursor.close

#Populate the user table
# cursor.execute("Insert into user (first_name, last_name) values(?,?)",('First Name','Last Name'))  
# cursor.execute('commit;')
# cursor.close

# cursor.execute("")
# cursor.execute("")
        