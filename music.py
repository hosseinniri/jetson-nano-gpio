from pygame import mixer  # Load the popular external library

mixer.init()
mixer.music.load('/home/hossein/jetson-nano-gpio/41.mp3')
mixer.music.play()