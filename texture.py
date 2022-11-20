import struct

def setColor(r, g, b):
    return bytes([int(b * 255), int(g * 255), int(r * 255)])

class Texture(object):

    def __init__(self, path):
        self.path = path
        self.read()

    def read(self):
        with open(self.path, "rb") as image:
            image.seek(2 + 4 + 2 + 2)
            header_size = struct.unpack("=l", image.read(4))[0]
            image.seek(2 + 4 + 2 + 2 + 4 + 4)
            self.width = struct.unpack("=l", image.read(4))[0]
            self.height = struct.unpack("=l", image.read(4))[0]
            image.seek(header_size)

            self.pixels = []
            for y in range(self.height + 1):
                self.pixels.append([])

                for x in range(self.width + 1):
                    b = ord(image.read(1))
                    g = ord(image.read(1))
                    r = ord(image.read(1))
                    
                    self.pixels[y].append(
                        setColor(r, g, b)
                    )

    def get_color(self, tx, ty):
        x = round(tx * self.width)
        y = round(ty * self.height)

        return self.pixels[y][x]

    def get_color_with_intensity(self, tx, ty, intensity):
        x = round(tx * self.width)
        y = round(ty * self.height)

        b = self.pixels[y][x][0] * intensity   
        g = self.pixels[y][x][1] * intensity   
        r = self.pixels[y][x][2] * intensity   

        return setColor(r, g, b)