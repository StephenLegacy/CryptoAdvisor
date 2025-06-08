#!/bin/bash
python3 -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
echo "Environment ready. Run with: source venv/bin/activate && streamlit run app.py"
