#! /usr/bin/env sh

# Install pinned version of uv
curl -LsSf https://astral.sh/uv/0.9.6/install.sh | sh

# Go folder level down and install dependencies
cd $PWD/demo-app
uv sync

# Get this from ⚠️ public Google Cloud bucket
curl $PUBLIC_BUCKET_GOOGLE_KEY > $PWD/key.json

# Go back up a folder level
cd ..