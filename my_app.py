from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message
import os

app = Flask(__name__)

# Retrieve the API key and port from environment variables
GOOGLE_API_KEY = os.getenv("AIzaSyC34XpHsl-avtNInQ2w7Lgqc72S15KdCpI")

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ramenjanahary129@gmail.com'  # Your email
app.config['MAIL_PASSWORD'] = 'xqyx bkvc dwdr xbtv'          # Your password
app.config['MAIL_DEFAULT_SENDER'] = 'ramenjanahary129@gmail.com'

mail = Mail(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Send registration notification to admin (your email)
        msg = Message(subject='New Registration',
                      recipients=['ramenjanahary129@gmail.com'],  # Admin email
                      body=f'New registration: {name}, {email}, Message: {message}')
        mail.send(msg)

        # Send welcome email to the new user
        welcome_msg = Message(subject='Welcome to PTC #POLYGOT TRAINING CENTER',
                              recipients=[email])  # New user's email
        welcome_msg.body = f'Dear {name},\n\nWelcome to PTC #POLYGOT TRAINING CENTER!\nWe\'re excited to have you onboard.'
        mail.send(welcome_msg)

        return redirect(url_for('thank_you'))

    return render_template('index.html')

@app.route('/thank_you')
def thank_you():
    return '<h1>Thank you for registering! A welcome email has been sent to you.</h1>'

if __name__ == '__main__':
    # Use the PORT environment variable or default to 5000 for local testing
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
