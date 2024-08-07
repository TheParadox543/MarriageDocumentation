from flask import Flask, render_template

app = Flask(__name__)


JOBS = [
    {
        "id": 1,
        "title": "Data Scientist",
        "location": "Bengaluru",
        "salary": "Rs 80,000",
    },
    {
        "id": 2,
        "title": "Data Analyst",
        "location": "Delhi",
        "salary": "Rs 100,000",
    },
    {
        "id": 3,
        "title": "Backend Developer",
        "location": "New York",
    },
    {
        "id": 4,
        "title": "Frontend",
        "location": "Australia",
        "salary": "Rs 20,000",
    },
]
TEST = {1, 2, 4, 5}


@app.route("/")
def hello_world():
    return render_template("home.html", jobs=JOBS)


@app.route("/app")  # type: ignore
def hello_app():
    return {"Hello World"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
