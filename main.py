from flask import Flask, render_template, request
import random

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/check", methods=["POST"])
def check_eligibility():
    is_registered = "registration" in request.form
    has_medical = "medical" in request.form
    grade = int(request.form["grade"])

    # Conditions
    if not is_registered:
        return "Not Eligible: Please register online first."

    if not has_medical:
        return "Not Eligible: Please secure a medical clearance."

    if grade < 7 or grade > 10:
        return "Not Eligible: Only students in Grades 7 to 10 can join Intramurals."

    # If eligible
    teams = ["Blue Bears", "Red Bulldogs", "Yellow Tigers", "Green Hornets"]
    assigned_team = random.choice(teams)

    return f"""
 Congratulations! You are eligible to join the Intramurals.</h2>
 Your assigned team is: {assigned_team}</h3>
    """

if __name__ == "__main__":
    app.run(debug=True)
