from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("animeList.csv")
x = data.drop(columns=["movie"])
y = data["movie"]
model = DecisionTreeClassifier()
model.fit(x.values, y)


app = Flask(__name__)

@app.route("/recommend", methods=["POST"])

def recommend():
    action = 0
    sport = 0
    romance = 0
    adventure = 0

    if request.method == "POST":
        Aaction = request.form["action"]
        Ssport = request.form["sport"]
        Rromance = request.form["romance"]
        Aadventure = request.form["adventure"]

        action = Aaction
        sport = Ssport
        romance = Rromance
        adventure = Aadventure

    predicted_value = model.predict([[action, sport, romance, adventure]])
    return render_template("recommend.html", predicted=predicted_value[0])

@app.route("/", methods=["POST","GET"])
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)