# digunakan untuk mengextract image
from PIL import Image

# reference
# ============
# https://www.geeksforgeeks.org/image-based-steganography-using-python/
# https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372
# https://www.geeksforgeeks.org/base64-b64encode-in-python/
# https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372

# digunakan untuk melakukan convert encoding data menjadi base64
def generate(data):
    # list untuk kode base64
    new = []

    for i in data:
        # base64 = 8-bit binary
        new.append(format(ord(i), '08b'))
    return new

# digunakan untuk melakukan modifikasi pixel sesuai dengan data base64
def modifikasi(pixel, data):
    list = generate(data)
    lenlist = len(list)
    imlist = iter(pixel)

    for i in range(lenlist):
        # melakukan extract sebanyak 3 pixel
        pixel = [value for value in imlist.__next__()[:3] + imlist.__next__()[:3] + imlist.__next__()[:3]]

        # value pada pixel harus dibuat menjadi odd 1 dan even 0
        for j in range(0,8):
            if list[i][j] == '0' and pixel[j]%2 != 0:
                pixel[j] -= 1

            elif list[i][j] == '1' and pixel[j]%2 == 0:
                if pixel[j] != 0:
                    pixel[j] -= 1
                else:
                    pixel[j] += 1
        
        # menentukan apakah akan melanjut membaca atau selesai/berhenti
        # 0 untuk melanjutkan dan 1 untuk selesai/berhenti
        if i == lenlist-1:
            if pixel[-1]%2 == 0:
                if pixel[-1] != 0:
                    pixel[-1] -= 1
                else:
                    pixel[-1] += 1
            else:
                if pixel[-1]%2 != 0:
                    pixel[-1] -= 1
            
            pixel = tuple(pixel)
            yield pixel[0:3]
            yield pixel[3:6]
            yield pixel[6:9]

# menaruh hasil modifikasi ke image baru
def nencode(nimg, data):
    # berisikan besar file image
    imgsize = nimg.size[0]
    # koordinat awal 
    (x,y) = (0,0)

    for px in modifikasi(nimg.getdata(), data):
        # menaruh pixel yang sudah diubah pada iamge baru
        nimg.putpixel((x,y), px)
        if x == imgsize-1:
            x = 0
            y += 1
        else:
            x += 1

# melakukan endode data mrnjadi image
def encode():
    img = input("Enter Image name with extention: ")
    image = Image.open(img, 'r')

    data = input("Enter data or text that want to be encoded: ")
    # mengecek agar data yang ingin di encode tidak kosong
    if len(data) == 0:
        raise ValueError('Data is empty, please enter data or text!')
    
    nimg = image.copy()
    nencode(nimg, data)

    newimg = input("Enter Image new name with extention: ")
    name = str(newimg.split(".")[1].upper())
    nimg.save(newimg, name)

# melakukan decoding pada data di Image
def decode():
    img = input("Enter Image name with extention: ")
    image = Image.open(img, 'r')

    data = ''
    dataimage = iter(image.getdata())

    while True:
        pixels = [value for value in dataimage.__next__()[:3] + dataimage.__next__()[:3] + dataimage.__next__()[:3]]

        # string dari encoding base64
        strbin = ''

        for i in pixels[:8]:
            if i%2 == 0:
                strbin += '0'
            else:
                strbin += '1'
        
        data += chr(int(strbin, 2))
        if pixels[-1]%2 != 0:
            return data

# digunakan untuk memilih fungsi yang ingin dijalankan encode atau decode
def main():
    print("\n::: Welcome to Steganography :::\n")
    print("1. Encode Image")
    print("2. Decode Image")
    menu = int(input(">> "))

    if menu == 1:
        encode()
    elif menu == 2:
       print("Encoded Text: \n" + decode())
    else:
        raise Exception("Enter between 1 or 2!")

if __name__ == '__main__':
    main()
