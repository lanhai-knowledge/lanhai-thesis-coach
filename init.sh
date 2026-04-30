#!/usr/bin/env bash
set -e

if [ ! -d ".venv" ]; then
  echo "Creating Python venv..."
  python3 -m venv .venv
fi

source .venv/bin/activate
pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet

echo ""
echo "Setup complete. Run:"
echo "  source .venv/bin/activate"
echo "  streamlit run app.py"
