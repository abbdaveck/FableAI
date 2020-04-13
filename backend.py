import gpt_2_simple as gpt2
import os, tarfile, time, json
from datetime import datetime

os.system("cls")        #clear terminal

if os.environ['COMPUTERNAME'] == "HOME":
    compath = r"C:\Users\david\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\communication.txt"
    changepath = r"C:\Users\david\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\change.txt"
    checkpoint = r"C:\Users\david\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\checkpoint"
else:
    compath = r"C:\Users\S8daveck\OneDrive\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\communication.txt"
    changepath = r"C:\Users\S8daveck\OneDrive\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\change.txt"
    checkpoint = r"C:\Users\S8daveck\OneDrive\OneDrive - ABB Industrigymnasium\Teknik\VT 20\Create your own story\checkpoint"


sess = gpt2.start_tf_sess()     #start session
gpt2.load_gpt2(sess, run_name='runstory', checkpoint_dir = checkpoint)   #laddar in modellen

os.system("cls")        #clear terminal

def getInfo(name, friends, num, story):
    if story[len(story)-1] != ".":
        story += "."
    if num == 0:
        re = "This is a story about " + name + " that " + story
    else:
        characters = ""
        for i in range(num):
            if i < num-1:
                characters += str(", " + friends[i])
            elif num == 1:
                characters += friends[i]
            else:
                characters += " and " + friends[i]
        if num > 1:
            re = "This is a story about " + name +  " and his friends" + characters + " and they " + story
        else:
            re = "This is a story about " + name +  " that, together with his friend " + characters + " " + story
    return re

def createStory(prefix):
    print("Loading...")
    text = gpt2.generate(sess, run_name='runstory', length=50, temperature=0.8, prefix=prefix,return_as_list=True)  #skapar storyn
    split = text[0].split("§")      #Splits the output into 'new' and 'old' data
    return split

def change(filename):

    print("Waiting for requests...")
    txt1 = open(filename, "r", encoding="utf-8")
    read1 = json.loads(txt1.read())
    while True:
        time.sleep(2)
        txt2 = open(filename, "r", encoding="utf-8")
        read2 = json.loads(txt2.read())
        if len(read2['time']) == 0:
            update = False
        else:
            update = True
        if read1['time'] != read2['time'] and update:
            break
    txt1.close()
    txt2.close()
    return True

def latest(arr):
    
    cp = arr.copy()  #kopierar arrayen med alla meningar
    for i in range(len(cp)-6):    #Gör om arrayen så bara de 8 sista meningarna är kvar (de är vad som skickas in till AI:n)
        cp.pop(0)
    string = ""
    for i in cp:
        string += i + " "
    return string

def output(text):
    text = text.split(". ")     #splittar vid 
    text.pop(len(text)-1)       #tar bort den sista i arrayen
    for n, i in enumerate(text):    #lägger till en punkt där vi tog punkten vid splitten
        text[n] = i + "."
    re = ""
    for i in text:
        re += i + " "
    return re                 #skickar tillbaka en array där varje objekt är en mening

def writeto(name, dict):
    dict['time'] = getTime()

    f = open(name, 'w', encoding="utf-8")
    f.write(json.dumps(dict)) # use `json.loads` t"o do the reverse
    f.close()
    c = open(changepath, 'w', encoding="utf-8")
    c.write(json.dumps(True)) # use `json.loads` to do the reverse
    c.close() 

def cleanUpArr(arr):
    for n, i in enumerate(arr):    #lägger till en punkt där vi tog punkten vid splitten
        arr[n] = cleanUpString(i)
        if i == "":
            arr.pop(n)
    return arr

def cleanUpString(string):
    send = string.replace("0","").replace("1","").replace("2","").replace("3","").replace("4","").replace("5","").replace("6","").replace("7","").replace("8","").replace("9","").replace("  ", " ").replace(" .", ".").replace("..",".").replace("\n\n", "<br>").replace("\n \n","<br>").replace("\n","<br>").replace(",.", "").replace(" ,", " ")
    return send

def getTime():
    now = str(datetime.now()).split(" ")
    send = []
    time = now[1].split(":")
    time[2] = time[2].split(".")[0]
    [send.append(i) for i in time]
    return send
    
while True:
    # try:
        # os.system("cls")
    change(compath)

    openedfile = open(compath, "r", encoding="utf-8")
    dic = json.loads(openedfile.read())
    openedfile.close()

    prefix = dic['prefix']
    story = cleanUpArr(cleanUpArr(dic['story']))
    friends = prefix['sidech']['names']

    if not story:
        info = getInfo(prefix['name'], friends, int(prefix['sidech']['number']), prefix['prestory'])
        info = cleanUpString(info)
        re = createStory("§" + info)
        re = output(re[1])      #tar vad som kommer tillbaka från createStory och tar bort sista meninen, sätter ihop dem och tar bort lite skräp
        story.append(re)
        story = cleanUpArr(cleanUpArr(story))

        writeto(compath, dic)

    else:   
        late = latest(story)
        late = cleanUpString(late)
        re = createStory(late + "§")
        re = output(re[1])
        story.append(re)
        story = cleanUpArr(cleanUpArr(story))

        writeto(compath, dic)

        # print(dic)

    # except:
    #     print("Error")