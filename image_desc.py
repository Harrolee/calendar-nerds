# from transformers import pipeline
import ollama

# url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/transformers/tasks/ai2d-demo.jpg"

# image = Image.open(requests.get(url, stream=True).raw)
# prompt = "USER: <image>\nWhat does the label 15 represent? (1) lava (2) core (3) tunnel (4) ash cloud\nASSISTANT:"
# outputs = pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200})
# print(outputs)
# >>> {"generated_text": "\nUSER: What does the label 15 represent? (1) lava (2) core (3) tunnel (4) ash cloud\nASSISTANT: Lava"}



class Image_Description:

    def __init__(self):
        ...
        # model_id = "llava-hf/llava-1.5-7b-hf"
        # self.pipe = pipeline("image-to-text", model=model_id)

    def generate(self, image):
        prompt = "Describe the content of this image to someone who has not seen the image itself"
        # call to image-to-text llm
        # return self.pipe(image, prompt=prompt, generate_kwargs={"max_new_tokens": 200})
        return ollama.generate(model='llava', prompt=prompt, images=["camInYarn.png"])
