from torchvision import models
import json

# mapping
imagenet_class_mapping = json.load(open('imagenet_class_index.json'))

# Make sure to pass `pretrained` as `True` to use the pretrained weights:
model = models.densenet121(pretrained=True)
# Since we are using our model only for inference, switch to `eval` mode:
model.eval()

def get_category(model, imagenet_class_mapping, image_path):
    with open(image_path, 'rb') as file:
        image_bytes = file.read()
    transformed_image = transform_image(image_bytes=image_bytes)
    outputs = model.forward(transformed_image)