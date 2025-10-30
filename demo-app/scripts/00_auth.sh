curl -O https://dl.google.com/dl/cloudsdk/channels/rapid/downloads/google-cloud-cli-linux-x86_64.tar.gz
tar -xf google-cloud-cli-linux-x86_64.tar.gz
mkdir -p /workspaces/tools
mv google-cloud-sdk/ /workspaces/tools/google-cloud-sdk
/workspaces/tools/google-cloud-sdk/install.sh --quiet
echo 'PATH=/workspaces/tools/google-cloud-sdk/bin:$PATH' >> ~/.bashrc
rm google-cloud-cli-*
. ~/.bashrc

#curl [TODO] > key.json