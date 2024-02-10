from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, session
from flask import render_template
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import rainbow

import warnings
warnings.filterwarnings('ignore')

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.neighbors import KNeighborsClassifier

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
#################################################
# Flask Routes
#################################################

@app.route("/")
def index():
    return render_template('index.html')
	
@app.route('/homepage', methods =['GET', 'POST'])
def homepage():
    return render_template('index.html')
	
@app.route('/classification', methods =['GET', 'POST'])
def classification():
    return render_template('classification.html')

@app.route('/graph', methods =['GET', 'POST'])
def graph():
    return render_template('graph.html')
    
if __name__ == "__main__":
    app.run(debug=True)