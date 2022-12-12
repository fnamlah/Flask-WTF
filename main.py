from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.secret_key = "-"


class Form(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
    password = PasswordField("What's your password", validators=[DataRequired()])
    submit = SubmitField("Submit")


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/name", methods=["GET", "POST"])
def name_fun():
    name = None
    password = None
    form = Form()
    # Validate
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        password = form.password.data
        form.password.data = ""
    return render_template("name.html", name=name, password=password, form=form)


if __name__ == "__main__":
    app.run(debug=True)