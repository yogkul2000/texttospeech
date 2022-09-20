from flask import Flask, render_template, request
from gtts import gTTS
import os
import playsound

app = Flask(__name__, template_folder="templates")


@app.route("/")
def form():
    return render_template("form.html")


# Decorator to tell the app which function is to be called.
@app.route("/data", methods=["POST", "GET"])
def data():
    """
   After form submit render the next page.
   """
    global form_data  # Storing the form data globally
    form_data = request.form
    return render_template("data.html")


@app.route("/download", methods=["POST", "GET"])
def download():
    """
    Download the audiofile
    """
    if request.method == "POST":
        for _, value in form_data.items():
            obj = gTTS(
                text=value, lang="en", slow=True
            )  # Pass the text, save the audio file in the same directory.
            obj.save(f"{value}.mp3")

    return render_template("data.html")


@app.route("/play", methods=["POST", "GET"])
def play():
    """
    Currently this function downloads the audiofile to the system, plays it and deletes it.
    """
    if request.method == "POST":
        for _, value in form_data.items():
            obj = gTTS(text=value, lang="en", slow=True)
            filename = "test.mp3"
            obj.save(filename)
            playsound.playsound(os.getcwd() + "\\" + filename)  # Play the audiofile
            os.remove(filename)

    return render_template("data.html")


if __name__ == "__main__":
    app.run(debug=True, port=8080, use_reloader=False)
