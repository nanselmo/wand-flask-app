#libraries
import os
import random

#modules
from flask import Flask
from flask import render_template


#custom functions
def get_random_wand():
    wand_cores = ["unicorn", "dragon", "wolfsbane", "phoneix"]
    random_core = random.choice(wand_cores)
    return random_core
    
app = Flask(__name__)

#the routes AND handlers
@app.route('/')
def mainpage():
    return "Hello World. I am an amazing programmer - in only 7 hours"

    
@app.route('/wandstart')
def start_handler():
    return "Welcome Wizard. Let's find you wand"
    
@app.route('/yourwand')
def wand_handler():
    the_random_core = get_random_wand()
    return render_template('results.html', output_core = the_random_core) 
    #the variable user_core gets passed to the results.html template and replaces the {{user_core}}
    
    

if __name__ == '__main__':
    app.debug = True
    app.run(host=os.environ['IP'], port=os.environ['PORT']) 
    
    
    


    
    