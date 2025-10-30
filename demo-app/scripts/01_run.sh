#! /usr/bin/env bash

export GOOGLE_APPLICATION_CREDENTIALS=/workspaces/playground-streamlit-hack-and-beers/demo-app/key.json
poetry run python -m streamlit run streamlit_app/main.py