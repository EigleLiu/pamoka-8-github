# Testavimo pavyzdžiai

## Programos testavimo eiga

### 1. Prieš pradedant
- Įsitikinkite, kad Ollama veikia: `ollama serve`
- Patikrinkite, ar modelis atsisiųstas: `ollama list`
- Jei modelio nėra: `ollama pull gemma3:4b`

### 2. Paleidimas
```bash
streamlit run app.py
```
arba
```bash
paleisti.bat  # Windows
```

### 3. Testavimo scenarijai

#### Sėkmingas testavimas:
1. Atidarykite http://localhost:8501
2. Įkelkite paveikslėlį (PNG, JPG, JPEG)
3. Spustelėkite "Analizuoti paveikslėlį"
4. Palaukite AI atsakymo

#### Galimi paveikslėlių tipai testavimui:
- **Portretas** - žmonių nuotraukos
- **Gamta** - peizažai, gyvūnai
- **Objektai** - namų apyvokos daiktai
- **Architektūra** - pastatai, tiliai
- **Maistas** - valgių nuotraukos

### 4. Klaidų diagnozavimas

#### "Nepavyko prisijungti prie Ollama"
```bash
# Paleiskite Ollama
ollama serve

# Patikrinkite, ar veikia
ollama list
```

#### "Modelis nerastas"
```bash
# Atsisiųskite modelį
ollama pull gemma3:4b

# Alternatyvūs modeliai
ollama pull gemma3:2b  # mažesnis
ollama pull llama3.2-vision  # geresnis paveikslėliams
```

#### Lėtas atsakymas
- Tikėtina su dideliais paveikslėliais
- Pabandykite mažesnį paveikslėlį
- Patikrinkite kompiuterio našumą

### 5. Tikėtini rezultatai

Programa turėtų pateikti detalų paveikslėlio aprašymą lietuvių kalba, pvz.:
- "Šiame paveikslėlyje matau..."
- "Paveikslėlyje vaizduojama..."
- Objektų, spalvų, veiksmų aprašymas
- Atmosferos ir nuotaikos komentarai