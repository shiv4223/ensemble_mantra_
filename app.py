import streamlit as st
from PIL import Image, ImageOps
import os
import json
import base64

# --------- PAGE CONFIG ---------
st.set_page_config(page_title="Ensemble Mantra", layout="wide")

# --------- SIDEBAR NAV ---------
page = st.sidebar.radio("Our Pages", ["Home", "Instagram Feed"])

# --------- BASE64 IMAGE LOADER ---------
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# --------- CSS STYLES ---------  #e6b3d1;
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&family=Playfair+Display:ital@1&display=swap');

        html, body, [data-testid="stApp"] {
            background-color: #ffffff;
            font-family: 'Open Sans', sans-serif;
            color: #111;
        }

        @media (prefers-color-scheme: dark) {
            html, body, [data-testid="stApp"] {
                background-color: #0e0e0e;
                color: #f0f0f0;
            }

            .title-font {
                color: #e6b3d1; 
            }

            .subtitle {
                color: #cccccc;
            }

            .desc-container {
                color: #dddddd;
                border-top: 1px solid #444;
            }

            .collection-title {
                color: #eeeeee;
            }

            .whatsapp-btn {
                background-color: #823c6e;
                color: #fff;
            }

            .whatsapp-btn:hover {
                background-color: #a85c8f;
            }

            .footer-section {
                background-color: #1e1e1e;
            }

            .footer {
                color: #cccccc;
            }

            .social-links a {
                color: #89bfff;
            }

            .slider img {
                border: 2px solid #333;
            }
        }

        .title-font {
            font-family: 'Great Vibes', cursive;
            color: #111111;
            font-size: 3rem;
            text-align: center;
            margin-bottom: 0.2em;
        }

        .subtitle {
            font-size: 1.2rem;
            color: #555;
            text-align: center;
            font-style: italic;
            margin-bottom: 2rem;
        }

        .slider-wrapper {
            width: 100%;
            overflow: hidden;
            max-height: 320px;
            margin: 1rem auto 3rem auto;
            border-radius: 12px;
        }

        .slider {
            display: flex;
            animation: scroll 24s linear infinite;
            width: max-content;
        }

        .slider img {
            width: 400px;
            height: 300px;
            object-fit: cover;
            object-position: top;
            margin-right: 8px;
            border-radius: 12px;
        }

        @keyframes scroll {
            0% { transform: translateX(0); }
            30% { transform: translateX(-33.33%); }
            60% { transform: translateX(-66.66%); }
            100% { transform: translateX(0); }
        }

        .collection-title {
            text-align: center;
            font-size: 2rem;
            font-weight: 600;
            margin: 3rem 0 1.5rem;
            color: #000;
        }

        .desc-container {
            margin-top: 2rem;
            margin-bottom: 2.5rem;
            padding-top: 1rem;
            border-top: 1px solid #ddd;
            font-family: 'Playfair Display', serif;
            font-style: italic;
            font-weight: 400;
            font-size: 1.05rem;
            color: #444;
            text-align: center;
            line-height: 1.6;
        }

        .whatsapp-btn {
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 10px;
            background-color: #cccccc;
            color: white;
            font-weight: bold;
            border: none;
            padding: 0.8rem 1.8rem;
            border-radius: 30px;
            text-decoration: none;
            font-size: 1.1rem;
            margin: 2rem auto;
            width: fit-content;
        }

        .whatsapp-btn:hover {
            background-color: #999999;
        }

        .whatsapp-btn img {
            width: 20px;
        }

        .footer-section {
            background-color: #cccccc;
            padding: 40px 20px;
            margin-top: 60px;
        }

        .footer {
            text-align: center;
            font-size: 0.95rem;
            color: #444;
        }

        .social-links {
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 25px;
            margin-top: 20px;
        }

        .social-links a {
            display: flex;
            align-items: center;
            text-decoration: none;
            color: #0077cc;
            font-weight: 600;
            font-size: 1rem;
        }

        .social-links img {
            width: 22px;
            margin-right: 8px;
        }

        .brand-tag {
            display: block;
            margin: 0 auto 0.1rem auto;
            height: 250px;
        }

        @media screen and (max-width: 768px) {
            .slider img {
                width: 90vw;
                height: 200px;
            }

            .collection-title {
                font-size: 1.5rem;
            }

            .desc-container {
                font-size: 0.9rem;
                margin-top: 1.5rem;
                margin-bottom: 2rem;
            }

            .social-links {
                flex-direction: column;
                align-items: center;
                gap: 15px;
            }

            .brand-tag {
                height: 30px;
            }
        }
    </style>
""", unsafe_allow_html=True)

# ============ PAGE HEADER ============
def render_header():
    if os.path.exists("data/tag_updated.png"):
        st.markdown(f'<img class="brand-tag" src="data:image/jpeg;base64,{get_base64_image("data/tag_updated.png")}" />', unsafe_allow_html=True)

# ============ HOME PAGE ============
if page == "Home":
    render_header()
    st.markdown('<div class="title-font">Ensemble Mantra Boutique</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Where Elegance Meets Tradition</div>', unsafe_allow_html=True)

    # SLIDER
    slider_folder = "data/slider"
    if os.path.exists(slider_folder):
        slider_images = sorted([f for f in os.listdir(slider_folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))])
        if slider_images:
            slider_html = '<div class="slider-wrapper"><div class="slider">'
            for filename in slider_images:
                full_path = os.path.join(slider_folder, filename)
                encoded_image = get_base64_image(full_path)
                slider_html += f'<img src="data:image/jpeg;base64,{encoded_image}" />'
            slider_html += '</div></div>'
            st.markdown(slider_html, unsafe_allow_html=True)
        else:
            st.warning("No slider images found.")
    else:
        st.error("Missing folder: data/slider")

    # COLLECTION TITLE
    st.markdown('<div class="collection-title">Our Latest Collection</div>', unsafe_allow_html=True)

    # IMAGE GALLERY
    with open("data/descriptions.json", "r") as f:
        descriptions = json.load(f)

    image_folder = "data/images"
    image_files = sorted(os.listdir(image_folder))
    standard_size = (350, 470)

    for i in range(0, len(image_files), 3):
        cols = st.columns(3)
        for j in range(3):
            if i + j < len(image_files):
                img_path = os.path.join(image_folder, image_files[i + j])
                image = Image.open(img_path)
                image = ImageOps.fit(image, standard_size, method=Image.LANCZOS)
                with cols[j]:
                    st.markdown(
                        f'<div class="desc-container">{descriptions.get(image_files[i + j], "")}</div>',
                        unsafe_allow_html=True
                    )
                    st.image(image, use_container_width=True)

    # WHATSAPP BUTTON
    st.markdown("""
        <a href="https://wa.me/917529016888" target="_blank" class="whatsapp-btn">
            <img src="https://cdn-icons-png.flaticon.com/512/733/733585.png" />
            Contact Us on WhatsApp
        </a>
    """, unsafe_allow_html=True)

    # FOOTER
    st.markdown("""
        <div class="footer-section">
            <div class="footer">
                📍 Ensemble Mantra Fashion Studio & Boutique  
                <br>Address - 69D, Road, Power Colony, Model Town, Patiala, Punjab 147001  
                <br>📞 +91-9999999999  
                <div class="social-links">
                    <a href="https://www.instagram.com/ensemble_mantra_boutique/" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" /> @ensemblemantra
                    </a>
                    <a href="https://www.facebook.com/profile.php?id=100066463165402" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/1384/1384005.png" /> Ensemble Mantra
                    </a>
                    <a href="https://www.youtube.com/@ensemble_mantra?feature=shared" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" /> Ensemble Mantra
                    </a>
                    <a href="https://maps.app.goo.gl/xayjWyNRqdZbRue7A?g_st=ic" target="_blank">
                        <img src="https://cdn-icons-png.flaticon.com/512/684/684908.png" /> Google Maps
                    </a>
                </div>
            </div>
        </div>
    """, unsafe_allow_html=True)

# ============ INSTAGRAM FEED ============
elif page == "Instagram Feed":
    render_header()
    st.markdown('<div class="title-font">Instagram Feed</div>', unsafe_allow_html=True)
    st.markdown("""
        <div class="subtitle">
            <a href="https://www.instagram.com/ensemble_mantra_boutique/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384031.png" width="20px" />
                @ensemblemantra
            </a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <iframe src="https://www.juicer.io/api/feeds/boutique_ensemble_112/iframe" width="100%" height="900" frameborder="0" allowfullscreen></iframe>
    """, unsafe_allow_html=True)
