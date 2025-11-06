#!/usr/bin/env python3
"""
Ollama modelio patikrinimo skriptas
"""

import ollama
import sys

def check_ollama_connection():
    """Patikrina Ollama serverio ryšį"""
    try:
        # Pabandomе prisijungti prie Ollama
        models = ollama.list()
        print("✅ Sėkmingai prisijungta prie Ollama serverio")
        return True
    except Exception as e:
        print(f"❌ Nepavyko prisijungti prie Ollama serverio: {e}")
        print("Įsitikinkite, kad Ollama veikia. Paleiskite: ollama serve")
        return False

def check_model_availability():
    """Patikrina, ar gemma2:4b modelis yra prieinamas"""
    try:
        models = ollama.list()
        model_names = [model.get('name', model.get('model', '')) for model in models.get('models', [])]
        
        print("\n📋 Prieinami modeliai:")
        for name in model_names:
            print(f"  - {name}")
        
        # Tikriname, ar yra gemma3:4b modelis
        target_models = ['gemma3:4b', 'gemma3']
        found_model = None
        
        for target in target_models:
            for model_name in model_names:
                if target in model_name:
                    found_model = model_name
                    break
            if found_model:
                break
        
        if found_model:
            print(f"\n✅ Rastas modelis: {found_model}")
            return found_model
        else:
            print(f"\n❌ Modelis gemma3:4b nerastas")
            print("Atsisiųskite modelį: ollama pull gemma3:4b")
            return None
            
    except Exception as e:
        print(f"❌ Klaida tikrinant modelius: {e}")
        return None

def test_model(model_name):
    """Testuoja modelį su paprastu užklausos pavyzdžiu"""
    try:
        print(f"\n🧪 Testuojamas modelis: {model_name}")
        
        response = ollama.chat(
            model=model_name,
            messages=[{
                'role': 'user', 
                'content': 'Pasakyk "sveiki" lietuvių kalba.'
            }]
        )
        
        print("✅ Modelio testas sėkmingas!")
        print(f"Atsakymas: {response['message']['content']}")
        return True
        
    except Exception as e:
        print(f"❌ Modelio testas nepavyko: {e}")
        return False

def main():
    """Pagrindinė funkcija"""
    print("🔍 Ollama konfigūracijos patikrinimas")
    print("=" * 50)
    
    # 1. Tikriname ryšį
    if not check_ollama_connection():
        sys.exit(1)
    
    # 2. Tikriname modelius
    model_name = check_model_availability()
    if not model_name:
        sys.exit(1)
    
    # 3. Testuojame modelį
    if not test_model(model_name):
        sys.exit(1)
    
    print("\n🎉 Viskas konfigūruota teisingai!")
    print("Galite paleisti programą: streamlit run app.py")

if __name__ == "__main__":
    main()