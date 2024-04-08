import pygame
from gtts import gTTS
from io import BytesIO


def play_audio(text):
   
  # Create a gTTS object
  tts = gTTS(text=text, lang='es')

  speech_bytes = BytesIO()
  tts.write_to_fp(speech_bytes)
  
  # Load speech from BytesIO
  speech_bytes.seek(0)
  pygame.mixer.init()
  pygame.mixer.music.load(speech_bytes)
  pygame.mixer.music.play()

  # Wait until speech finishes
  while pygame.mixer.music.get_busy():
      continue
  






