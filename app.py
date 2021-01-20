from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def home():
    try:
      a = request.form.get("text")
      opt = request.form.get("options")
      if opt == "pc" :
          t = a.title()
      elif opt == "uc" :
          t = a.upper()
      else :
          t = a.casefold()  
    except:
        a = ''
        t = ''
    return render_template('home.html', strtext=a, strnew=t)

app.run()
 