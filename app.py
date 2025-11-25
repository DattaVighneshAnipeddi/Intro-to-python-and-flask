from flask import Flask

# Create a Flask application
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return "Welcome to my first Flask Web Server! 🎉"

# About route
@app.route('/about')
def about():
    return "This is the About Page 👀"

# Contact route
@app.route('/contact')
def contact():
    return "Contact us at: info@example.com 📩"

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
