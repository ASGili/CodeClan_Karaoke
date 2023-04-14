class Room:
    def __init__(self,name,capacity,tab):
        self.name = name
        self.capacity = capacity
        self.song_list = []
        self.tab = tab
        self.guest_list = []
    
    def add_song(self,song_to_add):
        self.song_list.append(song_to_add)
    
    def check_song_list(self,song_to_check):
        return song_to_check in self.song_list
    
    def play_song(self,song_to_play):
        result =f'{song_to_play.title} by {song_to_play.artist} is playing.'
        return result
    
    def increase_tab(self,amount):
        self.tab += amount

    def decrease_tab(self,amount):
        self.tab -= amount

    def check_vacancy(self):
        return self.capacity > len(self.guest_list)
    
