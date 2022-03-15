from gtts import gTTS
from playsound import playsound
a = input()
b = input()
a = int(a)
b = int(b)
hap = a + b
cha = a - b
gop = a * b
nng = a / b
text = hap,cha,gop,nng
tts = gTTS(str(text),lang="ko")
tts.save("test.mp3")
playsound("test.mp3") 