from flask import Flask, render_template, request
import os

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/report", methods=["POST"])
def report():

    name = request.form["name"]
    age = request.form["age"]
    location = request.form["location"]
    phone = request.form["phone"]

    image = request.files["photo"]

    if image:
        image.save(os.path.join(UPLOAD_FOLDER, image.filename))

    return f"""
    <h2>Report Submitted Successfully</h2>

    <p><b>Name:</b> {name}</p>
    <p><b>Age:</b> {age}</p>
    <p><b>Last Seen:</b> {location}</p>
    <p><b>Phone:</b> {phone}</p>

    <a href="/">Back</a>
    """

if __name__ == "__main__":
    app.run(debug=True)