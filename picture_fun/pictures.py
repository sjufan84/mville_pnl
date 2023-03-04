import os
import openai
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import json
from PIL import Image
from io import BytesIO






openai.api_key = os.getenv("OPENAI_KEY")
openai.organization = os.getenv("OPENAI_ORG")

generate_image_button = st.button("Generate Image")
if generate_image_button:
    # Read the image file from disk and resize it
    image1 = Image.open("./pictures/sandal.png")
    image_2 = Image.open("./pictures/sandal2.png")
    width, height = 256, 256
    image1 = image1.resize((width, height))
    image2 = image_2.resize((width, height))

    # Convert image1 to a BytesIO object
    buffered = BytesIO()
    image1.save(buffered, format="PNG")
    # Convert image2 to a BytesIO object
    buffered2 = BytesIO()
    image2.save(buffered2, format="PNG")

    # Read the image data into a byte array
    byte_array = buffered.getvalue()
    byte_array2 = buffered2.getvalue()


    response = openai.Image.create_edit(
    prompt = "A smokey old fashioned floating on a cloud next to a large blue sandal",
    image=byte_array,
    mask = byte_array2,
    n=1,
    size="1024x1024",
    response_format = "url"
    )

    # Save the response in json format to a dictionary
    response_dict = json.loads(response)

    # Export the dictionary to a json file
    with open('response.json', 'w') as f:
        json.dump(response_dict, f)





    
    