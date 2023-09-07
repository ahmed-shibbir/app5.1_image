
import requests

url = "https://free-images.com/sm/05c6/benediktbeuern_und_benediktenwand.jpg"

response = requests.get(url)
print(response)

# image_data = response.text
# print(image_data)

image_data = response.content
print(image_data)

with open("image.jpg", 'wb') as file:
    file.write(image_data)