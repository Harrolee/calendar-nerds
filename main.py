# import Pydantic
from gen_image import generate_image
from gen_image_desc import generate_image_desc
from gen_calendar_desc import generate_calendar_description


rpt = {
    "prompt":"",
    "img": "",
    "imgDesc":"",
    "calDesc":""
}

prompt = "cam shredding gnar"
rpt["prompt"] = prompt

img_path = generate_image()
rpt["img"] = img_path

imgDesc = generate_image_desc()
rpt["imgDesc"] = imgDesc

calDesc = generate_calendar_description()
rpt["calDesc"] = calDesc


print(rpt)