from flask import Flask, render_template
import random
app = Flask(__name__)
@app.route ("/")



def num():
	return render_template("test1.html")





	# abd2 = ["Mohmmed","_ma_","highigh","ghfdgkh","1231568","252025"]
	# return random.choice(abd2)






# @app.route ("/goodBay")
# def goodBay():
# 	return "good Bay!!!!!"

# @app.route ("/Mohmmed")
# def Mohmmed():
# 	return "Mohmmed"







if __name__ == "__main__":
	app.run(port= 8585,debug = True)   