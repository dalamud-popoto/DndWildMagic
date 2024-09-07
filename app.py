from flask import Flask, render_template,request
import random
from utils.wild_magic_utils import roll_dice


# python -m flask run
app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():

    job = request.form.get("job_table")
    print(job)
    if job is None:
        data = {'dice': '', 'magic_effect': '', 'job':''}
    else:
        data = roll_dice(job)
    return render_template("home.html",**data)

if __name__ == "__main__":
    # app.run(debug=True)
    app.run()