import unittest
import time
from flask import url_for
from urllib.request import urlopen

from os import getenv
from flask_testing import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from application import app, db, bcrypt
from application.models import Users


test_admin_first_name = "admin"
test_admin_last_name = "admin"
test_admin_email = "admin@email.com"
test_admin_password = "admin2020"
test_name="test song"
test_artist="test artist"
song_name="test song"
song_artist="test artist"


class TestBase(LiveServerTestCase):

    def create_app(self):
        app.config['SQLALCHEMY_DATABASE_URI'] = str(getenv('TEST_DB_URI'))
        app.config['SECRET_KEY'] = getenv('TEST_SECRET_KEY')
        return app

    def setUp(self):
        """Setup the test driver and create test users"""
        print("--------------------------NEXT-TEST----------------------------------------------")
        chrome_options = Options()
        chrome_options.binary_location = "/usr/bin/chromium-browser"
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path="/home/jenkins/chromedriver", chrome_options=chrome_options)
        self.driver.get("http://localhost:5000")
        db.session.commit()
        db.drop_all()
        db.create_all()

    def tearDown(self):
        self.driver.quit()
        print("--------------------------END-OF-TEST----------------------------------------------\n\n\n-------------------------UNIT-AND-SELENIUM-TESTS----------------------------------------------")

    def test_server_is_up_and_running(self):
        response = urlopen("http://localhost:5000")
        self.assertEqual(response.code, 200)



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



class TestRegistration(TestBase):

    def test_registration(self):
        """
        Test that a user can create an account using the registration form
        if all fields are filled out correctly, and that they will be
        redirected to the login page
        """

        # Click register menu link
        self.driver.find_element_by_xpath("/html/body/a[4]").click()
        time.sleep(5)

        # Fill in registration form
        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="first_name"]').send_keys(
            test_admin_first_name)
        self.driver.find_element_by_xpath('//*[@id="last_name"]').send_keys(
            test_admin_last_name)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="confirm_password"]').send_keys(
            test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(5)

        # Assert that browser redirects to login page
        assert url_for('login') in self.driver.current_url

class TestLogin(TestBase):
    def test_login(self):
        """
        Test that a user can log in and be redirected to the songs page
        """

        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="email"]').send_keys(test_admin_email)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(test_admin_password)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(5)

        assert url_for('home') in self.driver.current_url

"""class TestSong(TestBase):
    def test_song(self):
        
        self.driver.find_element_by_xpath('/html/body/a[3]').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="song_name"]').send_keys(song_name)
        self.driver.find_element_by_xpath('//*[@id="song_artist"]').send_keys(song_artist)
        self.driver.find_element_by_xpath('//*[@id="submit"]').click()
        time.sleep(5)

        assert url_for('songs') in self.driver.current_url
"""
class TestPlaylist(TestBase):
    logging_in(self)
    def test_playlist(self):
        self.driver.find_element_by_xpath('/html/body/a[4]').click()
        time.sleep(5)

        self.driver.find_element_by_xpath('//*[@id="title"]').send_keys(test_playlist)
        self.driver.find_element_by_xpath('//*[@id="content1"]').send_keys(test_song)
        self.driver.find_element_by_xpath('//*[@id="content2"]').send_keys(test_song)
        self.driver.find_element_by_xpath('//*[@id="content3"]').send_keys(test_song)

        self.driver.find_element_by_xpath('//*[@id="submit"').click()
        time.sleep(5)

        assert url_for('home') in self.driver.current_url


if __name__ == '__main__':
    unittest.main(port=5000)
