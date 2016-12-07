![Alpha](https://raw.githubusercontent.com/joab40/Alpha/master/share/images/logo.png)
# Alpha
Alpha alias sasha aka chacha is a Smart AI (aiml) chatbot build in Python, which have several supported api / webservice dependencies.
In a near future Alpha will be hosted a RaspberryPi inserted in a robotic head.

### How it works
The main core of the project is avoid subscribe to information that you do not need. To get the information when you want it.
And by words or phrases describe a specific or unique call instead of being dependent on a single word or command to make that call. For example, say, "honey can you please turn off the kitchen light"  Or next time you say. "Can someone turn the light off in the kitchen for God's sake" Advantages or disadvantages alpha is highly dependent on web services . Which may result in reduced privacy and security in a smart home solution. 

### API Connections
#### Working OK
    - Chatbot AIML
    - Google speech STT API (SpeechRecognition)
    - Google translate API (Because default language is Swedish)
    - Yandex translate API
    - Pyvona API TTS
    - espeak TTS
    - TelldusCenter "Tellstick" bourne shell scripts (Not included) 
#### In progress ! Unstable
    - Raspberry PI GPIO (robotic motor and lights for the head)
    - Face and Voice recognition (RaspberryPI - Pi Spy camera and microphone)
    - WebeHome (Home Security - Webservice API)
    - Wolframalpha API
    
    

## Installation
Unfortunately there is no boundle installation scripts available. (WORKING ON IT)
At the moment, for more info regarding Raspbarry PI. Se README in raspberrypi catalog
```sh
git clone http://github.com/joab40/Alpha
```

#### Rasberry Pi Setup:
Pyaudio Minimum req. version 2.9

```sh
git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
cd pyaudio;sudo python /setup.py install
```
```sh
sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev python-dev 
sudo apt-get install python-pygame
sudo apt-get install flac
sudo apt-get espeak 
```
```sh
pip install aiml
pip install SpeechRecognition
pip install pyvona
pip install pyyaml
pip install yandex
https://pypi.python.org/pypi/yandex.translate/0.3.5
pip install google-api-python-client
```
## Running (Run)
#### Basic
```sh
./alpha.py
```
#### TextMode
```sh
./alpha.py -t (textmode without stt or tts)
```
#### Option
```sh
./alpha --debug
```


## Supported "verified" Hardware
 - Raspberry PI 2
 - Kinobo - "AKIRO" USB Microphone
 - DM500USB Microphone 

## Supported "verified" Software
 - RASPBIAN "Debian" JESSIE LITE
 - Linux Ubuntu 15.10

## Inspired by
Originally inspererad by my daughter's imaginary friend Sasha. 
And a complete Smart Home Security Center. 
###  Awesome projects
```sh
https://pypi.python.org/pypi/SpeechRecognition
https://pypi.python.org/pypi/wolframalpha
https://github.com/gunthercox/ChatterBot
```

## TODO
    - chatbot deamon.
    - PRE DEV Alpha Work in progress:
        - communicat_client sends stt (typed word text) to mqtt
          ['mqtt']['topic']['stt'] = alpha/stt (at the moment)
        - Alpha(pre dev) listen to all topic.
          catch stt and sends to ['mqtt']['topic']['chatbot'] - alpha/chatbot
          chatbot deamon listen to ['mqtt']['topic']['chatbot'] - alpha/chatbot
          catches messages and process and then send answer to ['chatbot']['mqtttopic']
        - Descripte Json code and decode flow
            Create json sender:

        - Check alive modules

        - Alva o Alpha. 2 bots. Alfa - wolframalpfa - Alva is chatbot2 Alice
           - TTS response to ether name. If Alva o Alpha accure.
             Then change sender from TSS to Alva o Alpha
             because Alva and Alpha is a module. they can have it own releations.
             Alva - Chatbot 1 tellstick samsungremote anc chatbot2 Alva-tts2
                - If chatbot cant answer. orogin message continues.
             Alpha - Chatbor 1 tellstick samsungremote and wolfram alpha-tts2

        - Chatbot 1 allways have a static(same) answers on matched intepretation.
          Chatbot 2(alva and alpha doesnt need to - they can say whatever)
            - Chatbot 1 mange predefines commands. Tellstick Remote etc webehome.
              These ned to allways be the same.

        - Save message state in dict in dict [processing|complete] and timestamp
            time timeout in yaml configuration. ev 5s.
        - json should maybe have a state variable in the message.



## How does this work, what is it and what can i do with it ?
    Well, think of this as a human. How do you function on a very low level?
    First, you might need some kind of "brain". Say you have arms, hands and legs.
    And dont forget ears and mouth. This are some of the main functions you need to
    be able to interact with things. Say its your system modules. without these you
    body want be able to react on things. If some one tells you "very nicely" could you
    please hand me that "cake" in front of you. what might happened is this.

    1) The telling message reaches your ear. And becomes signals into your brain.
    2) Your brain interpreters the message and maybe the result will look something like this:
        "okey" + "i will lif my arm" + "grab cake" + "move cake to its new destination"
    3) And I will say "here is your cake"

    In order to be able to interact with environment, you might need to know how things are
    kept together. This is done by learning. In Alphas case, we already done som learning.
    This is done by telling alpha from the beginning what its arms,legs, ears and mouth is for
    and that it could be used. Alpha also has a AI - chatbot.
    This arms legs ears mouth AI etc. are what we call system modules. Every module have an "predefined - learned" relationship
    with its environment. For example. A ear always sends message data to the brain.
    Brain needs to interpreters message with its own thinking a AI (system module Chatbot.
    AI have a lot of its own releations. Mainly to system modules: Arm, Hand, Mouth etc. But could have
    relations to smaller modules like "a tool or a spoon (for eating the cake) nearby"
    This small modules are registered in memory like the system module. But the big difference
    is that small module could disappear and be forgotten.

    If we would translate this process into a programming flow, this is what might happened.
    1) A voice message recives an ear (STT - Speach To Text) system modul collect information.
       STT interpreters the voice into a text message. Sends it to the Brain (Alpha).
    2) The Brain collects the message and sends message to AI (wich is a learning chatbot with AIML)
       Chatbot interpreters message and reply back to the brain(Alpha). Message might then look like
       something like this: "ok" + "move arm" + "grab cake" + "move to destination" + "here you have the cake".

       Brain receives that thought and sends that message to the arm.
       arm moves and sends back message to brain(Alpha)
       Brain then sends message to hand. etc.

    3) Brain sends then message to TTS (Text To Speach). "Her you have the cake"

    Think of the Brain(alpha) as a HUB. The Brain sends messages (brain synaps) to its modules.
    Modules interpreters message, if message is unknown to module, its just sends it back.
    For exampel. If brain sends "lift arm" to "legs" module. legs module will not approve and
    reject the message. (the legs module could have a relation to mouth/TTS (Text to speach)
    and say: "That Hurt!!" Or "This did not work". In the end the Module that have the highest rate of determing
    whats going to happen is Sysmstem module Chatbot.

    Chatbot should have a hard and straight relation to arm,hand etc and mouth(Text To Speach - TTS).
    Ex: Message first reaches arm, then hand.. and in the end TTS(text to speach)

       You could change cake example with Tv remote control (change channel), or turn off the light
       in this room. The big problem with predefined commands is that you always need to
       know the "exact" command to execute a task. This is where the AI resolves this problem
       AI determines what do response to. but it could be its nemesis, because if a AI learns
       to much of its awareness. It might not want to reply on things that you expect.
       There for, AI allways need to be loaded with a set of predfines (set of rules)AIML files.
       Its like raising a child. If you would like to have some kind of rules/structure in your house,
       you need to tell the environment about those rules. Ex "I bring the food, you help me with the washing"

     Chatbot need to know how it should react, this is done by mainly telling chatbot what
     to response to by coding AIML files(rules). this demonstrate a simple task.
     Say.    Could you please give me the cake. Response could be "ok i will give you the cake"
     or Say  Could you for good sake give me a pice of the cake". response "ok i will give you the cake"

    If your for a example are a chef, and you tell your employee to create a dish.
    You would only settle on that perfect dish that you ask for. Not half of it. or the wrong one.
    But you could accept employee saying. Not I cant" because then you know, its not gonna happened.
    (and then you might need to rewrite the dish recipe)

     So the responses should always be the same on the task that matters to you.
     because that what you want, right? You dont want the Brain to turn on the lights in the kitchen when you
     asked about turning on the lights in the living room. Or if you for example swear in
     a sentence. You would prefer the chatbot to at least try understand what you want.
     Perhaps if that interpretation fails, because of bad rules, then you could let the bot response at its own
     request.

     Think of how you would like your environment to behave. Is it not more accurate to say that
     we dont want information that we didnt ask for. No one likes when some one is telling
     you things you didnt ask for. Or sent you advertising regarding sales you dont
     care about. Time is the value. And you dont want to loose it on things that doesnt matter.






























