from PIL import Image, ImageDraw
import math

img = Image.open("4.jpg")
draw = ImageDraw.Draw(img)
img.show()
w = img.size[0]
h = img.size[1]
pix = img.load()
filterK = (255 + 255 + 255)*0.1


for i in range(w):
    for j in range(h):
        if (j < h-1):
            Sn = pix[i,j][0] + pix[i,j][1] + pix[i,j][2]
            Sn1 = pix[i,j+1][0] + pix[i,j+1][1] + pix[i,j+1][2]
            if (math.fabs(Sn - Sn1) > filterK):
                draw.point((i,j), (190,0,0))
            else:
                draw.point((i,j), (255,255,255))
img.save("res.jpg", "JPEG")
res = Image.open("res.jpg")
res.show()