from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField,BooleanField,SubmitField,TextAreaField,RadioField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError



class PitchForm(FlaskForm):
	title = StringField('Title', validators=[Required()])
	description = TextAreaField("What would you like to pitch ?",validators=[Required()])
	category = RadioField('Label', choices=[ ('motivationpitch','motivationpitch'), ('interviewpitch','interviewpitch'),('pickuplines','pickuplines')],validators=[Required()])
	submit = SubmitField('Submit')
class CommentForm(FlaskForm):
	description = TextAreaField('write a comment',validators=[Required()])
	submit = SubmitField()

class UpvoteForm(FlaskForm):
	submit = SubmitField()


class Downvote(FlaskForm):
    submit = SubmitField()
