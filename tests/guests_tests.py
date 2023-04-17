import unittest
from src.guests import Guest
from src.room import Room
from src.songs import Song

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.song1 = Song("Waterloo","ABBA",2.5)
        self.song2 = Song("Waterloo Sunset","The Kinks",3)
        self.room1 = Room("Green Room",5,50)
        self.guest1 = Guest("Dave",20,[])
        self.guest2 = Guest("Allan",30,[self.song1])
        self.room1.add_song(self.song1)

    def test_has_name(self):
        self.assertEqual("Dave",self.guest1.name)
        
    def test_has_wallet(self):
        self.assertEqual(20,self.guest1.wallet)
    
    def test_has_favourite_song__true(self):
        self.assertEqual(0,len(self.guest1.favourite_songs))
 
    def test_has_favourite_song__false(self):
        self.assertEqual(1,len(self.guest2.favourite_songs))

    def test_enter_room(self):
        self.guest1.enter_room(self.room1)
        result = len(self.room1.guest_list)
        self.assertEqual(1,result)

    def test_leave_room(self):
        self.guest1.enter_room(self.room1)
        self.guest1.leave_room()
        result = len(self.room1.guest_list)
        self.assertEqual(0,result)

    def test_choose_song__pass(self):
        self.guest1.enter_room(self.room1)
        result = self.guest1.choose_song(self.song1)
        self.assertEqual("Waterloo by ABBA is playing.",result)
    
    def test_choose_song__fail(self):
        self.guest1.enter_room(self.room1)
        result = self.guest1.choose_song(self.song2)
        self.assertEqual("Please choose a song in the song list.",result)

    def test_decrease_wallet(self):
        self.guest1.decrease_wallet(10)
        self.assertEqual(10,self.guest1.wallet)

    def test_pay_bill(self):
        self.guest1.enter_room(self.room1)
        self.guest1.pay_bill(10)
        self.assertEqual(10,self.guest1.wallet)
        self.assertEqual(40,self.room1.tab)