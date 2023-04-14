import unittest
from src.guests import Guest
from src.room import Room
from src.songs import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Waterloo","ABBA",1.5)

    def test_has_title(self):
        self.assertEqual("Waterloo",self.song1.title)

    def test_has_artist(self):
        self.assertEqual("ABBA",self.song1.artist)
