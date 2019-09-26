from app.models import Pitch, User
from app import db



class PitchTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Movie class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''

        self.user_ines = User(username = 'ines', password = 'best', email = 'uwaseines7@gmail.com')
        
        self.new_pitch = Pitch(id=1,pitch_title="First Pitch", descriptiont='No pain without Gain',category='Motivation')

    def tearDown(self):
        Pitch.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEquals(self.new_pitch.id,1)
        self.assertEquals(self.new_pitch.pitch_title,'First Pitch')
        self.assertEquals(self.new_pitch.description,'No pain without Gain')
        self.assertEquals(self.new_pitch.category,"Motivation")
        

    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertTrue(len(Pitch.query.all())>0)

    def test_get_pitch_by_id(self):

        self.new_pitch.save_pitch()
        got_pitches = Pitch.get_pitch(1)
        self.assertTrue(len(got_pitches) == 1)
