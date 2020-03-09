# Written by Matthew Hill
# Steganography : Finding an image inside another image
# Use .bmp format images of the same dimension 


from PIL import Image

im = Image.open("---") #Add location of the image you want to exract a secret image from
pix1 = im.load()
width, height = im.size

for x in range(0, width):
    for y in range(0, height):
        R,G,B = pix1[x,y]
        # Remove the MSB components of each RBG value and shift the 4 LSB into the MSB which will reveal the hidden image
        R1 = (R & 15)<<4
        G1 = (G & 15)<<4
        B1 = (B & 15)<<4
        pix1[x,y] = (R1,G1,B1)

im.save("---") #Add the location and the name of the revealed secret
print("finished")

