import fitz  # PyMuPDF

def compress_pdf(input_pdf, output_pdf, image_quality=50):
    pdf_document = fitz.open(input_pdf)

    for page_number in range(len(pdf_document)):
        page = pdf_document[page_number]
        images = page.get_images(full=True)

        for img_index, image in enumerate(images):
            xref = image[0]  # Reference ID of the image
            base_image = pdf_document.extract_image(xref)

            image_bytes = base_image["image"]
            image_ext = base_image["ext"]

            # Compress the image
            from PIL import Image
            from io import BytesIO

            with Image.open(BytesIO(image_bytes)) as img:
                img = img.convert("RGB")
                output_buffer = BytesIO()
                img.save(output_buffer, format="JPEG", quality=image_quality)
                new_image_bytes = output_buffer.getvalue()

            # Replace the image in the PDF
            pdf_document.update_stream(xref, new_image_bytes)

    pdf_document.save(output_pdf)
    pdf_document.close()

# Example usage
input_pdf = "D:\\1_16034893728.pdf"
output_pdf = "D:\\outrput.pdf"
compress_pdf(input_pdf, output_pdf, image_quality=50)

