README

 Rasberry Pi Setup:
 Base setup dep:
 pip install aiml
 pip install SpeechRecognition
 pip install pyvona
 pip install pyyaml
 extra:
 (FAILED) pip install pyaudio
    Min req. version 2.9
    - sudo apt-get install libportaudio0 libportaudio2 libportaudiocpp0 portaudio19-dev
    - sudo apt-get install python-dev
    - git clone http://people.csail.mit.edu/hubert/git/pyaudio.git
    - sudo python pyaudio/setup.py install

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

