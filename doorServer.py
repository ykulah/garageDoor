import random 
import hashlib
import RPi.GPIO as GPIO
import time

key = hashlib.sha224("quick%brownfox@jumpsover_thelazydog").hexdigest()
print key
   
from flask import Flask
from flask import render_template
app = Flask(__name__)

# GPIO configurations
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18,GPIO.HIGH)

#@app.route("/")
#def hello():
#    return 'Hello World!'

@app.route('/openDoor/<phrase>', methods=['GET', 'POST'])
def openDoor(phrase):

	if (phrase == str(key) and GPIO.input(18) == True):
		GPIO.output(18,GPIO.LOW)
		time.sleep(5)	
		GPIO.output(18,GPIO.HIGH)
	        return render_template('index.html', img="checkmark.svg", text="Ok, door will open in few seconds.")    	  
	if (phrase == str(key) and GPIO.input(18) == False):
	        return render_template('index.html', img="fail.svg", text="Another operation is in progress. Try after 5 seconds.")    	  
	else:
		return render_template('index.html', img="fail.svg", text="Check your URL.")   
	
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=571)
