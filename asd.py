from PIL import Image, ImageDraw

im = Image.new('RGB', (200, 200), color=('#FAACAC'))
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (100, 100),
    'Test Text',
    fill=('#1C0606')
    )
im.show()
