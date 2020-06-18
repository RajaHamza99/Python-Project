from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Users, Playlists, Songs
from flask_login import current_user


from flask_login import current_user

class UpdateAccountForm(FlaskForm):
    first_name = StringField('First Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    last_name = StringField('Last Name',
        validators=[
            DataRequired(),
            Length(min=4, max=30)
        ])
    email = StringField('Email',
        validators=[
            DataRequired(),
            Email()
        ])
    submit = SubmitField('Update')

    def validate_email(self,email):
        if email.data != current_user.email:
            user = Users.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already in use')

class UpdatePlaylistForm(FlaskForm):
    title = StringField('Title',
            validators=[
                DataRequired(),
                Length(min=4, max=100)
            ])
    content1 = SelectField(u'Song 1', coerce=int, choices=[])
    content2 = SelectField(u'Song 2', coerce=int, choices=[])
    content3 = SelectField(u'Song 3', coerce=int, choices=[])

    submit = SubmitField('Update')
            

            
class SongsForm(FlaskForm):
    song_name = StringField('Song name: ',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )

    song_artist = StringField('Song Artist: ',
            validators=[
                DataRequired(),
                Length(min=4, max=100)
            ]
    )
    
    submit = SubmitField('Add song')


class PlaylistForm(FlaskForm):
    title = StringField('Title',
            validators = [
                DataRequired(),
                Length(min=4, max=100)
            ]
    )
    content1 = SelectField(u'Song 1', coerce=int, choices=[])
    content2 = SelectField(u'Song 2', coerce=int, choices=[])
    content3 = SelectField(u'Song 3', coerce=int, choices=[])

    submit = SubmitField('Post Content')


class RegistrationForm(FlaskForm):
    first_name = StringField('First Name',
                    validators=[
                        DataRequired(),
                        Length(min=2, max=30)
            ]
     )
    
    last_name = StringField('Last Name',
                validators=[
                    DataRequired(),
                    Length(min=3, max=30)
            ]
                
    )
    email = StringField('Email',
        validators = [
            DataRequired(),
            Email()
        ]
    )
    password = PasswordField('Password',
        validators = [
            DataRequired(),
        ]
    )
    confirm_password = PasswordField('Confirm Password',
        validators = [
            DataRequired(),
            EqualTo('password')
        ]
    )
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()

        if user:
            raise ValidationError('Email already in use')


class LoginForm(FlaskForm):
    email = StringField('Email',
            validators=[
                DataRequired(),
                Email()
            ]
    )

    password = PasswordField('Password',
            validators=[
                DataRequired()
            ]
    )

    remember = BooleanField('Remember Me')
    submit = SubmitField ('Login')
