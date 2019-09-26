from app import create_app,db
from flask_script import Manager,Server
from  flask_migrate import Migrate, MigrateCommand
from app.models import User,Pitch,Comment,Upvote,Downvote

# Creating app instance
# app = create_app('development')
app = create_app('production')


# Create manager instance 
manager = Manager(app)
migrate = Migrate(app,db)
manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)


@manager.shell
def make_shell_context():
    return dict( app=app, db=db, User=User, Pitch = Pitch,Comment = comment,Upvote = upvote,Downvote = downvote)


@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()



