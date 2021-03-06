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
