from flask import Flask, request
import os
import jinja2
import cgi

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir),autoescape=True)

app= Flask(__name__)
app.config['DEBUG']=True



@app.route('/')
def index():
    template = jinja_env.get_template('info-form.html')
    return template.render(title='Log-in')


@app.route('/validate', methods=["POST"])
def validate():
    username = ''
    password_one = ''
    password_two = ''
    email = ''
    username_error = ''
    password_error = ''
    email_error = ''
    password_length_error = ''
    username_space_error = ''

    template = jinja_env.get_template('info-form.html')
    username_new = request.form['username']
    password_one_new = request.form['password_one']
    password_two_new = request.form['password_two']
    email_name = request.form['email']

    if password_one_new == password_two_new:
        password_error = ""
    else:
        password_error = "passwords do not match"


    if len(password_one_new) >= 3 and len(password_one_new) <= 20:
        password_error = ""
    else:
        password_error = "password not valid"


    if len(username) > 3 or len(username) < 20:
        username_error = ''
    else:
        username_error = 'username not valid'
    
    
    if " " in username:
        username_error = 'username not valid'

    if "@" not in email_name or "." not in email_name:
        email_error = 'email not valid'
    






    return template.render(title="login", password_error = password_error, password_length_error = password_length_error,
    username_error = username_error, username_space_error = username_space_error, email_error = email_error)
    
#@app.route('/', methods=["GET"])
#def success():
    #template = jinja_env.get_template('thank-you.html')
    #return template.render(title="thank you")

#def username_error():
    #username = request.form['username']
    
    #if len(username) < 3 or len(username) > 20:
        #template = jinja_env.get_template('info-form-two.html')
        #return template.render(title='Log-in error')
    #else:
        #template = jinja_env.get_template('thank-you.html')
        #return template.render(title="thank-you")

        
        


app.run()