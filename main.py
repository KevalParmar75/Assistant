import datetime
import speech_recognition as sr
import os
import pyttsx3
import webbrowser
import openai

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = "your open ai api here"
    chatStr += f"your name here: {query}\n Optimus: "
    response = openai.Completion.create(
        model="text-davinci-003", # you can use other models as well
        prompt= chatStr,
        temperature=0.7,
        max_tokens=4096,#adjust as per convinience
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    say(response["choices"][0]["text"])
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]


def ai(propmt):
    openai.api_key = "your open ai api here"
    text = f"OpenAI for response for propmt: {propmt} \n"

    response = openai.ChatCompletion.create(
      model="text-davinci-003",# you can use other models as well
      propmt=propmt,
      temperature=1,
      max_tokens=4096,# adjust as per convinience
      top_p=1,
      frequency_penalty=0,
      presence_penalty=0
    )
    # print(response["choices"][0]["text"])
    text +=response["choices"][0]["text"]
    if not os.path.exists("OpenAi"):
        os.mkdir("OpenAi")

    # with open(f"OpenAi/prompt- {random.randint(1,10000000000)}","w") as f:
    #     f.write(text)
    with open(f"Openai/{''.join(propmt.split('intelligence')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def say(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            say(f"User said: {query}")
            return query
        except Exception:
            return "Some Error Occurred. Sorry from Optimus"


if __name__ == '__main__':
    print('PyCharm')
    say(" HII I am Optimus")

    while True:
        query = takeCommand().lower()

        if "open website" in query:
            # Extract the website URL from the query
            website = query.replace("open website", "").strip()
            # Add the URL prefix if not provided (e.g., "https://")
            if not website.startswith("http"):
                website = "https://www." + website + ".com"
            # Open the website in the default web browser
            webbrowser.open(website)
            say(f"Opening {website} in your web browser.")
        elif "open website .in" in query:  # Check for a specific condition
            website = query.replace("open website .in", "").strip()
            website = "https://www." + website + ".in"
            webbrowser.open(website)
            say(f"Opening {website} in your web browser.")



        elif "time" in query:
            strfTime = datetime.datetime.now().strftime("%H:%M")
            say(f"sir time is {strfTime}")

        elif "date" in query:
            current_date = datetime.datetime.now().strftime("%Y-%m-%d")
            say(f"Current date: {current_date}")


        elif "using A.I" in query:
            ai(propmt=query)

        elif "reset chat".lower() in query.lower():
            chatStr = ""

        elif "exit" in query:
            exit()

        else:
            print("Chatting...")
            chat(query)

