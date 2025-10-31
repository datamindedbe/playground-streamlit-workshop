#! /usr/bin/env sh

export GOOGLE_APPLICATION_CREDENTIALS=/$PWD/key.json

uv run python -m streamlit run streamlit_app/main.py