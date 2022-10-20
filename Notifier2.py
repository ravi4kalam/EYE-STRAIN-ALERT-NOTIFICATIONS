from winotify import Notification,audio
import time
while True:
    toast=Notification(app_id="Hello Achiever !",
                       title="Take A Break! ",
                       msg="Since 40 mins you are on screen . It effects your eyes ",
                       duration="long",
                       icon=r"D:\break.jpg")
    toast.set_audio(audio.LoopingCall2,loop=True)
    time.sleep(2400) #40 minutes i.e 2400 seconds
    toast.show()



