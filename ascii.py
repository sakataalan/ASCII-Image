import PIL.Image
import urllib.request
import os

asciiChars = ['@', '#', '$', '%', '?', '*', '+', ';', ':', ',', '.']

def resizeImage(image, newWidth=475):
    width, height = image.size
    ratio = height / width
    newHeight = int((newWidth * ratio)/2)
    resizedImage = image.resize((newWidth, newHeight))
    return resizedImage

def convertGrey(image):
    grayscaleImage = image.convert('L')
    return grayscaleImage 

def convertImageToAscii(image):
    pixels = image.getdata()
    characters = "".join([asciiChars[pixel//25] for pixel in pixels])
    return characters

def main(newWidth=475):
    path = input('Digite a URL da imagem: \n')
    
    try:
        urllib.request.urlretrieve(path, "image.jpg")
        image = PIL.Image.open('image.jpg')
    except:
        print('O endereço da imagem não é valido')

    newImageData = convertImageToAscii(convertGrey(resizeImage(image)))

    pixelCount = len(newImageData)
    asciiImage = '\n'.join(newImageData[i:(i+newWidth)] for i in range(0, pixelCount, newWidth))

    print("Pronto")
    os.remove("image.jpg")

    with open('ascii_image.txt', 'w') as f:
        f.write(asciiImage)

main()