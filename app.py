import streamlit as st
import ollama
from PIL import Image
import base64
import io
import os

def main():
    """Pagrindinė programos funkcija"""
    st.set_page_config(
        page_title="Paveikslėlių analizė su AI",
        page_icon="🖼️",
        layout="wide"
    )
    
    st.title("🖼️ Paveikslėlių analizė su dirbtinio intelekto pagalba")
    st.markdown("---")
    
    # Paaiškinimas vartotojui
    st.markdown("""
    ### Kaip naudotis programa:
    1. Įkelkite paveikslėlį naudodami žemiau esantį mygtuką
    2. Palaukite, kol dirbtinis intelektas išanalizuos paveikslėlį
    3. Gaukite detalų paveikslėlio aprašymą
    
    **Pastaba:** Programa naudoja Ollama gemma2:4b modelį vietiniam paveikslėlių analizavimui.
    """)
    
    st.markdown("---")
    
    # Paveikslėlio įkėlimo widget'as
    uploaded_file = st.file_uploader(
        "Įkelkite paveikslėlį analizei",
        type=['png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'],
        help="Palaikomi formatai: PNG, JPG, JPEG, GIF, BMP, TIFF"
    )
    
    if uploaded_file is not None:
        # Sukuriame du stulpelius paveikslėlio ir rezultato atvaizdavimui
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("📁 Įkeltas paveikslėlis:")
            # Atvaizduojame paveikslėlį
            image = Image.open(uploaded_file)
            st.image(image, caption="Įkeltas paveikslėlis", width='stretch')
            
            # Parodome paveikslėlio informaciją
            st.info(f"""
            **Failo informacija:**
            - Pavadinimas: {uploaded_file.name}
            - Dydis: {uploaded_file.size} baitų
            - Formatas: {image.format}
            - Matmenys: {image.size[0]} × {image.size[1]} pikselių
            """)
        
        with col2:
            st.subheader("🤖 AI analizės rezultatas:")
            
            # Sukuriame mygtuką analizei
            if st.button("🔍 Analizuoti paveikslėlį", type="primary"):
                analyze_image(uploaded_file, image)

def analyze_image(uploaded_file, image):
    """Analizuoja paveikslėlį naudojant Ollama modelį"""
    
    # Progreso juostos atvaizdavimas
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    try:
        status_text.text("🔄 Ruošiamas paveikslėlis analizei...")
        progress_bar.progress(25)
        
        # Konvertuojame paveikslėlį į base64 formatą
        image_bytes = io.BytesIO()
        
        # Konvertuojame į RGB, jei reikia (nes Ollama geriau dirba su RGB)
        if image.mode in ('RGBA', 'LA', 'P'):
            image = image.convert('RGB')
        
        image.save(image_bytes, format='JPEG', quality=85)
        image_bytes.seek(0)
        
        # Užkoduojame į base64
        image_b64 = base64.b64encode(image_bytes.getvalue()).decode()
        
        progress_bar.progress(50)
        status_text.text("🤖 Siunčiama užklausa dirbtinio intelekto modeliui...")
        
        # Siunčiame užklausą Ollama modeliui
        response = ollama.chat(
            model='gemma3:4b',
            messages=[{
                'role': 'user',
                'content': 'Apibūdink šį paveikslėlį išsamiai ir tiksliai. Paminėk, ką matai paveikslėlyje: objektus, žmones, gyvūnus, spalvas, veiklas, aplinką, nuotaiką. Atsakyk lietuvių kalba.',
                'images': [image_b64]
            }],
            options={
                'temperature': 0.7,
                'top_p': 0.9,
                'num_predict': 300
            }
        )
        
        progress_bar.progress(100)
        status_text.text("✅ Analizė baigta!")
        
        # Atvaizdavome rezultatą
        st.success("**Paveikslėlio aprašymas:**")
        st.write(response['message']['content'])
        
        # Išvalome progreso indikatorius
        progress_bar.empty()
        status_text.empty()
        
    except Exception as e:
        progress_bar.empty()
        status_text.empty()
        
        # Klaidų apdorojimas
        if "connection" in str(e).lower():
            st.error("""
            ❌ **Klaida: Nepavyko prisijungti prie Ollama serverio**
            
            Patikrinkite:
            1. Ar Ollama veikia jūsų kompiuteryje
            2. Ar gemma2:4b modelis yra atsisiųstas
            
            Paleiskite terminale:
            ```
            ollama serve
            ollama pull gemma2:4b
            ```
            """)
        elif "model" in str(e).lower():
            st.error("""
            ❌ **Klaida: Modelis gemma3:4b nerastas**
            
            Atsisiųskite modelį terminale:
            ```
            ollama pull gemma3:4b
            ```
            """)
        else:
            st.error(f"❌ **Nenumatyta klaida:** {str(e)}")

# Šoninė juosta su papildoma informacija
def show_sidebar():
    """Atvaizdoja šoninę juostą su informacija"""
    st.sidebar.title("ℹ️ Informacija")
    
    st.sidebar.markdown("""
    ### Apie programą
    Ši programa naudoja:
    - **Streamlit** - web sąsajai
    - **Ollama** - vietiniam AI modeliui
    - **gemma3:4b** - paveikslėlių analizei
    
    ### Reikalavimai
    - Paleistas Ollama serveris
    - Atsisiųstas gemma3:4b modelis
    
    ### Paleidimo instrukcijos
    1. `ollama serve`
    2. `ollama pull gemma3:4b`
    3. `streamlit run app.py`
    """)
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("**Sukurta su ❤️ naudojant Python**")

if __name__ == "__main__":
    show_sidebar()
    main()