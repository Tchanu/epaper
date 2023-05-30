fontpath="./fonts/FiraCode-Regular.ttf"

def gray(x):
    if x < 0 and x > 16: raise Exception('Invalid color ' + x)
    return (16*x, 16*x, 16*x)

initialLayout = {
            'head': {
                'type': 'TextBlock',
                'text': 'Tasks',
                'image': None,
                'max_lines': 1,
                'width': 1,
                'height': .1,
                'abs_coordinates': (0, 0),
                'hcenter': False,
                'vcenter': True,
                'relative': False,
                'font_size': None,
                'padding': 8,
                'font': str(fontpath),
                'fill': gray(16),
                'bkground': gray(0),
                'mode': 'L',
                'border_config': {
                    "sides": ["bottom"],
                    "fill": 0,
                    "width": 2
                }
            },
            'body': {                       # text only block
                'type': 'ImageBlock',
                'width': 1,                  # 1/1 of the width - this stretches the entire width of the display
                'height': .6,               # 1/3 of the entire height
                'abs_coordinates': (0, None),   # this block is the key block that all other blocks will be defined in terms of
                'hcenter': False,             # horizontally center text
                'vcenter': True,             # vertically center text 
                'relative': ['body', 'head'],
                'bkground': gray(16),
                'mode': 'L',
            },
            'bottom': {
                'type': 'TextBlock',
                'text': 'Bottom',
                'image': None,
                'max_lines': 4,
                'width': 1,
                'height': .3,
                'abs_coordinates': (0, None),   # X = 0, Y will be calculated
                'hcenter': False,
                'vcenter': False,
                'font': str(fontpath),
                'relative': ['bottom', 'body'],# use the X postion from abs_coord from `artist` (this block: 0)
                                                # calculate the y position based on the size of `title` block
                
                # 'fill': (255, 255, 255),
                'bkground': gray(16),
                'mode': 'L',
                'border_config': {
                    "sides": ["top"],
                    "fill": 0,
                    "width": 2
                }
            }
    } 
bodyItemLayout = {
            'type': 'TextBlock',
            'image': None,
            'text': 'Hello World',
            'max_lines': 1,
            'width': 1,
            'height': .1,
            'abs_coordinates': (0, 0),
            'hcenter': False,
            'vcenter': True,
            'padding': 4,
            'font': str(fontpath),
            # 'fill': (255, 255, 255),
            'bkground': gray(16),
            'mode': 'L',
            'relative': False,
            'border_config': {
                "sides": ["top"],
                "fill": 0,
                "width": 1
            }
        }
