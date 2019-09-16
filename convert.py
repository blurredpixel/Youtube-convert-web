import youtube_dl
import os

class convertVideo():

    def __init__(self,url,title,artist):
        self.url=url
        self.title=title
        self.artist=str(artist).replace(" ","")
        #eturn super().__init__(*args, **kwargs)

    def statusCheck(self,d):
        return d['status']=='finished'
    def getfilename(self):
        return '{}-{}.mp3'.format(self.title,self.artist)
    def getfilepath(self):
           
        return str(os.getcwd())+'/public/{}-{}.mp3'.format(self.title,self.artist)
    def downloadVideo(self):
        ydl_opts = {
            'format': 'bestaudio/best',
            'outtmpl': str(os.getcwd())+'/public/{}-{}.%(ext)s'.format(self.title,self.artist),
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
                
            }],'postprocessor_args': [
            '-threads', '4'
            ],
            'prefer_ffmpeg': True,
        
            'progress_hooks': [self.statusCheck],
        }

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                ydl.download([self.url])
            except:
                return "Error: Download link invalid"
           
            # ydl.prepare_filename(self.title)
            return '{}-{}.mp3'.format(self.title,self.artist)
    