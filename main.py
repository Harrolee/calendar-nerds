# import Pydantic
from image import generate_image
from image_desc import Image_Description
from calendar_desc import generate_calendar_description


rpt = {
    "prompt":"",
    "img": "",
    "imgDesc":"",
    "calDesc":""
}

prompt = "cam shredding gnar"
rpt["prompt"] = prompt

# almost there
img,img_path = generate_image()
rpt["img"] = img_path

# check
imgDesc = Image_Description()
imgDesc = imgDesc.generate(img)
rpt["imgDesc"] = imgDesc

calDesc = generate_calendar_description()
rpt["calDesc"] = calDesc


print(rpt)