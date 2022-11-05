import openai
from PIL import Image
import requests
from io import BytesIO
import dotenv as dotenv
import os

dotenv.load_dotenv()

key = os.getenv("OPENAI-SECRET")
openai.api_key = key
a = True
while a == True:
    p = input("prompt:(q to escape) ")
    if p == "q":
        a = False
    else:
        response = openai.Image.create(
          prompt=p,
          n=1,
          size="1024x1024"
        )
        image_url = response['data'][0]['url']
        print(image_url)
        res = requests.get(image_url)
        img = Image.open(BytesIO(res.content))
        img.show()
