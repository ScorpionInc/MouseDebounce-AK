#Author : SI
#Created: 20210315
#Updated: 20210315
#Purpose: Remove extra clicks from faulty mouse hardware input

#import libraries/modules
import time

#Define functions
def current_milli_time():
    #return system.exec_command('echo $(($(date +%s%N)/1000000))', getOutput=True)#Way slow
    return round(time.time() * 1000.0)#Returns float

#Allow Script to be enabled/disabled externally
if store.has_key("RunMouseDebounce"):
    running = store.get_value("RunMouseDebounce")
else:
    running = True
    store.set_global_value("RunMouseDebounce", running)
#Get or set default settings
if store.has_key("MouseDebouncerMinDelay"):
    minDelay = store.get_value("MouseDebouncerMinDelay")
else:
    minDelay = 250.0
    store.set_global_value("MouseDebouncerMinDelay", minDelay)
#retCode, user = dialog.info_dialog(title='DEBUG', message='Loaded Setings. Running: '+str(running)+'\tMinDelay: '+str(minDelay))
lastTime = current_milli_time()
#retCode, user = dialog.info_dialog(title='DEBUG', message='Last Click: '+str(lastTime))
while running:
    mouse.wait_for_click(1, timeOut=99999999999999999999999999)#Couldn't find an infinite wait in AutoKey
    nextTime = current_milli_time()
    #retCode, user = dialog.info_dialog(title='DEBUG', message='Next Click: '+str(nextTime))
    nextDelta = (nextTime - lastTime)
    #retCode, user = dialog.info_dialog(title='DEBUG', message='Delta: '+str(nextDelta))
    if (nextDelta >= minDelay):
        mouse.click_relative_self(0, 0, 1)
        lastTime = nextTime
    else:
        print('\a')
        continue
