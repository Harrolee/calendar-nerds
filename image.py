from PIL import Image    
# import requests

def generate_image():
    # write the image to a filepath

    url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/ai2d-demo.jpg"
    img = Image.open('ascend.png')
    path_to_image = "/Users/lee/calendarNerds/ascend.png"
    return img,path_to_image
