from PIL import Image

img=Image.open('road (2).png')

resize=img.resize((430,322))

resize.save('realroad.png',quality=95)
