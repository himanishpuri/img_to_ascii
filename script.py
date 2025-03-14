from PIL import Image
import os

def img_to_py(image : str, type: str, saveas: str, scale: str) -> None:
    scale = int(scale)
    
    img = Image.open(image)
    w, h = img.size
    
    img.resize((w // scale, h // scale)).save("mod.%s" % type)
    
    img = Image.open("mod.%s" % type)
    w, h = img.size
    
    grid = list()
    for i in range(h):
        grid.append(["X"] * w)
        
    pix = img.load()
    
    for y in range(h):
        for x in range(w):
            if sum(pix[x, y]) == 0:
                grid[y][x] = "#"
            elif sum(pix[x,y]) in range(1,100):
                grid[y][x] = "X"
            elif sum(pix[x,y]) in range(100,200):
                grid[y][x] = "%"
            elif sum(pix[x,y]) in range(200,300):
                grid[y][x] = "&"
            elif sum(pix[x,y]) in range(300,400):
                grid[y][x] = "*"
            elif sum(pix[x,y]) in range(400,500):
                grid[y][x] = "+"
            elif sum(pix[x,y]) in range(500,600):
                grid[y][x] = "/"
            elif sum(pix[x,y]) in range(600,700):
                grid[y][x] = "("
            elif sum(pix[x,y]) in range(700,750):
                grid[y][x] = "'"
            else:
                grid[y][x] = " "
    
    asc = open(saveas, "w")
    
    for row in grid:
        asc.write("".join(row) + "\n")
    
    asc.close()
    
    os.unlink("mod.%s" % type)

if __name__ == "__main__":
    # path = input("Enter Image Path: ")
    img_to_py("test.jpg", "jpg", "test.txt", "5")