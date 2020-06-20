import unittest

from flask import url_for
from flask_testing import TestCase

from application import app, db, bcrypt
from application.models import Users, Playlists, Songs
from os import getenv

class TestBase(TestCase):

    def create_app(self):

        # pass in configurations for test database
        config_name = 'testing'
        app.config.update(SQLALCHEMY_DATABASE_URI=getenv('TEST_DB_URI'),
                SECRET_KEY=getenv('TEST_SECRET_KEY'),
                WTF_CSRF_ENABLED=False,
                DEBUG=True
                )
        return app

    def setUp(self):
        """
        Will be called before every test
        """
        # ensure there is no data in the test database when the test starts
        db.session.commit()
        db.drop_all()
        db.create_all()

        # create test admin user
        hashed_pw = bcrypt.generate_password_hash('admin2016')
        admin = Users(first_name="admin", last_name="admin", email="admin@admin.com", password=hashed_pw)

        # create test non-admin user
        hashed_pw_2 = bcrypt.generate_password_hash('test2016')
        employee = Users(first_name="test", last_name="user", email="test@user.com", password=hashed_pw_2)

        song = Songs(title = "test song", artist = "test artist")
        
        # save users to database
        db.session.add(admin)
        db.session.add(employee)
        db.session.add(song)
        db.session.commit()
        


    def tearDown(self):
        """
        Will be called after every test
        """

        db.session.remove()
        db.drop_all()




def logging_in(self):
    response =  self.client.post(
          '/login',
            data=dict(
                   email = "admin@admin.com",
                    password = "admin2016",               
                    ),
            follow_redirects=True
             )
    return response

def logging_out(self):
    response = self.client.get(
            '/logout',)
    return response

class TestViews(TestBase):

    def test_homepage_view(self):
        """
        Test that homepage is accessible without login
        """
        self.assertEqual(self.client.get(url_for('home')).status_code, 200)

    def test_login(self):
        self.assertEqual(self.client.get(url_for('login')).status_code, 200)

    def test_about(self):
        self.assertEqual(self.client.get(url_for('about')).status_code, 200)

    def test_register(self):
        self.assertEqual(self.client.get(url_for('register')).status_code, 200)

    def test_songs(self):
        logging_in(self)
        self.assertEqual(self.client.get(url_for('add_songs')).status_code, 200)

    def test_playlist(self):
        logging_in(self)
        self.assertEqual(self.client.get(url_for('playlist')).status_code, 200)
    

    def test_account(self):
        logging_in(self)
        self.assertEqual(self.client.get(url_for('account')).status_code, 200)

        
class TestRegistration(TestBase):

    def test_registration(self):
        """
        Test that when I register a new user, it redirects me to the login page
        """
        with self.client:
            logging_out(self)
            response = self.client.post(
                    '/register',
                    data = dict(
                        first_name="testfirst",
                        last_name="testsur",
                        email="test@test.com",
                        password="test123",
                        ),
                    follow_redirects=True
                    )
            self.assertIn(b'testfirst', response.data)
            self.assertIn(b'testsur', response.data)
            self.assertIn(b'test@test.com', response.data)


class TestLogin(TestBase):
    def test_Login(self):
        """
        test that logging in redirects me to the songs page
        """
        with self.client:
            logging_out(self)
            response = self.client.post(
                    '/login',
                    data = dict(
                        email="admin@admin.com",
                        password = "admin2016",
                        ),
                    follow_redirects=True
                    )
            return response
        self.assertIn(b'admin@admin.com', response.data)
        self.assertIn(b'admin2016', response.data)

class TestPlaylist(TestBase):

    def test_playlist(self):
        """
        Test that a user can create a playlist
        """
        with self.client:
            logging_in(self)
            response = self.client.post(
                    '/playlist',
                    data = dict(
                        title="test playlist",
                        songs_id="test song",
                        songs_id2="test song",
                        songs_id3="test song",
                        ),
                    follow_redirects=True
                    )
        self.assertIn(b'test playlist', response.data)
        self.assertIn(b'test song', response.data)
        self.assertIn(b'test song', response.data)
        self.assertIn(b'test song', response.data)



#class TestSong(TestBase):
 #   def test_song(self):
  #      """
   #     test a user can create songs
    #    """
     #   with self.client:
      #      logging_in(self)
       #     response = self.client.post(
        #            '/songs',
         #           data=dict(
          #              title = "test song title",
           #             artist = "test artist",
            #            ),
             #       follow_redirects=True
              #      )
            #return response
        #self.assertIn(b'test song title', response.data)
        #self.assertIn(b'test artist', response.data)

"""class TestSongs(TestBase):
    def test_add_song(self):
        with self.client:
            response = self.client.post(
                    '/login',
                    data=dict(
                        email="admin@admin.com",
                        password="admin2016"
                        ),
                    follow_redirects=True
                    )
            self.assertEqual(response.status_code, 200)
            responsetwo = self.client.post(url_for('playlist', playlists_id=1), data=dict(title="test song", artist="test artist"))
            self.assertIn(b'test song', responsetwo.data)
"""
class TestUpdate(TestBase):
    def test_account(self):
        """
        test a user can update their account
        """
        with self.client:
            logging_in(self)
            response = self.client.post(
                    '/account',
                    data=dict(
                        first_name="test",
                        last_name="test",
                        email="test@test.com",
                        ),
                    follow_redirects=True
                    )
            return response
        self.assertIn(b'test', response.data)
        self.assertIn(b'test', response.data)
        self.assertIn(b'test@test.com', response.data)
