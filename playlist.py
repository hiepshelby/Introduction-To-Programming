import webbrowser

class Video:
    def __init__(self, title, link):
        self.title = title
        self.link = link

class Playlist:
    def __init__(self, name, description, rating, videos):
        self.name = name
        self.description = description
        self.rating = rating
        self.videos = videos

def read_video():
    title = input("Enter title: ") + "\n"
    link = input("Enter link: ") + "\n"
    video = Video(title, link)
    return video

def read_videos():
    videos = []
    total = input("Enter how many video: ")
    print("---------------------------")
    for i in range(int(total)):
        print("Video " + "[" + str(i+1) + "]")
        video = read_video()
        videos.append(video)
    return videos

def write_video_to_txt(file, video):
    file.write(video.title) 
    file.write(video.link)

def write_videos_to_txt(videos, file):
    total = len(videos)
    file.write(str(total) + "\n")
    for i in range(total):
        write_video_to_txt(file, videos[i])

def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    video = Video(title, link)
    return video

def read_videos_from_txt(file):
    videos = []
    total = file.readline()
    for i in range(int(total)):
        video = read_video_from_txt(file)
        videos.append(video)
    return videos

def print_video(video):
    print("Video title: " + video.title, end = "")
    print("Video link: " + video.link, end = "")

def print_videos(videos):
    total = len(videos)
    for i in range(total):
        print("Video " + "[" + str(i+1) + "]")
        print_video(videos[i])

def read_playlist():
    playlist_name = input("Enter playlist name: ") + "\n"
    playlist_description = input("Enter playlist description: ") + "\n"
    playlist_rating = input("Enter playlist rating: ") + "\n"
    playlist_videos = read_videos()
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def read_playlists():
    playlists = []
    total = input("Enter how many playlist: ") 
    for i in range(int(total)):
        print("\nPlaylist " + "[" + str(i+1) + "]")
        print("---------------------------")
        playlist = read_playlist()
        playlists.append(playlist)
    return playlists

def write_playlist_to_txt(file, playlist):
    file.write(playlist.name )
    file.write(playlist.description)
    file.write(playlist.rating)
    write_videos_to_txt(playlist.videos, file)

def write_playlists_to_txt(playlists):
    total = len(playlists)
    with open("playlist.txt", "w") as file:
        file.write(str(total) + "\n")
        for i in range(total):
            write_playlist_to_txt(file, playlists[i])

def read_playlist_from_txt(file):
    playlist_name = file.readline()
    playlist_description = file.readline()
    playlist_rating = file.readline()
    playlist_videos = read_videos_from_txt(file)
    playlist = Playlist(playlist_name, playlist_description, playlist_rating, playlist_videos)
    return playlist

def read_playlists_from_txt():
    playlists = []
    with open("playlist.txt", "r") as file:
        total = file.readline()
        for i in range(int(total)):
            playlist = read_playlist_from_txt(file)
            playlists.append(playlist)
    return playlists

def print_playlist(playlist):
    print("Playlist name: " + playlist.name, end = "")
    print("Playlist description: " + playlist.description, end = "")
    print("Playlist rating: " + playlist.rating, end = "")
    print_videos(playlist.videos)

def print_playlists(playlists):
    total = len(playlists)
    print("---------------------------")
    print("You are having " + str(total) + " playlist")
    for i in range(total):
        print("\nPlaylist " + "[" + str(i+1) + "]")
        print_playlist(playlists[i])

def select_option():
    print("------- Menu Option -------")
    print("| [1] Creat playlist      |")
    print("| [2] Print playlist      |")
    print("| [3] Add a playlist      |")
    print("| [4] Delete playlist     |")
    print("| [5] Update playlist     |")
    print("| [6] Add video           |")
    print("| [7] Delete video        |")
    print("| [8] Play video          |")
    print("| [9] Save and exit       |")
    print("---------------------------")

def select_in_range(prompt, min, max):
    choice = input(prompt)
    while not choice.isdigit() or int(choice) < min or int(choice) > max:
        choice = input(prompt)
    choice = int(choice)
    return choice 

def add_playlist(playlists):
    print("---------------------------")
    playlist = read_playlist()
    playlists.append(playlist)
    return playlists

def delete_playlist(playlists):
    total = len(playlists)
    print("---------------------------")
    print("You are having " + str(total) + " playlist")
    for i in range(total):
        print("[" + str(i+1) + "] " + playlists[i].name, end = "")
        print("---------------------------")
    choice = select_in_range("Enter playlist you want to delete: ", 1, total)
    del playlists[choice-1]
    return playlists

def update_playlist(playlists):
    total = len(playlists)
    print("You are having " + str(total) + " playlist")
    for i in range(total):
        print("[" + str(i+1) + "] " + playlists[i].name, end = "")
    for i in range(total):
        choice = select_in_range("Enter playlist you want to update: ", 1, total)
        if choice - 1 == i:
            print("[1] Name: " + playlists[i].name, end = "")
            print("[2] Description: " + playlists[i].description, end = "")
            print("[3] Rating: " + playlists[i].rating, end = '')
            choice = select_in_range("Enter what you want to update (1-3): ", 1, 3)
            if choice == 1:
                new_playlist_name = input("Enter new playlist name: ") + "\n"
                playlists[i].name = new_playlist_name
                return playlists
            if choice == 2:
                new_playlist_description = input("Enter new playlist description: ") + "\n"
                playlists[i].description = new_playlist_description
                return playlists
            if choice == 3:
                new_playlist_rating = input("Enter new playlist rating: ") + "\n"
                playlists[i].rating = new_playlist_rating
                return playlists

def add_video(playlists):
    total = len(playlists)
    print("You are having " + str(total) + " playlist")
    for i in range(total):
        print("[" + str(i+1) + "] " + playlists[i].name, end = "")
    choice = select_in_range("Enter playlist you want to add video: ", 1, total)
    for i in range(total):
        if choice - 1 == i:
            new_video_title = input("Enter title: ") + "\n"
            new_video_link = input("Enter link: ") + "\n"
            new_video = Video(new_video_title, new_video_link)
            playlists[i].videos.append(new_video)
            return playlists
    
def delete_video(playlists):
    total = len(playlists)
    print("You are having " + str(total) + " playlist")
    for i in range(total):
        print("[" + str(i+1) + "] " + playlists[i].name, end = "")
    choice = select_in_range("Enter playlist you want to delete video: ", 1, total)
    for i in range(total):
        if choice - 1 == i:
            print_videos(playlists[i].videos)
            choice = select_in_range("Enter video you want to delete: ", 1, len(playlists[i].videos))
            del playlists[i].videos[choice - 1]
            return playlists
            
def play_video(playlists):
    total = len(playlists)
    print("You are having " + str(total) + " playlist")
    for i in range(total):
        print("[" + str(i+1) + "] " + playlists[i].name, end = "")
    choice = select_in_range("Enter playlist you want to open video: ", 1, total)
    for i in range(total):
        if choice - 1 == i:
            print_videos(playlists[i].videos)
            choice = select_in_range("Enter video you want to open: ", 1, len(playlists[i].videos))
            if choice - 1 == i:
                print("Open video: " + playlists[i].videos[choice - 1].title)
                webbrowser.open(playlists[i].videos[choice - 1].link, new = 2)
def main():
    try:
        playlists = read_playlists_from_txt()
        print("Loaded data successfully!")
    except:
        print("Welcome the first user!")
        playlists = -1

    if playlists == -1:
        while True:
            select_option()
            choice = select_in_range("Enter [1] to create the first playlist: ", 1, 1)
            if choice == 1:
                print("---------------------------")
                playlists = read_playlists()
                print("---------------------------")
                input("Press to continue")
                break
    
    while True:
        select_option()
        choice = select_in_range("Enter your option (1-9): ", 1, 9)
        if choice == 1:
            playlists = read_playlists()
            print("---------------------------")
            input("Press to continue")
        elif choice == 2:
            print_playlists(playlists)
            print("---------------------------")
            input("Press to continue")
        elif choice == 3:
            playlists = add_playlist(playlists)
            print("---------------------------")
            input("Press to continue")
        elif choice == 4:
            playlists = delete_playlist(playlists)
            print("---------------------------")
            input("Press to continue")
        elif choice == 5:
            playlists = update_playlist(playlists)
            print("---------------------------")
            input("Press to continue")
        elif choice == 6:
            playlists = add_video(playlists)
            print("---------------------------")
            input("Press to continue")
        elif choice == 7:
            playlists = delete_video(playlists)
            print("---------------------------")
            input("Press to continue")
        elif choice == 8:
            play_video(playlists)
        elif choice == 9:
            write_playlists_to_txt(playlists)
            print("---------------------------")
            print("Save playlist successfully!")
            break
        else:
            print("Wrong Input!")

main()