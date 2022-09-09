class Video:
    def __init__(self, title, link):
        self.title = title 
        self.link = link

def read_video():
    title = input("Enter title: ")
    link = input("Enter link: ")
    video = Video(title, link)
    return video

def read_videos():
    videos = []
    total_video = int(input("Enter howm many videos: "))
    for i in range(total_video):
        print("Enter video", i+1)
        vid = read_video()
        videos.append(vid)
    return videos

def write_video_to_txt(video,file):
    file.write(video.title + "\n")
    file.write(video.link + "\n")

def write_videos_to_txt(videos):
    with open("videos.txt", "w") as file:
        total = len(videos)
        file.write(str(total) + "\n")
        for i in range(total):
            write_video_to_txt(videos[i],file)

def read_video_from_txt(file):
    title = file.readline()
    link = file.readline()
    video  = Video(title, link)
    return video

def read_videos_from_txt():
    videos = []
    with open("videos.txt", "r") as file:
        total = file.readline()
        for i in range(int(total)):
            video = read_video_from_txt(file)
            videos.append(video)
    return videos

def print_video(video):
    print("Video title:", video.title, end = " ")
    print("Video link:", video.link, end = " ")

def print_videos(videos):
    print("-----")
    for i in range(len(videos)):
        print_video(videos[i])

def main():
    videos = read_videos()
    write_videos_to_txt(videos)
    videos = read_videos_from_txt()
    print_videos(videos)

main()