import os
import time
from pytube3 import YouTube

def download_video(video_url):
    y = YouTube()
    y.url = video_url

    #y.filename contains the default file name
    if not os.path.isfile(DOWNLOAD_PATH+y.filename+'.mp4'):
        print "Downloading %s: " % y.filename
        video = y.get("mp4", "720p")
        video.download(DOWNLOAD_PATH)
        return
    print "Aborting: Already downloaded %s" % y.filename


def get_video_list(filepath):
    return open(filepath, "r").read().splitlines()

if __name__ == "__main__":
    filepath = 'video_urls.txt'
    
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    DOWNLOAD_PATH = ROOT_PATH + "/videos/"
    if not os.path.exists(DOWNLOAD_PATH):
        os.mkdir(DOWNLOAD_PATH)
    
    start_time = time.time()
    for video_url in get_video_list(filepath):
        download_video(video_url)

    time_taken = time.time()-start_time
    print "Time Taken: %s" % time_taken
    print "Finished downloading all pycon videos!"
