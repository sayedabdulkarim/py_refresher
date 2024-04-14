from PIL import Image

mac = Image.open("../example.webp")

# print(type(mac))
print(mac.format_description)