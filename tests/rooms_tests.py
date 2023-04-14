import unittest
from src.guests import Guest
from src.room import Room
from src.songs import Song
from src.functions import *

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room_test = Room("Green Room",1,100)
        self.song1 = Song("Waterloo","ABBA",2.5)
        self.song2 = Song("Intergalactic","Beastie Boys",3)
        # self.guest1 = Guest("Dave",20,[])
        # self.guest2 = Guest("Allan",30,[self.song1])

    def test_has_name(self):
        self.assertEqual("Green Room",self.room_test.name)

    def test_has_capacity(self):
        self.assertEqual(1,self.room_test.capacity)

    def test_has_tab(self):
        self.assertEqual(100,self.room_test.tab)

    def test_has_song_list(self):
        self.assertEqual([],self.room_test.song_list)

    def test_add_song_to_list(self):
        self.room_test.add_song(self.song1)
        result = self.song1 in self.room_test.song_list
        self.assertEqual(True,result)

    def test_check_song_list__true(self):
        self.room_test.add_song(self.song1)
        result = self.room_test.check_song_list(self.song1) 
        self.assertEqual(True,result)

    def test_check_song_list__false(self):
        self.room_test.add_song(self.song1)
        result = self.room_test.check_song_list(self.song2) 
        self.assertEqual(False,result)

    def test_play_song(self):
        self.room_test.add_song(self.song1)
        result = self.room_test.play_song(self.song1)
        self.assertEqual("Waterloo by ABBA is playing.",result)

    def test_increase_tab(self): 
        self.room_test.increase_tab(10) 
        self.assertEqual(110,self.room_test.tab)

    def test_decrease_tab(self): 
        self.room_test.decrease_tab(10) 
        self.assertEqual(90,self.room_test.tab)  

    def test_check_vacancy__pass(self):
        result = self.room_test.check_vacancy()
        self.assertEqual(True,result)

    # def test_check_vacancy__fail(self):
    #     self.guest1.enter_room(self.room_test)
    #     result = self.room_test.check_vacancy()
    #     self.assertEqual(False,result)