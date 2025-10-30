# curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
# tar -xf google-cloud-cli-linux-x86_64.tar.gz
# mkdir -p /workspaces/tools
# mv google-cloud-sdk/ /workspaces/tools/google-cloud-sdk
# /workspaces/tools/google-cloud-sdk/install.sh --quiet
# echo 'PATH=/workspaces/tools/google-cloud-sdk/bin:$PATH' >> ~/.bashrc
# rm google-cloud-cli-*
# . ~/.bashrc

# Install pinned version of uv
curl -LsSf https://astral.sh/uv/0.9.6/install.sh | sh

# Go folder level down and install dependencies
cd $PWD/demo-app
uv sync

# Get this from ⚠️ public Google Cloud bucket
curl $PUBLIC_BUCKET_GOOGLE_KEY > $PWD/key.json

# Go back up a folder level
cd ..