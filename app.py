from flask import Flask

# Create application object
app = Flask(__name__)
app.config['DEBUG'] = True

# Use decorator to link the view function to a URL
@app.route("/")
@app.route("/hello")
def hello_world():
    return "Hello, World!"

# Dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

@app.route("/integer/<int:value>")
def int_type(value):
    print(value + 1)
    return "correct"

@app.route("/float/<float:value>")
def float_type(value):
    print(value + 1)
    return 'correct'

@app.route("/path/<path:value>")
def path_type(value):
    print(value)
    return 'correct'

@app.route("/name/<name>")
def index(name):
    if name.lower() == 'michael':
        return "Hello, {}".format(name)
    else:
        return "Not Found", 404


# Start development server using the run() method
if __name__ == "__main__":
    app.run()

