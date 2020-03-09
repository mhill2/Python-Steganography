# Written by Matthew Hill
# Steganography : Hiding an image inside another image
# Use .bmp format images of the same dimension 


from PIL import Image

im = Image.open("---") #Add secret image location
# The secret image has been loaded
pix1 = im.load()
width, height = im.size
for y in range(0, height):
    for x in range(0, width): #for every pixel of the image
        R,G,B = pix1[x,y]
        # We need to remove the LSB from each RGB components and shift the MSBs into this 4 bit space
        R1 = (R & 240)>>4
        G1 = (G & 240)>>4
        B1 = (B & 240)>>4
        # The 4 least significant bits of the red, green and blue bytes are now 0, the 4 MSB were then shifted to the right, therefore becoming the 4 LSB
        pix1[x,y] = (R1,G1,B1)



im = Image.open("---") #Add carrier image location
# The carrier image has been loaded
pix2 = im.load()
width2, height2 = im.size
if width == width2 and height == height2:
    for y in range(0, height2):
        for x in range(0, width2): #for every pixel in the image
            R,G,B = pix2[x,y]
            R1,G1,B1 = pix1[x,y]
            # Same process as before except now we replace the zeroed LSBs with the data from the secret image
            R2 = (R & 240)|R1
            G2 = (G & 240)|G1
            B2 = (B & 240)|B1
            # The 4 LSB of each RVB value of every pixel from the carrier image have been replaced by the 4 MSB of each RGB value from every pixel of the secret image
            pix2[x,y] = (R2,G2,B2)


    im.save("---") #Add the location where you want the image to be saved along with the name
    print("The Image has been hidden in another image")
else:
    print("The images are not the same size!")
# You should be able to see the new image in the location 
# The secret image will now be hidden in the old image