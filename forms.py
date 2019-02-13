from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, \
    BooleanField, SelectField
from wtforms.validators import InputRequired, Email, URL, Length, EqualTo


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password', validators=[InputRequired(),
                                                     Length(min=6)])
    # add remember me later


class RegistrationForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email()])
    password = PasswordField('password',
                             validators=[InputRequired(),
                                         Length(min=6),
                                         EqualTo('confirm_password')])
    confirm_password = PasswordField('confirm_password')


class CreateJobForm(FlaskForm):
    title = StringField('job_title', validators=[InputRequired()])
    job_location = StringField('job_location', validators=[InputRequired()])
    job_type = SelectField('Job Type', choices=[('part_time', 'Part Time'),
                                                ('full_time', 'Full Time'),
                                                ('contract', 'Contract')],
                           validators=[InputRequired()])
    job_description = TextAreaField('job_description',
                                    validators=[InputRequired()])
    link_to_apply = StringField('link_to_apply', validators=[InputRequired(),
                                                             URL()])
    company_name = StringField('company_name', validators=[InputRequired()])
    company_location = StringField('company_location',
                                   validators=[InputRequired()])
    company_website = StringField('company_website',
                                  validators=[InputRequired(), URL()])
    remote = BooleanField('remote', validators=[InputRequired()])


class JobSearchForm(FlaskForm):
    query = StringField('query', validators=[InputRequired()])
    job_type = SelectField('Job Type', choices=[('part_time', 'Part Time'),
                                                ('full_time', 'Full Time'),
                                                ('contract', 'Contract'),
                                                ('any', 'Any')],
                           validators=[InputRequired()])
    remote = BooleanField('remote', validators=[InputRequired()])


class PasswordResetForm(FlaskForm):
    password = PasswordField('password',
                             validators=[InputRequired(),
                                         Length(min=6),
                                         EqualTo('confirm_password')])
    confirm_password = PasswordField('confirm_password')
