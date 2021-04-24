import pandas as pd
import flask
import pickle

app = flask.Flask(__name__, template_folder='templates', static_url_path = "", static_folder = "templates/static")
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/', methods=['GET', 'POST'])

def main():
    if flask.request.method == 'GET':
        return(flask.render_template('main.html'))
    if flask.request.method == 'POST':
        name = flask.request.form['name']
        age = flask.request.form['age']
        cozone = flask.request.form['cozone']
        pneumonia=flask.request.form['pneumonia']
        cough = flask.request.form['cough']
        breath = flask.request.form['breath']
        chills= flask.request.form['chills']
        diarreah = flask.request.form['diarreah']
        fatique = flask.request.form['fatique']
        fever = flask.request.form['fever']
        malaise = flask.request.form['malaise']
        itch = flask.request.form['itch']
        muscle = flask.request.form['muscle']
        vomit = flask.request.form['vomit']
        myalgia = flask.request.form['myalgia']
        soar = flask.request.form['soar']
        sputum = flask.request.form['sputum']
        tired = flask.request.form['tired']

        input_variables = pd.DataFrame([[age,cozone,pneumonia,cough,breath,chills,diarreah,fatique,fever,malaise,itch,muscle,vomit,myalgia,soar,sputum,tired]],
                                       columns=['age', 'from_covid_zone', 'pneumonia', 'cough', 'difficult in breath',
       'chills', 'diarrhea', 'fatigue', 'feaver', 'malaise', 'itchy throat',
       'muscle aches', 'vomitting nausea', 'myalgia', 'sore throat', 'sputum','tired'], dtype=float)
        prediction = model.predict(input_variables)[0]
        if(prediction==0):
            prediction="Looks like you are not infected by corona virus! Be safe!"
        else:
            prediction="Looks like you may infected by corona. Don't panic->Contact your nearby Hospital Immediately!"

        if(cozone=="1"):
            cozone="Yes"
        else:
            cozone="No"

        if(pneumonia=="1"):
            pneumonia="Yes, affected by pneumonia"
        else:
            pneumonia="Not pneumonia patient"
          

        if(cough=="1"):
          cough="Yes, having dry cough"
        else:
          cough="No, cough"

        if(breath=="1"):
          breath="Yes,  difficulties in breathing"
        else:
          breath="Don't have any difficulties in breathing"

        if(chills=="1"):
          chills="Yes having chills feeling"
        else:
          chills="Don't having chills feeling"

        if(diarreah=="1"):
          diarreah="Yes, have diarreah issues"
        else:
          diarreah="Don't, have diarreah issues"

        if(fatique=="1"):
          fatique="Yes, have fatique"
        else:
          fatique="Do not any have fatique"

        if(fever=="1"):
          fever="Yes, temparatureis abnormal "
        else:
          fever="No, tempareature is normal"

        if(malaise=="1"):
          malaise="Have malaise"
        else:
          malaise="Don't have malaise"

        if(itch=="1"):
          itch="Yes, have Itching in throat"
        else:
          itch="do not have itchy feeling on throat"

        if(muscle=="1"):
          muscle="yes, have muscle ache"
        else:
          muscle="Don't have muscle ache"

        if(vomit=="1"):
          vomit="Yes,  have Vomitting"
        else:
          vomit="Do not have vomitting"

        if(myalgia=="1"):
          myalgia="Yes, have Myalgia"
        else:
          myalgia="Do not have Myalgia"

        if(soar=="1"):
          soar="Yes, have soar throat"
        else:
          soar="Do not have soar throat"

        if(sputum=="1"):
          sputum="Yes, have sputum on nose and mouth"
        else:
          sputum="Do not have sputum on nose and mouth"

        if(tired=="1"):
          tired="Yes, have tiredness"
        else:
          tired="Do not have tiredness" 

        return flask.render_template('main.html',
                                     original_input={
                                      'Name':name,
                                      'Age':age,
                                      'From covid alert zone':cozone, 
                                      'Pneumonia':pneumonia, 
                                      'Cough':cough, 
                                      'Difficult in breath':breath,
                                      'Chills':chills,
                                      'Diarreah':diarreah, 
                                      'Fatigue':fatique, 
                                      'Feaver':fever, 
                                      'Malaise':malaise, 
                                      'Itchy throat':itch,
                                      'Muscle aches':muscle, 
                                      'Vomitting nausea': vomit, 
                                      'Myalgia':myalgia, 
                                      'Sore throat':soar, 
                                      'Sputum':sputum,
                                      'Tired':tired},result=prediction)


if __name__ == '__main__':
    app.run()
