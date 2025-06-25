import streamlit as st
import json
import os
from datetime import datetime

st.set_page_config(page_title="ZGZO.AI Bid Generator", layout="centered")
st.title("📄 ZGZO.AI - AI Bid Generator")

# Load available GC profiles
st.subheader("1. Select GC Profile")
gc_dir = "gc_profiles"
gc_files = [f for f in os.listdir(gc_dir) if f.endswith("_config.json")]

if not gc_files:
    st.warning("No GC profiles found. Please create one in the Config Creator first.")
else:
    selected_gc = st.selectbox("Choose GC Profile", gc_files)

    # Upload spec or plan file
    st.subheader("2. Upload Specs or Drawings")
    uploaded_file = st.file_uploader("Upload PDF or DOCX file", type=["pdf", "docx"])

    if uploaded_file and selected_gc:
        # Load GC config
        with open(os.path.join(gc_dir, selected_gc), "r") as f:
            config = json.load(f)

        # Parse basic info
        st.success(f"Using profile: {config['gc_name']}")
        st.write(f"License #: {config['license']}")
        st.write(f"Markup: {config['markup_percent']}%")
        st.write(f"Tone: {config['tone'].capitalize()}")

        # Placeholder AI-generated scope
        st.subheader("3. Generated Scope of Work (Example)")
        st.markdown("""
        - Division 02: Selective demolition of tile and plumbing fixtures
        - Division 03: New slab pour for restroom flooring
        - Division 09: New ceramic wall tile and paint finishes
        - Division 15: Installation of ADA-compliant fixtures and hot water piping
        - Division 16: Relocate lighting, add occupancy sensors
        """)

        # Bid summary
        st.subheader("4. Bid Summary Output")
        st.write("✅ Cover Page with GC Branding")
        st.write("✅ CSI-formatted Scope of Work")
        st.write("✅ Timeline & Phases")
        st.write("✅ Inclusions / Exclusions")
        st.write("✅ Signature & Legal Section")

        # Export dummy output
        if st.button("Generate Bid (Demo)"):
            with open("ZGZO_AIBid_Example.docx", "w") as f:
                f.write("This is a placeholder DOCX bid file.")
            st.success("✅ Bid generated! (placeholder for now)")

st.markdown("---")
st.caption("ZGZO.AI - Built for General Contractors by Zane.")
