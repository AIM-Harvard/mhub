# Specify the base image for the environment
FROM mhubai/totalsegmentator:nocuda

# Install some basic system utilities
RUN apt update && apt install -y --no-install-recommends \
  apt-transport-https\
  ca-certificates\
  curl\
  gnupg\
  subversion\
  zip\
&& rm -rf /var/lib/apt/lists/*


#Install the Google Cloud SDK (gcloud) to enable gsutil 
RUN echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg]\
            http://packages.cloud.google.com/apt cloud-sdk main" |\
            tee -a /etc/apt/sources.list.d/google-cloud-sdk.list \
&& curl https://packages.cloud.google.com/apt/doc/apt-key.gpg |\
   apt-key --keyring /usr/share/keyrings/cloud.google.gpg  add -\
&& apt-get update -y && apt-get install google-cloud-cli -y

# Install jupyter utilities (specify version if necessary)
RUN pip3 install --no-cache-dir \
  db_dtypes\
  google-cloud-bigquery\
  google-cloud-storage\
  ipykernel \
  ipython \
  ipywidgets\
  jupyter\
  papermill\
  thedicomsort\
  yamlmagic
