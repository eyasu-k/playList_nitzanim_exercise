import time
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

eyasu_liked_songs = {
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

def time_sum(minutes_and_seconds: tuple)-> int:
    return minutes_and_seconds[0]*60+minutes_and_seconds[1]

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

def generate_progress_bar(iterations: int, bar_size: int, char: str = '\u2588', empty_char: str = '')-> list[str]:
    if iterations == bar_size:
        return [char]*iterations
    if iterations < bar_size and iterations != 0:
        frequency = bar_size // iterations #the minimum number of chars per progress
        remaining_chars = bar_size % iterations
        progress_bar = []
        for i in range(iterations):
            if remaining_chars > 0:
                progress_bar.append(char*(frequency+1))#extra chars will be added to the first few bars if the bar_size cant be divided by the number of iterations evenly -> if bar_size = 10, iterations = 5 --> progress bar = ['[char][char]', '[char][char]', '[char][char]', '[char][char]', '[char][char]'], if bar_size = 5, iterations = 3 --> progress_bar = ['[char][char]', '[char][char]', '[char]']
                remaining_chars -= 1
            else:
                progress_bar.append(char*frequency)
        return progress_bar

    empty_space = iterations // bar_size
    progress_bar = []
    remaining_chars = bar_size
    for i in range(iterations):
        if i%empty_space == 0 and remaining_chars > 0:#the first value inside progress_bar will be char because 0 can be divided by any number, meaning: reversing progress_bar would make the last value of the progress bar be char instead of empty string
            progress_bar.append(char)
            remaining_chars -= 1
        else:
            progress_bar.append(empty_char)
    return progress_bar[::-1]#im reversing it because the first value inside progress_bar is always 'char' and i wanted the last value to be always 'char' instead

def play_playlist(playlist: dict, sleep_timer: tuple[int, int] = None, progress_bar_size: int = 100, speed: int = 1)-> None:
    sleep_timer_seconds = None
    if sleep_timer:
        sleep_timer_seconds = time_sum(sleep_timer)
    for song in playlist:
        if not sleep_timer or sleep_timer_seconds > 0:
            print(f"\"{song}\" by {playlist[song]['artist']}\n\t 0:0   ", end = '')
            total_seconds_in_song = time_sum(playlist[song]['duration'])
            progress_bar = generate_progress_bar(iterations=total_seconds_in_song, bar_size=progress_bar_size, char='−')
            for progress in range(total_seconds_in_song):
                print(progress_bar[progress], end='')
                time.sleep(1/speed)
                if sleep_timer:
                    sleep_timer_seconds -= 1
                    if sleep_timer_seconds <= 0:
                        break
            print(f"   {playlist[song]['duration'][0]}:{playlist[song]['duration'][1]}")
        else:
            print("Sleep timer ended.")
            break

def clean_input(msg: str, error_msg: str, checker_function)-> str:
    while True:
        new_input = input(msg)
        if checker_function(new_input):
            return new_input
        print(error_msg)

def menu()-> list[str]:
    choices = ["Show playlist", "Add a song", "Remove song", "Remove every song made by a given artist","Delete every song except Israeli songs shorter than 3:30 minutes"]
    print("-"*10+"Liked Songs Playlist Player"+"-"*10)
    for index, choice in enumerate(choices):
        print(index+1, choice, sep='. ')
    return choices

def main():
    pass