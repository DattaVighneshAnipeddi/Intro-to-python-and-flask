from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    print("Home route was called!")  # This will print in the terminal
    return "Welcome to my first Flask Web Server! 🎉"

@app.route('/about')
def about():
    print("About route was called!")
    return "This is the About Page 👀"

@app.route('/contact')
def contact():
    print("Contact route was called!")
    return "Contact us at: info@example.com 📩"

if __name__ == '__main__':
    print("Starting Flask server...") 
    app.run(debug=True)

