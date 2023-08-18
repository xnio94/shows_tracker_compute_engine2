# make sure instance is debian 10


gcloud compute ssh snapchat-tracker


gcloud config set project libiti-d5972


gcloud compute instances get-serial-port-output snapchat-tracker --zone us-central1-c






sudo supervisorctl stop pythonapp

cd /opt/app
sudo -u pythonapp git reset --hard HEAD
sudo -u pythonapp git pull origin main
sudo -u pythonapp sed -i "s|OPENAI_API_KEY_PLACEHOLDER|'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'|g"  /opt/app/python-app.conf

sudo /opt/app/env/bin/pip install -r /opt/app/requirements.txt


sudo supervisorctl start pythonapp










