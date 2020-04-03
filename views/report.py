# facebook/views/profile.py

from flask import Blueprint, render_template

report = Blueprint('report', __name__)


@report.route('/report')
def timeline():
    # Do some stuff
    return 'Local Report'
