from PIL import Image
import random

# CONFIGURATION
key = 12345
colourPlane = 2
significantBit = 7

stegoImage = "stego-image.bmp"

# READ IMAGE
image = Image.open(stegoImage).convert("RGB")

dimensions = image.size
pixels = image.load()

# TOTAL PIXELS
total_pixels = dimensions[0] * dimensions[1]

# SHUFFLE PIXELS
shuffledIndices = list(range(total_pixels))

random.seed(key)
random.shuffle(shuffledIndices)

# EXTRACT BITS
extractedBits = []

for i in shuffledIndices:

    x = i % dimensions[0]
    y = i // dimensions[0]

    p = format(pixels[x, y][colourPlane], 'b').zfill(8)

    extractedBits.append(p[significantBit])

# EXTRACT MESSAGE LENGTH
extractedLengthBits = extractedBits[:14]

extractedLength = int(''.join(extractedLengthBits), 2)

# REBUILD SECRET
extractedSecretASCII = []

for i in range(extractedLength):

    a = 0

    for j in range(7):

        a += int(extractedBits[14 + i * 7 + j]) * (2 ** (6 - j))

    extractedSecretASCII.append(chr(a))

# PRINT SECRET
secret = ''.join(extractedSecretASCII)

print("Extracted Secret:")
print(secret)