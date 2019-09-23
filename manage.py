from app import create_app,db
from flask_script import Manager,Server
from app.models import *

# Creating app instance
app = create_app('development')
app = create_app('production')


# Create manager instance 
manager = Manager(app)


@manager.shell
def make_shell_context():
    return dict( app=app, db=db, User=User, Pitch = Pitch)


if __name__ == '__main__':
    manager.run()


