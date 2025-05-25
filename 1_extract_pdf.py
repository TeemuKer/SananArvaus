import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

# Aseta tiedoston nimi oikein tähän
pdf_path = os.path.join("oma_gpt2_malli", "teksti_1.pdf")  # VAIHDA tiedostonimi oikeaksi!
raw_text = extract_text_from_pdf(pdf_path)

with open("train.txt", "w", encoding="utf-8") as f:
    f.write(raw_text)

print("Teksti tallennettu train.txt-tiedostoon.")
