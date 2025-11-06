# 🖼️ Paveikslėlių analizės programa su AI

Ši programa leidžia vartotojams įkelti paveikslėlius ir gauti jų detalų aprašymą naudojant dirbtinio intelekto modelį.

## ⚡ Funkcijos

- 📁 Paveikslėlių įkėlimas (PNG, JPG, JPEG, GIF, BMP, TIFF)
- 🤖 Automatinis paveikslėlio analizavimas su AI
- 🎨 Intuityvi web sąsaja su Streamlit
- 🔒 Vietinis AI modelis (duomenys neišsiunčiami į debesį)
- 🇱🇹 Aprašymai lietuvių kalba

## 🛠️ Reikalavimai

- Python 3.8 arba naujesnė versija
- Ollama programa
- gemma3:4b modelis

## 📦 Įdiegimas

### 1. Ollama įdiegimas

Atsisiųskite ir įdiekite Ollama iš: https://ollama.ai/

### 2. Modelio atsisiuntimas

```bash
ollama pull gemma3:4b
```

### 3. Python priklausomybių įdiegimas

```bash
pip install -r requirements.txt
```

## 🚀 Paleidimas

### 1. Paleiskite Ollama serverį

```bash
ollama serve
```

### 2. Paleiskite Streamlit programą

```bash
streamlit run app.py
```

### 3. Atidarykite naršyklę

Programa bus prieinama adresu: http://localhost:8501

## 📋 Naudojimo instrukcija

1. **Įkelkite paveikslėlį** - spustelėkite "Browse files" ir pasirinkite paveikslėlį
2. **Peržiūrėkite paveikslėlį** - patikrinkite, ar paveikslėlis įkeltas teisingai
3. **Analizuokite** - spustelėkite "🔍 Analizuoti paveikslėlį" mygtuką
4. **Gaukite rezultatus** - palaukite, kol AI pateiks paveikslėlio aprašymą

## 🔧 Techniniai duomenys

- **Frontend**: Streamlit
- **AI modelis**: Ollama gemma3:4b
- **Paveikslėlių apdorojimas**: Pillow (PIL)
- **Kalba**: Python

## ❗ Galimos problemos ir sprendimai

### Ollama neprisijungia
```bash
# Patikrinkite, ar Ollama veikia
ollama list

# Paleiskite Ollama serverį
ollama serve
```

### Modelis nerastas
```bash
# Atsisiųskite modelį
ollama pull gemma3:4b

# Patikrinkite atsisiųstus modelius
ollama list
```

### Priklausomybių problemos
```bash
# Atnaujinkite pip
python -m pip install --upgrade pip

# Įdiekite priklausomybes iš naujo
pip install -r requirements.txt --force-reinstall
```

## 🤝 Pagalba

Jei kyla problemų:
1. Patikrinkite, ar visi reikalavimai įvykdyti
2. Peržiūrėkite konsolės pranešimus apie klaidas
3. Užtikrinkite, kad Ollama serveris veikia

## 📄 Licencija

Ši programa sukurta mokymosi tikslais.