from flask import Flask

# Create application object
app = Flask(__name__)

# Use decorator to link the view function to a URL
@app.route("/")
@app.route("/hello")

# Define the view using a function, which returns a string
def hello_world():
    return "Hello, World!"

# Start development server using the run() method
if __name__ == "__main__":
    app.run()

