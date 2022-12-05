from flask import Flask, render_template, request, redirect

from users import User


app = Flask(__name__)    


@app.route('/')          
def index():
    return redirect('/users')  


@app.route('/users')
def users():
    return render_template("users.html", users=User.get_all())



@app.route('/user/new')
def new():
    return render_template("new_user.html")

#CREATE ROUTE
@app.route('/user/create', methods=['POST'])
def create():
    print(request.form)
    User.save(request.form)
    return redirect('/users')

#EDIT ROUTE
@app.route('/user/edit/<int:id>') #bring in the id
def edit(id):
    #need to create data object/dictionary
    data = {
        "id":id
    }
    return render_template("edit_user.html",user=User.getOne(data)) 
#this says users is = to teh class of User and pull all this information from the form
#now if you go to the /user s page...you will see a new columb (Actions) and when you hover over the button "Update" at the bottom of the screen you will see the variable of the id being 
#passed through  localhost:5000/users/3 (the third entry in your database)
#when you click on upate it will bring you to user/update/(ID) and it has all the form fields populated so you can edit the information


#UPDATE ROUTE
#this is the route we use when a user updates their information to send to the DB To be updated
@app.route('/user/update', methods=['POST'])
def update():
#take the udpated information from teh user (request.form) and pass that in to the class User via update
    User.update(request.form)
#then take us back to the page where it lists all teh users and their information stored in the db
    return redirect('/users')


#DELETE ROUTE
@app.route('/user/delete/<int:id>')
def delete(id):
    data = {
        'id':id
    }
    User.delete(data)
#after we delete the data we rediect to the user page to show the deleted entry no longer exists
    return redirect('/users')


#Show is going to be similar to the app.route - EDIT
@app.route('/user/show/<int:id>') #bring in the id
def show(id):
    #need to create data object/dictionary
    data = {
        "id":id
    }
    return render_template("show_user.html",user=User.getOne(data)) 





if __name__=="__main__":     
    app.run(debug=True)    

