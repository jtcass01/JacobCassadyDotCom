# Import 3rd party modules
from flask import Flask

# Create app instance of Flask
app = Flask(__name__)

# Define functions mapped to each route
@app.route('/')
def home():
    return "Hey there!"

# Run App
if __name__ == "__main__":
    app.run(debug=True)
