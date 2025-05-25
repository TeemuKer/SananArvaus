# Sanan ennustaja – GPT-2-pohjainen kielimalliprojekti

Tässä projektissa rakennettiin järjestelmä, joka osaa ennustaa käyttäjän kirjoittaman tekstin seuraavan sanan. Käytössä on neljä GPT-2-malliin perustuvaa vaihtoehtoa – mukaan lukien yksi itse koulutettu malli.

## Tavoite
Tutkia, kuinka hyvin kielimalli voi oppia yksilöllistä kieltä ja tyyliä, sekä vertailla esikoulutettuja ja itse hienosäädettyjä malleja käytännön tilanteessa.

## Projektin ominaisuudet
- PDF-tekstin purku ja esikäsittely (`1_extract_pdf.py`)
- GPT-2-mallin hienosäätö omalla datalla (`2_finetune_gpt2.py`)
- Tkinter-käyttöliittymä tekstinsyöttöön ja mallin valintaan (`sananarvaus.py`)
- Mahdollisuus tallentaa kirjoitettu teksti PDF-tiedostoksi
- TAB-näppäimen toiminto: lisää mallin ehdottama sana tekstikenttään

## Käytössä olevat kielimallit
- DistilGPT2 (kevyt englanninkielinen)
- GPT2-Medium (laajempi englanninkielinen)
- Finnish GPT2 (Finnish-NLP)
- **Oma hienosäädetty GPT-2**, koulutettu käyttäjän PDF-tekstillä

## Tiedostorakenne
├── 1_extract_pdf.py # PDF-tekstin purku
├── 2_finetune_gpt2.py # Mallin koulutus
├── sananarvaus.py # Käyttöliittymä
├── train.txt # PDF:stä saatu teksti
├── oma_gpt2_malli/ # Koulutettu malli
└── sanaarvausNotebook.ipynb # Notebook-dokumentti


## Käyttöohjeet
1. Aja `1_extract_pdf.py` valitsemallasi PDF-tekstillä
2. Kouluta malli ajamalla `2_finetune_gpt2.py`
3. Käynnistä graafinen käyttöliittymä ajamalla `sananarvaus.py`
4. Valitse haluamasi malli ja kirjoita teksti
5. Käytä TAB-näppäintä lisätäksesi mallin ehdottaman sanan tekst
6. Tallenna kirjoitettu teksti PDF-tiedostoksi painamalla "Tallenna PDF" -painiketta


## Tulokset ja havaintoja:
- Oma malli tuottaa selvästi parempia ennusteita, kun syöte muistuttaa koulutusdataa

- GPT2-medium toimii yleiskielessä parhaiten, mutta ei erikoistu tyyliin

- Finnish-NLP-malli ei osaa ennustaa englanninkielistä tekstiä

## Teknologiat ja kirjastot:
- Python

- Hugging Face Transformers

- datasets

- PyPDF2

- Tkinter

- reportlab

## Mahdolliset jatkokehitysideat:

- Useamman PDF:n käyttö koulutusdatana

- Automaattinen mallin valinta

- Hyperparametrien optimointi (GridSearch)
