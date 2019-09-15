from flask import Flask, render_template, flash, request,send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from convert import convertVideo 
import eyed3
import os
# App config.

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER']="public"
class ReusableForm(Form):
    videourl = TextField('Video URL:', validators=[validators.required()])
    title = TextField('Track Title:')
    artist = TextField('Track Artist:')
    album = TextField('Track Album:')
 
def changetags(file,form):
    audiofile = eyed3.load(str(os.getcwd())+'/public/'+file)
    audiofile.tag.artist = str(form.artist.data)
    audiofile.tag.album = str(form.album.data)
    audiofile.tag.album_artist = str(form.artist.data)
    audiofile.tag.title = str(form.title.data)
    audiofile.tag.save()
@app.route("/", methods=['GET', 'POST'])
def processURL():
    form = ReusableForm(request.form)
    
    # print (form.errors)
    if request.method == 'POST':
        
        cv=convertVideo(form.videourl.data,form.title.data,form.artist.data)
        
        
        

        if form.validate():
            # Save the comment here.
            
            if(os.path.exists(cv.getfilename())):
                return render_template('ytdl.html', form=form,file=cv.getfilename())
            
            
            else:
                flash('Converting video! Please wait...')
                file=cv.downloadVideo()
                if("Error" in file):
                    flash("Error in Youtube URL")
                    return render_template('ytdl.html', form=form)
                # print(file)
                else:
                    if(cv.statusCheck):
                        flash("Video done!")
                        changetags(file,form)
                        return render_template('ytdl.html', form=form,file=file)
            
            
        else:
            flash('Error in form input.')
        
 
    return render_template('ytdl.html', form=form)
@app.route("/downloads/<file>")
def sendfiletouser(file):
    return send_file(str(os.getcwd())+'/public/{}'.format(file),as_attachment=True)
if __name__ == "__main__":
    app.run(port='6969', host="0.0.0.0")