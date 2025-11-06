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
    
    # Inicializuojame session state
    if 'analysis_result' not in st.session_state:
        st.session_state.analysis_result = None
    if 'last_question' not in st.session_state:
        st.session_state.last_question = None
    
    st.title("🖼️ Paveikslėlių analizė su dirbtinio intelekto pagalba")
    st.markdown("---")
    
    # Paaiškinimas vartotojui
    st.markdown("""
    ### Kaip naudotis programa:
    1. 📁 Įkelkite paveikslėlį naudodami žemiau esantį mygtuką
    2. 💬 Užduokite klausimą apie paveikslėlį (nebūtina)
    3. 🔍 Spustelėkite "Analizuoti paveikslėlį"
    4. 📋 Gaukite detalų AI atsakymą
    
    **Pastaba:** Programa naudoja Ollama gemma3:4b modelį vietiniam paveikslėlių analizavimui.
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
            st.image(image, caption="Įkeltas paveikslėlis", width="stretch")
            
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
            
            # Klausimo įvedimo laukas
            user_question = st.text_area(
                "💬 Užduokite klausimą apie paveikslėlį (nebūtina):",
                placeholder="Pvz.: Kokia yra šio paveikslėlio nuotaika? Kiek žmonių matote? Kas vyksta paveikslėlyje?",
                height=100,
                help="Jei paliksite tuščią, AI pateiks bendrą paveikslėlio aprašymą"
            )
            
            # Pasirinkimas analizės tipo
            col2_1, col2_2 = st.columns(2)
            
            with col2_1:
                if st.button("🔍 Analizuoti paveikslėlį", type="primary"):
                    analyze_image(uploaded_file, image, user_question)
            
            with col2_2:
                if st.button("🆕 Išvalyti rezultatus"):
                    st.session_state.analysis_result = None
                    st.session_state.last_question = None
                    st.rerun()
            
            # Rodome ankstesnį rezultatą, jei yra
            if st.session_state.analysis_result:
                st.markdown("---")
                if st.session_state.last_question:
                    st.success(f"**Atsakymas į klausimą:** *{st.session_state.last_question}*")
                else:
                    st.success("**Bendras paveikslėlio aprašymas:**")
                
                st.write(st.session_state.analysis_result)

def analyze_image(uploaded_file, image, user_question=""):
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
        
        # Suformuojame prompt'ą pagal vartotojo klausimą
        if user_question.strip():
            prompt = f"Atsakyk į šį klausimą apie paveikslėlį: {user_question.strip()}. Atsakyk lietuvių kalba ir būk tikslus."
        else:
            prompt = 'Apibūdink šį paveikslėlį išsamiai ir tiksliai. Paminėk, ką matai paveikslėlyje: objektus, žmones, gyvūnus, spalvas, veiklas, aplinką, nuotaiką. Atsakyk lietuvių kalba.'
        
        # Siunčiame užklausą Ollama modeliui
        response = ollama.chat(
            model='gemma3:4b',
            messages=[{
                'role': 'user',
                'content': prompt,
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
        
        # Išsaugome rezultatą session state
        st.session_state.analysis_result = response['message']['content']
        st.session_state.last_question = user_question.strip()
        
        # Išvalome progreso indikatorius
        progress_bar.empty()
        status_text.empty()
        
        # Atvaizdavome rezultatą
        if user_question.strip():
            st.success(f"**Atsakymas į klausimą:** *{user_question.strip()}*")
        else:
            st.success("**Bendras paveikslėlio aprašymas:**")
        
        st.write(response['message']['content'])
        
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
    
    ### Klausimų pavyzdžiai
    - "Kokia yra šio paveikslėlio nuotaika?"
    - "Kiek žmonių matote paveikslėlyje?"
    - "Kokios spalvos dominuoja?"
    - "Kas vyksta paveikslėlyje?"
    - "Kokie objektai matomi?"
    - "Kur buvo daryta nuotrauka?"
    - "Kokia metų laikas?"
    
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