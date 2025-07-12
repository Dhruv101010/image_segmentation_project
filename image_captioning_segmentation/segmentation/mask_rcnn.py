import torch
from torchvision.models.detection import maskrcnn_resnet50_fpn
from torchvision import transforms as T
from PIL import Image
import numpy as np
import cv2

def load_model():
    model = maskrcnn_resnet50_fpn(pretrained=True)
    model.eval()
    return model

def segment_image(image_path, threshold=0.8):
    model = load_model()
    image = Image.open(image_path).convert("RGB")
    transform = T.Compose([T.ToTensor()])
    img_tensor = transform(image)

    with torch.no_grad():
        pred = model([img_tensor])[0]

    np_img = np.array(image)
    for box, score in zip(pred["boxes"], pred["scores"]):
        if score > threshold:
            box = box.detach().numpy().astype(int)
            cv2.rectangle(np_img, (box[0], box[1]), (box[2], box[3]), (0, 255, 0), 2)

    return Image.fromarray(np_img)