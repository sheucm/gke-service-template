gcloud config set project XXX-XXX-XXX
gcloud secrets versions access latest --secret="adc" >> /root/.config/gcloud/application_default_credentials.json
mkdir /root/.ssh
gcloud secrets versions access latest --secret="xxx_pri_key" >> /root/.ssh/id_rsa
chmod 400 /root/.ssh/id_rsa
ssh-keyscan -H xxx.xxx.xxx.xxx >> /root/.ssh/known_hosts
ssh-keyscan -H xxx.xxx.xxx.xxx >> /root/.ssh/known_hosts

python3 -m myapp.main