from flask import Flask, render_template, flash, request,send_file
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from convert import convertVideo 
import eyed3
# App config.

app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
app.config['UPLOAD_FOLDER']="public"
class ReusableForm(Form):
    videourl = TextField('Video URL:', validators=[validators.required()])
    title = TextField('Track Title:',validators=[validators.required()])
    artist = TextField('Track Artist:',validators=[validators.required()])
    album = TextField('Track Album:',validators=[validators.required()])
 
def changetags(file,form):
    audiofile = eyed3.load('. /public/{}'.format(file))
    audiofile.tag.artist = str(form.artist.data)
    audiofile.tag.album = str(form.album.data)
    audiofile.tag.album_artist = str(form.artist.data)
    audiofile.tag.title = str(form.title.data)
    audiofile.tag.save()
@app.route("/", methods=['GET', 'POST'])
def processURL():
    form = ReusableForm(request.form)
    
    print (form.errors)
    if request.method == 'POST':
        flash('Converting video! Please wait...')
        cv=convertVideo(form.videourl.data,form.title.data)
        
        
        

        if form.validate():
            # Save the comment here.
            
            file=cv.downloadVideo()
            if(cv.statusCheck):
                flash("Video done!")
                changetags(file,form)
        else:
            flash('Error in form input.')
        return render_template('ytdl.html', form=form,file=file)
 
    return render_template('ytdl.html', form=form)
@app.route("/downloads/<file>")
def sendfiletouser(file):
    return send_file('. /public/{}'.format(file))
if __name__ == "__main__":
    app.run(port='6969', host="0.0.0.0")