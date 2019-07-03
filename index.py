from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from flask import request
import os
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
saved_image = 'static/generated_images'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    #types of planes
    plane_types = SelectField(u'Plane Types', choices=[('boeing', 'BOEING'), ('airbus', 'AirBus')], default='boeing')
    #init_weights
    init_weights = SelectField(u'Initial Weights', choices=[('5k', '5000'), ('10k', '10000')], default='5k')
    #departure locations
    depart_locations = SelectField(u'Departure Locations', choices=[('ls', 'Los Angeles'), ('sf', 'San Francisco')], default='sf')
    #arrival locations
    arr_locations = SelectField(u'Arrival Locations', choices=[('bt', 'Boston'), ('dt', 'Detroit')], default='bt')
    submit = SubmitField('Generate Plan')


@app.errorhandler(404)
def page_not_found():
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.route('/', methods=['GET', 'POST'])
def index():
    form = NameForm()
    if request.method == 'GET':
        return render_template('index.html', form=form)
    if request.method == 'POST':
        imagePath = {}
        # imagePath['alt'] = os.path.join(saved_image, 'altitude')
        imagePath['alt'] = saved_image + '/altitude.png'
        imagePath['gamma'] = saved_image + '/gamma.png'
        imagePath['psi'] = saved_image + '/psi.png'
        imagePath['route'] = saved_image + '/route.png'
        imagePath['speed'] = saved_image + '/speed.png'
        imagePath['thrust_force'] = saved_image + '/thrust_force.png'
        return render_template('index.html', form=form, postRequest=True, imagePath=imagePath)



if __name__ == "__main__":
    app.run(debug=True, use_debugger=True, use_reloader=False, passthrough_errors=True)



