# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def me():

    name = "Aadam" # write your name
    age = "14" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage
@app.route("/father")
def dad():

    name = "Jonathan" # write your name
    age = "59" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to mother webpage


# define the route to friends webpage
@app.route("/mother")
def mum():

    name = "Yasmin" # write your name
    age = "47" # write your age

    return render_template('index.html' , name = name , age = age)

# add other routes, if you want
@app.route("/brother")
def brother():

    name = "Ismael" # write your name
    age = "12" # write your age

    return render_template('index.html' , name = name , age = age)



# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
