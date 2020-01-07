from flask import Flask, render_template
import numpy as np
from random import randint

app = Flask(__name__)


def dice_roll():
    blob = []
    for i in range(3):
        num = randint(1,6)
        blob.append("Die roll = " + str(num))
    return str(blob)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/which-side-of-the-force')
def force():
    return "The dark side"


@app.route('/dice')
def dice():
    return render_template('roll-dice.html',dice_roll=dice_roll())


#def repeat_dice():
  #  for x in range(5):
  #      return dice()
        

