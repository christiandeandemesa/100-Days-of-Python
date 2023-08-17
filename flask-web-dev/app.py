from flask import Flask
# Creates a Flask app.
app = Flask(__name__)

# Defines the route.
@app.route("/")
# Executes the function with the associated route.
def home():
    return "Hello, Flask!"

@app.route("/bye")
def bye():
    return "Bye, Flask!"

# If the script is being run directly, run the Flask app.
if __name__ == "__main__":
    app.run()