from epdlib import Screen, Layout, Block
from PIL import Image, ImageDraw, ImageFont

# setup epd
s = Screen(epd="HD", vcom=-1.98, mode="L")
s.clearEPD()


def partial(image):
    s.writeEPD(image, partial=True)


# for x in range(0, 10):
#     l.update_block_props('head', { 'bkground': gray(16), 'fill': gray(0), 'hcenter': False }, force_recalc=True)
#     l.update_contents({'head': 'Todo List'})
#     partial(l)

#     time.sleep(3)

#     l.update_block_props('head', { 'bkground': gray(0), 'fill': gray(16), 'hcenter': True}, force_recalc=True)
#     l.update_contents({'head': '!!!NEW MESSAGE!!!'})
#     partial(l)
#     time.sleep(3)

    # l.update_block_props('mid', {'bkground': gray(16)})
    # l.update_contents({'mid': ' '})
    # s.writeEPD(l.concat(), partial=True)
    #
    # l.update_contents({'mid': ' '})
    # s.writeEPD(l.concat(), partial=True)

    # l.update_contents({'mid': 'Read Book'})
    # s.writeEPD(l.concat(), partial=True)

    # l.update_contents({'bottom': ' '})
    # s.writeEPD(l.concat(), partial=True)
# with Image.open('./a.png').convert('RGBA') as base:
#     fnt = ImageFont.truetype("./fira.ttf", 40)
#     txt = Image.new("RGBA", base.size, (255, 255, 255, 0))
    
#     d = ImageDraw.Draw(txt)

#     # draw text, half opacity
#     d.text((10, 10), "Hello", font=fnt, fill=(255, 255, 255, 255))
#     # draw text, full opacity
#     d.text((10, 60), "World", font=fnt, fill=(255, 255, 255, 128))

#     out = Image.alpha_composite(base, txt)

#     s.writeEPD(out, partial=False)


#     s.writeEPD(out, partial=True)



# image.thumbnail(s.resolution)


# time.sleep(5)

# image.thumbnail(s.resolution)
# s.writeEPD(image, partial=True)

# myScreen.initEPD()
# myScreen.writeEPD('./my_image.png')