from PIL import Image

mac = Image.open("../example.webp")

# print(type(mac))
# print(mac.format_description)

# 
# print(mac.crop(0,0,100,100))
# print(mac.crop((0, 0, 100, 100)))

crop_mac = mac.crop((0, 0, 500, 500))

# To display the cropped image
crop_mac.show()