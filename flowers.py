import os
from flask import Flask, render_template, flash, redirect
from src.forms import AddForm, InferForm

app = Flask(__name__)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/train")
def train():
    return render_template("train.html")


@app.route("/add", methods=['GET', 'POST'])
def add():
    form = AddForm()
    if form.validate_on_submit():
        flash('Adding <{},{}>'.format(
            form.x.data, form.y.data))
        return redirect("/")
    return render_template('add.html', title='Add Data', form=form)


@app.route("/list")
def list():
    return render_template("list.html")


@app.route("/infer", methods=['GET', 'POST'])
def infer():
    form = InferForm()
    if form.validate_on_submit():
        flash('Getting <{}>'.format(
            form.x.data))
        return redirect("/")
    return render_template('infer.html', title='Infer Data', form=form)
