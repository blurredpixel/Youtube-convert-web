import youtube_dl
import os

class convertVideo():

    def __init__(self,url,title):
        self.url=url
        self.title=title
        #eturn super().__init__(*args, **kwargs)

    def statusCheck(self,d):
        return d['status']=='finished'

    def downloadVideo(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(os.getcwd())+'/public/{}.%(ext)s'.format(self.title),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        
            'progress_hooks': [self.statusCheck],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            
            ydl.download([self.url])
           
            # ydl.prepare_filename(self.title)
            return self.title+".mp3"
    