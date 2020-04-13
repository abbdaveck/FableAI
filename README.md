# FableAI

This is the code for my website called FableAI

### URL

[Link to website](https://abbdaveck.github.io/)

## What is FableAI

It is a program that successively creates a story based on user input.


## How does it work

The user start by giving some info about how many characters there should be in the story what their names are and what they will do. The website then sends the info to the server through an API and using GPT2 it creates a story. GPT2 is an unsupervised transformer language model created by OpenAI. The user is then shown a couple of sentences and can continue the story. After every input by the user the AI creates a few more sentences and thought that process a story is made.

## How did I make it

### Backend

The backend is basiclly basically a loop that continuously checks a file on my computer to check if it has been updated with new info. If that is the case it it send the data to the AI. The scripts then checks for things like dubble spaces in the text from the AI writes it to a file for the API to see and send to the user.

### Training AI
I used code by [Max Wolf](https://minimaxir.com/2019/09/howto-gpt2/) to train my model. The GPT2 model that I use is a 744-model trained with the 10 000 most popular stories from the subreddit r/nosleep. I used a PRAW (Python API Reddit Wrapped) to take the stories write them to a text file on my computer. The auothors using that subreddit have a tendency to link to their other stories in the end of the story which meant that sprinkled in with all of the stories there were a bunch of URLs and such. I tried to manually clean them up but since all of the stories combined is more combines to more than 2 million words and a little over 4700 pages that obviously was impossible. So most of the text is left unedited and therefore some of the outputs frp, the AI are a bit weird.

### API

The API is a simple Flask API that through PUT and GET request is the link between the user and the backend. Since Flask runs locally I use NGROK to make the API public. NGROK is a localhost tunneling service. The downside to this is that a NGROK session is only eight hours and after that I need to restart it. I didn't bother writing a CORS (Cross Origin Resource Sharing) API and therefore I use the wonderful CROS Anywhere API made by Rob Wu. I send the all the requests through CORS Anywhere and it handles all that. 


### Frontend/Website

The frontend is a simple website that takes the inputs from the user and sends them using my API to the backend. The website then waits 5 seconds then checks if the text has been updated, is not then it waits another 5 seconds and so on. If the AI is finished loading the website displays is to the user. 

### Files

* **API.py** - the scrit fro the API
* **backend.py** - the script that creates the text
* **change.txt** - tells the API if the backends is proccessing something
* **communication.txt** - the file the API and the backend use to communicate
* **index.html** - the website (thought the website isn't running off of this exact file it is running from [here](https://github.com/abbdaveck/abbdaveck.github.io)
* **scraper.py** - took all the texts from the subreddit and downloaded them
* **style.css** - style sheet for the website
* **top10000.txt** - all the stories from the subreddit


### Problems
To communicate between my two simultainuasly running Python scripts they read and write to a local file. This isn't the most elegant solution but it works. When my website waites the 5 seconds between checking if the backends is finished loading it kinda freezes and you can't for example open the console. They way I built this website right now it isn't really scalable since the backends can only procces one request at a time and it takes 20-30 seconds for it to do that. 

## Built With

* [GPT2](https://openai.com/blog/better-language-models/) - The language prediction model used
* [Flask](https://flask.palletsprojects.com/en/1.1.x/) - The API framework used
* [NGROK](https://ngrok.com/docs) - The localhost tunneling serviced used
* [CORS Anywhere](https://github.com/Rob--W/cors-anywhere#documentation) - The service used for handeling CORS
* [GPT2 Model Trainer](https://colab.research.google.com/drive/1OG1HxBMdIMyWfc0qP2rz6tvQwtx9Gikn#scrollTo=t6MRCaq33f7s) - The code I used to train my model


## Author

* **David Eckemark** - [abbdaveck](https://github.com/abbdaveck)

