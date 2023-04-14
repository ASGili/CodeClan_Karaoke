class Guest:
    def __init__(self,name,wallet,favourite_songs):
        self.name = name
        self.wallet = wallet
        self.favourite_songs = favourite_songs
        self.room_flag = ()

    def enter_room(self,room):
        room.guest_list.append(self)
        self.room_flag = room

    def leave_room(self,room):
        room.guest_list.remove(self)
        self.room_flag = ()

    def choose_song(self,song):
        if song in self.room_flag.song_list:
            return self.room_flag.play_song(song)
        else:
            return "Please choose a song in the song list."