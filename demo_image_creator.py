import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

def create_demo_image():
    """Sukuria demonstracinį paveikslėlį testavimui"""
    # Sukuriame naują paveikslėlį
    width, height = 400, 300
    image = Image.new('RGB', (width, height), color='lightblue')
    draw = ImageDraw.Draw(image)
    
    # Pieškiame saulę
    draw.ellipse([320, 30, 370, 80], fill='yellow', outline='orange')
    
    # Pieškiame debesis
    draw.ellipse([50, 40, 120, 80], fill='white')
    draw.ellipse([80, 30, 150, 70], fill='white')
    
    # Pieškiame kalnus
    draw.polygon([(0, 180), (150, 120), (300, 160), (400, 140), (400, 300), (0, 300)], fill='green')
    
    # Pieškiame namą
    draw.rectangle([180, 160, 250, 220], fill='brown')
    draw.polygon([(170, 160), (215, 130), (260, 160)], fill='red')
    draw.rectangle([200, 190, 220, 220], fill='darkblue')
    
    # Pridedame tekstą
    try:
        font = ImageFont.load_default()
        draw.text((10, 10), "Demo paveikslėlis", fill='black', font=font)
    except:
        draw.text((10, 10), "Demo paveikslėlis", fill='black')
    
    # Konvertuojame į bytes
    img_bytes = io.BytesIO()
    image.save(img_bytes, format='PNG')
    img_bytes.seek(0)
    
    return img_bytes

if __name__ == "__main__":
    st.title("Demonstracinio paveikslėlio kūrimas")
    
    if st.button("Sukurti demo paveikslėlį"):
        demo_image = create_demo_image()
        
        # Parodyti paveikslėlį
        st.image(demo_image, caption="Demonstracinis paveikslėlis", width=400)
        
        # Atsisiuntimo mygtukas
        st.download_button(
            label="Atsisiųsti demo paveikslėlį",
            data=demo_image,
            file_name="demo_paveikslelis.png",
            mime="image/png"
        )