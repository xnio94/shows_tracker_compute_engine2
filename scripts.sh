# make sure instance is debian 10


gcloud compute ssh snapchat-tracker


gcloud config set project libiti-d5972


gcloud compute instances get-serial-port-output snapchat-tracker --zone us-central1-c






sudo supervisorctl stop pythonapp

cd /opt/app
sudo -u pythonapp git pull origin main
sudo /opt/app/env/bin/pip install -r /opt/app/requirements.txt


sudo supervisorctl start pythonapp










