import tkinter as tk
from transformers import pipeline, set_seed
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from tkinter import filedialog


current_prediction = ""


# Globaali generointimalli
generator = None

# Aseta siemen satunnaisuudelle
set_seed(42)

# Mallien nimet (huom. lisää oma mallisi mukaan)
MODELS = {
    "DistilGPT2 (EN, kevyt)": "distilgpt2",
    "GPT2-Medium (EN, parempi)": "gpt2-medium",
    "Suomi GPT2 (Finnish-NLP)": "Finnish-NLP/gpt2-finnish",
    "Oma malli (hienosäädetty)": "oma_gpt2_malli"
}

# Mallin vaihto
def load_model(model_name):
    global generator
    status_label.config(text=f"Ladataan mallia: {model_name}...")
    root.update()
    try:
        generator = pipeline("text-generation", model=model_name)
        status_label.config(text=f"Aktiivinen malli: {model_name}")
    except Exception as e:
        status_label.config(text=f"Virhe ladattaessa: {e}")

# Tallennus PDF
def save_text_as_pdf():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        status_label.config(text="Ei tallennettavaa tekstiä.")
        return

    file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF Files", "*.pdf")],
        title="Tallenna PDF-tiedostona"
    )
    if not file_path:
        return

    try:
        c = canvas.Canvas(file_path, pagesize=A4)
        width, height = A4
        margin = 50
        y = height - margin
        lines = text.split('\n')

        for line in lines:
            c.drawString(margin, y, line)
            y -= 15
            if y < margin:
                c.showPage()
                y = height - margin

        c.save()
        status_label.config(text=f"PDF tallennettu: {file_path}")
    except Exception as e:
        status_label.config(text=f"Virhe tallennettaessa: {e}")

# Ennustus
def predict_next_word(prompt_text):
    global current_prediction
    if not generator:
        current_prediction = ""
        return "Ei mallia ladattu"
    try:
        generated = generator(
            prompt_text,
            max_new_tokens=5,
            num_return_sequences=1,
            temperature=0.7,
            top_k=50,
            top_p=0.95,
            do_sample=True
        )
        generated_text = generated[0]['generated_text']
        next_words = generated_text[len(prompt_text):].strip().split()
        for word in next_words:
            if word.isalpha():
                current_prediction = word
                return word
        current_prediction = next_words[0] if next_words else ""
        return current_prediction
    except Exception as e:
        current_prediction = ""
        return f"Virhe: {e}"


# Syötteen muutos
def on_key_release(event):
    input_text = text_input.get("1.0", tk.END).strip()
    if input_text:
        next_word = predict_next_word(input_text)
        prediction_label.config(text=f"Ehdotus: {next_word}")
    else:
        prediction_label.config(text="Ehdotus: ...")


def on_tab_press(event):
    global current_prediction
    if current_prediction:
        text_input.insert(tk.INSERT, " " + current_prediction)
        current_prediction = ""
        prediction_label.config(text="Ehdotus: ...")
        return "break"  # estää oletustoiminnon (sisennys)


# Luo käyttöliittymä
root = tk.Tk()
root.title("Seuraavan sanan ennustaja")

# Asetetaan taustaväri koko ikkunalle
root.configure(bg="#e6f0fa")  # vaalea siniharmaa

# Fonttiasetukset
label_font = ("Helvetica", 14)
button_font = ("Helvetica", 11)

# Tekstisyötekenttä
text_input = tk.Text(root, height=10, width=60, font=("Helvetica", 12), bg="#ffffff", bd=2, relief="groove")
text_input.pack(padx=20, pady=(20,10))
text_input.bind("<KeyRelease>", on_key_release)
text_input.bind("<Tab>", on_tab_press)

# Ennusteteksti
prediction_label = tk.Label(root, text="Ehdotus: ...", font=label_font, bg="#e6f0fa", fg="#003366")
prediction_label.pack(pady=(5, 15))

# Tallennuspainike
save_button = tk.Button(root, text="Tallenna PDF", command=save_text_as_pdf, font=button_font, bg="#d9edf7", relief="raised")
save_button.pack(pady=(0, 10))

# Mallinvalintapainikkeet
button_frame = tk.Frame(root, bg="#e6f0fa")
button_frame.pack(pady=(0, 15))

for label, model_name in MODELS.items():
    btn = tk.Button(button_frame, text=label, command=lambda m=model_name: load_model(m),
                    font=button_font, bg="#cce5ff", relief="groove")
    btn.pack(side=tk.LEFT, padx=5)

# Tila-teksti mallin lataukselle
status_label = tk.Label(root, text="Valitse kielimalli.", fg="#004085", bg="#e6f0fa", font=("Helvetica", 10, "italic"))
status_label.pack(pady=(0, 10))


root.mainloop()