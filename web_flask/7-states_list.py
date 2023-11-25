#!/usr/bin/python3
"""
python flask script
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_data(self):
    """
    refresh
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Retrieves data"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
