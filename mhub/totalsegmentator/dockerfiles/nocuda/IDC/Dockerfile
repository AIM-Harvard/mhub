# Specify the base image for the environment
FROM mhubai/totalsegmentator:nocuda

# Install some basic system utilities
RUN apt update && apt install -y --no-install-recommends \
  curl\
  apt-transport-https\
  ca-certificates\
  gnupg\
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
  jupyter \
  ipykernel \
  ipython \
  ipywidgets\
  papermill\
  google-cloud-bigquery\
  google-cloud-storage\
  db_dtypes


COPY weights_download.sh /root/weights_download.sh
RUN chmod +x /root/weights_download.sh
RUN /root/weights_download.sh

ENV S5CMD_URL="https://github.com/peak/s5cmd/releases/download/v2.0.0/s5cmd_2.0.0_Linux-64bit.tar.gz"
ENV S5CMD_FN="s5cmd_2.0.0_Linux-64bit.tar.gz"

RUN wget ${S5CMD_URL}
RUN tar -xvzf ${S5CMD_FN}
RUN rm ${S5CMD_FN}
