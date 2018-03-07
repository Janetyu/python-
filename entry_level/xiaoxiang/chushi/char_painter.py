from PIL import Image
#字符画
ascii_char = list(r"$@&%B#=-. ")

#选择字符填充
def select_ascii_char(r,g,b):
    gray = int((19595 * r + 38469 * g + 7472 * b) >> 16)
    unit = 256.0/len(ascii_char)
    return ascii_char[int(gray/unit)]

#获取图像，把图像转换成字符，并返回
def output(imgpath,width=100,height=100):
    im = Image.open(imgpath)
    im = im.resize((width,height),Image.NEAREST)
    txt = ""

    for h in range(height):
        for w in range(width):
            txt += select_ascii_char(*im.getpixel((w,h))[:3])
        txt += '\n'
    return txt

def main():
    imgpath = r"C:\Users\ASUS\Desktop\常用\产品.png"
    txt = output(imgpath)
    print(txt)
    
main()
