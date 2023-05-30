from epdlib import Layout as EPDLayout
from theme import initialLayout, bodyItemLayout
import time

class Layout:
    layout = None
    lbody = None
    resolution = None
    def __init__(self, resolution):
        self.resolution = resolution
        self.layout = EPDLayout(resolution=resolution, mode='L', layout=initialLayout)


    def initBody(self, taskList): 
        bodyResolution=(int(self.resolution[0]*initialLayout['body']['width']), int(self.resolution[1]*initialLayout['body']['height']))

        bodyLayout={}
        for key, item in enumerate(taskList):
            name='item' + str(key)
            bodyLayoutItem = bodyItemLayout.copy()
            bodyLayoutItem['text'] = "> " + item
            
            if key == 0:
                # remove border
                bodyLayoutItem['border_config'] = {}
            else:
                # make relative to the item above
                bodyLayoutItem['abs_coordinates'] = (0, None)
                bodyLayoutItem['relative'] = [name, 'item' + str(key - 1)]
            bodyLayout[name] = bodyLayoutItem

        self.lbody = EPDLayout(resolution=bodyResolution, mode='L', layout=bodyLayout)

    def renderBody(self):
        self.layout.update_contents({ 'body': self.lbody.concat() })

    def render(self):
        return self.layout.concat()
