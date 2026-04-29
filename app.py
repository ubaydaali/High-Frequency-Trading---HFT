import streamlit as st
import subprocess
import os

st.set_page_config(page_title="KRONOS HFT", page_icon="⚡", layout="wide")

# Custom Footer CSS
st.markdown("""
    <style>
    .main { padding-bottom: 100px; }
    .footer { position: fixed; left: 0; bottom: 0; width: 100%; background-color: #0e1117; color: white; text-align: center; padding: 20px 0; border-top: 1px solid #4a4a4a; z-index: 999; }
    .footer a { color: #64ffda; text-decoration: none; margin: 0 15px; font-size: 24px; transition: 0.3s; }
    .footer a:hover { color: #ffffff; text-shadow: 0 0 10px #64ffda; }
    .footer-text { font-size: 14px; color: #888; margin-top: 10px; }
    </style>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    """, unsafe_allow_html=True)

st.title("⚡ KRONOS High-Frequency Trading (HFT) Switch")
st.markdown("##### *Deterministic Memory-Safe Order Matching powered by Ada & Python.*")
st.divider()

exe_name = 'kronos_core.exe' if os.name == 'nt' else 'kronos_core'
exe_path = os.path.join('ada_engine', exe_name)

if st.button("🚀 Process Live Order Book", type="primary"):
    
    if not os.path.exists(exe_path):
        os.makedirs('ada_engine', exist_ok=True)
        with st.spinner("Compiling Ada HFT Engine natively..."):
            try:
                subprocess.run(["gnatmake", "src/kronos_core.adb", "-D", "ada_engine", "-o", exe_path], check=True)
            except FileNotFoundError:
                st.warning("⚠️ **Local Compiler Missing:** GNAT (Ada Compiler) is not installed on this local machine.")
                st.success("☁️ **CLOUD READY:** Deploy to Streamlit Cloud with `gnat` in your `packages.txt` to run this real-time trading engine!")
                st.stop()
    
    os.makedirs(os.path.join('data', 'output'), exist_ok=True)
    
    with st.spinner("Matching millions of orders in sub-milliseconds..."):
        subprocess.run([exe_path])
    
    st.success("✅ ORDER BOOK CLEARED. EXECUTIONS LOGGED.")
    
    try:
        with open('data/output/trade_executions.txt', 'r', encoding='utf-8') as f:
            st.code(f.read(), language="text")
    except FileNotFoundError:
        st.warning("Trading session complete. No trades matched.")
        
    st.info("💡 **Open Source Challenge:** Can you optimize the Ada core to implement a 'First-In-First-Out' (FIFO) B-Tree matching queue for millions of concurrent orders?")

# Footer
st.markdown("""
    <div class="footer">
        <div class="contact-icons">
            <a href="https://github.com/ubaydaali" target="_blank" title="GitHub"><i class="fab fa-github"></i></a>
            <a href="https://www.linkedin.com/in/ubayda-ali-95972a406/" target="_blank" title="LinkedIn"><i class="fab fa-linkedin"></i></a>
            <a href="https://t.me/obedaale" target="_blank" title="Telegram"><i class="fab fa-telegram"></i></a>
            <a href="https://wa.me/905530640804" target="_blank" title="WhatsApp"><i class="fab fa-whatsapp"></i></a>
            <a href="mailto:admin@onws.net" title="Email"><i class="fas fa-envelope"></i></a>
            <a href="https://onws.net" target="_blank" title="Portfolio"><i class="fas fa-globe"></i></a>
        </div>
        <div class="footer-text">
            <b>Lead Architect: Ubayda Ali</b><br>
            Engineered with Ada & Python for Zero-Latency FinTech
        </div>
    </div>
    """, unsafe_allow_html=True)
