import math 

class Pixel:
    def __init__(self, red, green, blue):
        self.red = red
        self.green = green
        self.blue = blue


class Image:
    def __init__(self, width = 0, height = 0):
        self._bitsPerPixel = 24
        self._width = width
        self._height = height
        self._pixelMatrix = []
        self._rowSize = math.ceil(self._width / 4) * 4
        self._path = ""
        self._fileSize = 0
        for i in range(width):
            row = []
            for j in range(height):
                row.append(Pixel(255, 255, 255))
            self._pixelMatrix.insert(0, row)

    def getWidth(self):
        return self._width

    def getHeight(self):
        return self._height

    def setPixel(self, pixel, pozX, pozY):
        self._pixelMatrix[pozX][pozY] = pixel

    def getPixel(self, pozX, pozY):
        return self._pixelMatrix[pozX][pozY]
    
    def open(self, path):
        self._path = path
        self._handleBMPRead()
    
    def save(self, path):
        self._path = path
        self._handleBMPWrite()

    def _handleBMPRead(self):
        bmpFile = open(self._path, "rb")

        bmpFile.seek(2) #go to the file size bytes
        self._fileSize = int.from_bytes(bmpFile.read(4), "little")

        bmpFile.seek(18) #go to width and height bytes
        self._width = int.from_bytes(bmpFile.read(4), "little")
        self._height = int.from_bytes(bmpFile.read(4), "little")

        bmpFile.seek(28) #go to bits per pixel
        self._bitsPerPixel = int.from_bytes(bmpFile.read(2), "little")
        
        bmpFile.seek(54) # go to pixels
        self._rowSize = math.ceil(self._width / 4) * 4
        row = []
        for i in range(self._width):
            row = []
            for j in range(self._height):
                b = int.from_bytes(bmpFile.read(1), "little")
                g = int.from_bytes(bmpFile.read(1), "little")
                r = int.from_bytes(bmpFile.read(1), "little")
                row.append(Pixel(r, g, b))
            if self._rowSize - self._width != 0:
                bmpFile.read(self._rowSize - self._width) # read the row padding
            self._pixelMatrix.insert(0, row)
        bmpFile.close()

    def _handleBMPWrite(self):
        bmpFile = open(self._path, "wb")
        bmpFile.write(b'BM') # write B and M bytes
        fileSize = 54 + (self._rowSize * self._height)
        bmpFile.write(fileSize.to_bytes(4, "little")) # write the size of the file
        bmpFile.write(b'\x00\x00\x00\x00') # write the reserved bytes
        bmpFile.write((54).to_bytes(4, "little")) # write the pixel offset
        bmpFile.write((40).to_bytes(4, "little")) # write size of information header
        bmpFile.write(self._width.to_bytes(4, "little")) # write width
        bmpFile.write(self._height.to_bytes(4, "little")) # write height
        bmpFile.write((1).to_bytes(2, "little")) # write number of planes
        bmpFile.write(self._bitsPerPixel.to_bytes(2, "little")) # write bits per pixel
        bmpFile.write((0).to_bytes(4, "little")) # write compression (no compression)
        bmpFile.write((0).to_bytes(4, "little")) # write compression size (none)
        bmpFile.write((2835).to_bytes(4, "little")) # write X pixels per meter
        bmpFile.write((2835).to_bytes(4, "little")) # write Y pixels per meter
        bmpFile.write((0).to_bytes(4, "little")) # colors used = 0
        bmpFile.write((0).to_bytes(4, "little")) # important colors = 0
        for i in range(self._height-1, -1, -1):
            for j in range(self._width):
                bmpFile.write(self._pixelMatrix[i][j].blue.to_bytes(1, "little"))
                bmpFile.write(self._pixelMatrix[i][j].green.to_bytes(1, "little"))
                bmpFile.write(self._pixelMatrix[i][j].red.to_bytes(1, "little"))
            if self._rowSize - self._width != 0:
                bmpFile.write((0).to_bytes(self._rowSize - self._width, "little"))

        


        