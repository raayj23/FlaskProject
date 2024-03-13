from flask import Flask, render_template, request
import pandas
from sklearn.tree import DecisionTreeClassifier

data = pandas.read_csv("animeList.csv")
x = data.drop(columns=["movie"])
y = data["movie"]
model = DecisionTreeClassifier()
model.fit(x.values ,y)


app = Flask(__name__)

@app.route("/", methods=["POST","GET"])

def home():
    action = 0
    comedy = 0
    romance = 0
    adventure = 0

    if request.method == "POST":
        Aaction = request.form["action"]
        Ccomedy = request.form["comedy"]
        Rromance = request.form["romance"]
        Aadventure = request.form["adventure"]

        action = Aaction
        comedy = Ccomedy
        romance = Rromance
        adventure = Aadventure

    predicted_value = model.predict([[action, comedy, romance, adventure]])

    return render_template("index.html" ,firstname=predicted_value[0])


if __name__ == "__main__":
    app.run(debug=True)