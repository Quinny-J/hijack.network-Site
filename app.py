# Import flask so we can serve the webpage and a few other things for the backend
from flask import Flask, request, jsonify, render_template, request, redirect, url_for
from views import hijack_network
# Import my contactHandler class
from contact import contactHandler

app = Flask(__name__)
app.register_blueprint(hijack_network)

# this is the admin key to check all the contacts. ?key=
ACCESS_KEY = 'C0D3N4T10N'

# Init our contactHandler with a file
contact_handler = contactHandler('contacts.csv')

if __name__ == '__main__':
    app.run(debug=True)
