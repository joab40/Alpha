# Alpha
Alpha alias sasha aka chacha is a Smart AI (aiml) chatterbot build in Python, which have several supported api / webservice dependencies.
In a near future Alpha will be hosted a RaspberryPi inserted in a robotic head.

### API Connections
#### Working OK
    - google speech STT API (SpeechRecognition)
    - google translate API
    - Pyvona API TTS
    - TelldusCenter "Tellstick" bourne shell scripts (Not inkluded) 
#### In progress ! Unstable
    - Raspberry PI GPIO (robotic motor and lights for the head)
    - Face and Voice recognition (RaspberryPI)
    - WebeHome (Home Security - webservice support)
    
## How it works
Advantages or disadvantages alpha is highly dependent on web services . Which may result in reduced privacy and security of a smart home solution.

## Installation
Unfortunately there is no boundle installation scripts available.
For Raspbarry se README in raspberrypi catalog

## Supported "verified" Hardware
 - Raspberry PI 2
 - Kinobo - "AKIRO" USB Microphone
 - DM500USB Microphone 

## Supported "verified" Software

## Inspired by
Alpha is pre name sascha. Is 


 Rasberry Pi Setup:
 Base setup dep:
```sh
pip install aiml
pip install SpeechRecognition
pip install pyvona
pip install pyyaml
```
 extra:
 (FAILED) pip install pyaudio
    Min req. version 2.9
    - sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
    - sudo apt-get install python-dev
    - git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
    - sudo python pyaudio/setup.py install

    apt-get install python-pygame (pyvonna)
    apt-get install flac (raspberry)

 DM500 USB MIC
    - sudo apt-get install alsa-utils mpg321
    - record from MIC: arecord -f S16_LE -D hw:1,0 -r 48000 test.wav
	- change hardware mic adress sudo vi /lib/modprobe.d/aliases.conf


sudo modprobe snd_bcm2835

 pip install wolframalpha

 Alpha, smart home AI. 
 sasha - My doughters imaginary friend "Chacha"

 sudo apt-get install python-pyaudio
 sudo apt-get install espeak
 sudo apt-get install jack-tools ant openjdk-6-jdk fftw3 qjackctl
 jackd -r -d alsa -r 44100 !?
 Follow: speech_recognition -> README for install
 sudo apt-get install python-pyaudio python3-pyaudio
 qjackctl gui stop | start jackdc

 YAML for reading config files
 -> install: pip install pyyaml
 API pip install wolframalpha -> https://pypi.python.org/pypi/wolframalpha


