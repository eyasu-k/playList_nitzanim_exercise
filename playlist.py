liked_songs = {
    "Shake It Off": {
        "artist": "Taylor Swift",
        "duration": (3, 23),
        "genre": "Pop"
    },
    "Shemesh": {
        "artist": "Mergi",
        "duration": (2, 33),
        "genre": "Israeli"
    },
    "Chop Suey!": {
        "artist": "System of a Down",
        "duration": (3, 30),
        "genre": "Metal"
    },
    "Mimaamakim": {
        "artist": "Idan Raichel",
        "duration": (4, 33),
        "genre": "Israeli"
    },
    "Do I Wanna Know?": {
        "artist": "Arctic Monkeys",
        "duration": (4, 26),
        "genre": "Rock"
    },
    "Love Story": {
        "artist": "Taylor Swift",
        "duration": (3, 55),
        "genre": "Pop"
    },
    "Bo’ee": {
        "artist": "Idan Raichel",
        "duration": (4, 45),
        "genre": "Israeli"
    }
}

my_likeed_songs = {
    "Kontnuum": {
        "artist": "SennaRin",
        "duration": (3, 11),
        "genre": "Unknown"
    },
    "Wahran": {
        "artist": "RANDALL",
        "duration": (3, 52),
        "genre": "instrumental"
    },
    "New Type of Hero": {
        "artist": "Chatterbox",
        "duration": (3, 16),
        "genre": "pop"
    }
}

liked_songs = liked_songs | my_likeed_songs


def delete_song(playlist: dict)-> None: #what if Mia deletes a song twice? she can't with this function :D.
    song = input("Enter the name of the song to check: ")
    print("The song exists:", song in playlist)
    if song not in playlist:
        return
    if input("Enter anything to delete the song, enter space or nothing to not delete it: ").strip():
        playlist.pop(song)
        print("song removed")

def remove_artist(playlist: dict[dict])-> None:#what if mia wants to remove songs of artist that doesn't exist? she can't, my code won't let her!
    artist = input("Enter the name of the artist to remove: ")
    songs_to_remove = [key for key in playlist if playlist[key]["artist"] == artist]
    if not songs_to_remove:
        print("Artist not found.")
    else:
        for song in songs_to_remove:
            print(f"Removed '{song}' by {playlist[song]['artist']}")
            playlist.pop(song)

def filter_israeli_songs(playlist: dict, max_len: tuple = (3, 30))-> dict:
    time_sum = lambda x: x[0]*60 + x[1] #returns the first index *60 + the second index. -> convert a  tuple containing a minute and a second into seconds. example: (3, 30) will be 240 (seconds)
    filtered_songs = {}
    for song in playlist:
        if playlist[song]["genre"].lower() == 'israeli' and time_sum(playlist[song]["duration"]) <= time_sum(max_len) :
            filtered_songs[song] = playlist[song]
    return filtered_songs

def print_playlist(playlist: dict)-> None:
    for song in playlist:
        artist, duration, genre = playlist[song].values()
        print(f"-{song}\n\t-made by {artist}\n\t-genre: {genre}")

def create_song(name: str, artist: str, duration: tuple[int, int], genre: str)->dict:
    return {name: {"artist": artist, "duration": duration, "genre": genre}}



def main():
    pass
