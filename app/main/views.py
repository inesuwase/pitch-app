from flask import render_template,request,redirect,url_for,abort, flash
from . import main
from flask_login import login_required, current_user
from ..models import Pitch, User
from .forms import PitchForm
from flask.views import View,MethodView
from .. import db
import markdown2


# Views
@main.route('/', methods = ['GET','POST'])
def index():

    '''
    View root function that gives index page and its data
    '''
    pitch = Pitch.query.filter_by().first()
    title = 'Home'
    motivationpitch = Pitch.query.filter_by(category = "motivationpitch")
    interviewpitch = Pitch.query.filter_by(category = "interviewpitch")
    pickuplines = Pitch.query.filter_by(category = "pickuplines")

    

    return render_template('home.html', title = title, pitch = pitch, motivationpitch= motivationpitch, interviewpitch= interviewpitch, pickuplines = pickuplines)
    




@main.route('/pitches/new/', methods = ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    if form.validate_on_submit():
        description = form.description.data
        title = form.title.data
        owner_id = current_user
        category = form.category.data
        print(current_user._get_current_object().id)
        new_pitch = Pitch(owner_id =current_user._get_current_object().id, title = title,description=description,category=category)
        db.session.add(new_pitch)
        db.session.commit()
        
        
        return redirect(url_for('main.index'))
    return render_template('pitches.html',form=form)