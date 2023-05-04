from flask import Flask, render_template, request
import smtplib
from flask import url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', message='Hello, Flask!')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/trial')
def trial():
    return render_template('trial.html')

@app.route('/contact_me')
def contact_me():
    return render_template('contact_me.html')

@app.route('/send_email', methods=['POST'])
def send_email():
    name = request.form['name']
    email = request.form['email']
    subject = request.form['subject']
    message = request.form['message']

    # Replace the placeholders with your own email address and password
    sender_email = 'a752502113@gmail.com'
    sender_password = 'Celfor2016dse!'
    receiver_email = 'mervynleemh@gmail.com'

    email_body = f'Name: {name}\nEmail: {email}\nSubject: {subject}\nMessage: {message}'

    # Create an SMTP object and connect to Gmail's SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()

    # Log in to your Gmail account
    server.login(sender_email, sender_password)

    # Send the email
    server.sendmail(sender_email, receiver_email, email_body)

    # Close the SMTP connection
    server.quit()

    return 'Email sent!'

if __name__ == '__main__':
    app.run(debug=True)