from epdlib import Screen

from layout import Layout
import os
import time

##
screenshots="./screenshots"
for file in os.listdir(screenshots):
    file_path = os.path.join(screenshots, file)
    os.unlink(file_path)

def partial(image):
    screenshot_name = str(time.time()) + '.jpg'
    image.save(os.path.join(screenshots, screenshot_name))
##

DUMMY_TASK_LIST=['Meditation', 'Workout', "Finish Task CP-15786", "Read Book Foobar", "This is the longest tasks that should be done asap"]
resolution = (1448, 1072)

start = time.time()
layout = Layout(resolution)
print('Layout', time.time() - start)

start = time.time()
layout.initBody(DUMMY_TASK_LIST)
print('initBody', time.time() - start)

layout.renderBody()

partial(layout.render())
