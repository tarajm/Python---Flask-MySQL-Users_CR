#This is the python file to make classes

from  flask_app.config.mysqlconnection import connectToMySQL
#need to update this statement

#create db = name of server so you don't have to type it over and over again- less opportunity for errors
class User:
    db = "users_schema"
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


#Make a regular function for OOP to address the needs for Show page (full name, email, created/updated)
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


#pLace class methods within the class - otherwise the class method will not execute...it's a function specifc to the class
#this is the READ ALL FILE
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
#i is one row of a user
        for i in results:
            users.append( cls(i) )
        return users

#THIS IS THE SAVE/CREATE METHOD    
    @classmethod
    def save(cls, data):
        #keep on one line
        query = "INSERT INTO users(first_name, last_name, email) VALUES (%(first_name)s, %(last_name)s, %(email)s);"
        #comes back as new row id
        result = connectToMySQL(cls.db).query_db(query,data)
        return result
    
#This is the READ GetONE Method
    @classmethod
    def getOne(cls, data):
        query = "SELECT * FROM users WHERE id=%(id)s;"
        result = connectToMySQL(cls.db).query_db(query, data)  #is it neccessary to have (query, data) or can we just put query?
        return cls(result[0]) #result is a list and we need to call on the first value of the list

#This is the UPDATE Method
#need to ask does the updated_at = NOW() prevent variable injection?
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE id=%(id)s;"
#this line code (above) is coming in from the hidden input on our html form on edit_user
        return connectToMySQL(cls.db).query_db(query, data)



#This is the Delete Method
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM users WHERE id=%(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

