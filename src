from PIL import Image
from transformers import TrOCRProcessor, VisionEncoderDecoderModel

MODEL_NAME = "microsoft/trocr-base-printed"

print("Loading OCR model...")

processor = TrOCRProcessor.from_pretrained(MODEL_NAME)
model = VisionEncoderDecoderModel.from_pretrained(MODEL_NAME)

image_path = "data/input/sample.jpg"

image = Image.open(image_path).convert("RGB")

pixel_values = processor(
    images=image,
    return_tensors="pt"
).pixel_values

generated_ids = model.generate(pixel_values)

text = processor.batch_decode(
    generated_ids,
    skip_special_tokens=True
)[0]

print("\n========== EXTRACTED TEXT ==========")
print(text)
print("====================================")

with open(
    "data/output/extracted_text.txt",
    "w",
    encoding="utf-8"
) as file:
    file.write(text)

print("\nText saved successfully!")
