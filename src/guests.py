class Guest:
    def __init__(self,name,wallet,favourite_songs):
        self.name = name
        self.wallet = wallet
        self.favourite_songs = favourite_songs
        self.room_flag = ()

    def enter_room(self,room):
        room.guest_list.append(self)
        self.room_flag = room

    def leave_room(self):
        self.room_flag.guest_list.remove(self)
        self.room_flag = ()

    def choose_song(self,song):
        if song in self.room_flag.song_list:
            return self.room_flag.play_song(song)
        else:
            return "Please choose a song in the song list."
        
    def decrease_wallet(self,amount):
        self.wallet -= amount

    def pay_bill(self,amount):
        self.room_flag.decrease_tab(amount)
        self.decrease_wallet(amount)