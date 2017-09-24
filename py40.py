class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

placebo = ["I'm in the basement",
            "You're in the sky"]

happy_bday = Song(["Happy birthday to you",
                    "I don't want to get sued",
                    "So I'll stop right there"])

bulls_on_parade = Song(["They rally around tha familiy",
                        "With pockets full of shells"])

placebo_song = Song(placebo)

happy_bday.sing_me_a_song()
placebo_song.sing_me_a_song()
bulls_on_parade.sing_me_a_song()
