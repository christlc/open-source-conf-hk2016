
import Image, time, serial, sys
# Adapt from https://gist.github.com/ladyada/3309494
# Configurable values
filename  = "hello.gif"
filename = sys.argv[1]
skip = sys.argv[2]
brightness = sys.argv[]3
baseHeight = 30
# Open SPI device, load image in RGB format and get dimensions:

print "Loading..."
img       = Image.open(filename).convert("RGB")
heightPercent = (baseHeight / float(img.size[1]))
width = int((float(img.size[0]) * float(heightPercent)))
img = img.resize((width, baseHeight),Image.BILINEAR)
pixels    = img.load()
width     = img.size[0]
height    = img.size[1]
print "%dx%d pixels" % img.size
# To do: add resize here if image is not desired height

 
# Create list of bytearrays, one for each column of image.
# R, G, B byte per pixel, plus extra '0' byte at end for latch.
print "Allocating..."
column = [0 for x in range(width)]
for x in range(width):
	column[x] = bytearray(height * 3 + 1)
 
# Convert 8-bit RGB image into column-wise GRB bytearray list.
print "Converting..."
for x in range(width):
	for y in range(height):
		value = pixels[x, y]
                y3 = y * 3
 		column[x][y3]     = int(float(value[0]) * float(brightness))
		column[x][y3 + 1] = int(float(value[1]) * float(brightness))
		column[x][y3 + 2] = int(float(value[2]) * float(brightness))
# Then it's a trivial matter of writing each column to the SPI port.
ser = serial.Serial('/dev/ttyACM0', 38400)
#sleep for a short time until serial is established
time.sleep(1)
print "Start in 1 second!"
time.sleep(1)
print "Displaying..."
while True:
	for x in range(width):
            for y in reversed(range(height)):
                y3 = y * 3
                ser.write(''+chr(column[x][y3])+chr(column[x][y3+1])+chr(column[x][y3+2]))
            time.sleep(float(skip))
        #write empty string to clear color
        for y in range(height):
            for i in range(3):
                ser.write(chr(0)+'')
        break
