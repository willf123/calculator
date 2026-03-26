from flask import Flask, render_template, request

app = Flask(__name__)

# This is the home page route.
# When you visit localhost:5000 in your browser, this function runs.
@app.route("/")
def home():
    return render_template("index.html", result="")

# This route handles the form submission when you click a button.
@app.route("/calculate", methods=["POST"])
def calculate():
    try:
        expression = request.form["expression"]
        result = eval(expression)
    except:
        result = "Error"
    return render_template("index.html", result=result)

# Start the server
if __name__ == "__main__":
    app.run(debug=True)
