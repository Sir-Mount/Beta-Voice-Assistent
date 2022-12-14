# Beta Voice Assistent
 A simple voice assistent written in python

You can interact with it through saying the wakeword "Beta"
Rightafter you say on of the command words:
* "Ask": With this command you can make the assistent ask questions to OpenAI (You will need an OPENAI_API_KEY for this.).
* "Joke": This will make the assistent tell a programmer joke.
* "Play"+(some music or video name): This will open the browser and play the first video on youtube with said name.
* "Run"+(application name): This will start the application of that name.*
* "Look up"+(subject): This will make the assistent tell you the first few lines of the first wikipedia hit on the subject.
* "Day": This will make the assistent tell you the current date.
* "Time": This will make the assistent tell you the current time.
* "Stop": This will shut down the assistent.

You can use these words in proper sentences and the assistent will still recognize the command words.

*some directories will have to be changed in  code:
 - The speech-to-text recognizer must point to the correct model.
 - The run-command will only run applications in the folder it points to.


