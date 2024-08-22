# Import flask so we can serve the webpage and a few other things for the backend
from flask import Flask, request, jsonify, render_template, request, redirect, url_for
# Import my contactHandler class
from contact import contactHandler

app = Flask(__name__)

# this is the admin key to check all the contacts. ?key=
ACCESS_KEY = 'C0D3N4T10N'

# Init our contactHandler with a file
contact_handler = contactHandler('contacts.csv')

# render our index page
@app.route('/')
def index():
    return render_template('index.html')

# render our contact page and also handle a post request for the contact form
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # take the form payload and assign it some variables
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']
        
        # using the contact handler to write a contact to file
        contact_handler.write_contact([name, email, subject, message])
        
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

# render the admin page and check if we have a ?key arg
@app.route('/admin')
def admin():
    # take the key arg and check if is the correct key
    # if not return 403 and show a error
    # could work this into error pages but for now its ok
    access_key = request.args.get('key')
    if access_key != ACCESS_KEY:
        return "Unauthorized", 403

    # using the contact handler to read all contacts from the file
    contacts = contact_handler.read_contacts()
    
    return render_template('admin.html', contacts=contacts)

if __name__ == '__main__':
    app.run(debug=True)
