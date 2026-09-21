import argparse
import os

from preprocessing import preprocess_image
from ocr import OCRModel


def main():
    parser = argparse.ArgumentParser(
        description="AI-powered Image-to-Text OCR"
    )

    parser.add_argument(
        "--image",
        required=True,
        help="Path to the input image"
    )

    parser.add_argument(
        "--output",
        default="data/output/extracted_text.txt",
        help="Path to save extracted text"
    )

    args = parser.parse_args()

    if not os.path.isfile(args.image):
        print(f"Error: Image not found - {args.image}")
        return

    try:
        print("\n======================================")
        print("   IMAGE-TO-TEXT INFERENCE USING AI")
        print("======================================")

        print("\n[1/3] Preprocessing image...")
        image = preprocess_image(args.image)

        print("[2/3] Loading Hugging Face OCR model...")
        ocr_model = OCRModel()

        print("[3/3] Extracting text...")
        extracted_text = ocr_model.extract_text(image)

        print("\n========== EXTRACTED TEXT ==========\n")

        if extracted_text:
            print(extracted_text)
        else:
            print("No readable text detected.")

        print("\n====================================")

        output_directory = os.path.dirname(args.output)

        if output_directory:
            os.makedirs(output_directory, exist_ok=True)

        with open(args.output, "w", encoding="utf-8") as file:
            file.write(extracted_text)

        print(f"\nText saved successfully to: {args.output}")

    except Exception as error:
        print(f"\nError while processing image: {error}")


if _name_ == "_main_":
    main()
