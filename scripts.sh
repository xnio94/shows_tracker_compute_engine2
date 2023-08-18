# make sure instance is debian 10


gcloud compute ssh snapchat-tracker


gcloud config set project libiti-d5972


gcloud compute instances get-serial-port-output snapchat-tracker --zone us-central1-c






sudo supervisorctl stop pythonapp

cd /opt/app
sudo -u pythonapp git pull origin main
sudo /opt/app/env/bin/pip install -r /opt/app/requirements.txt

sudo supervisorctl start pythonapp





sudo -u pythonapp sh -c 'echo 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 > OPENAI_API_KEY'














# other

sudo -u pythonapp git reset --hard HEAD
sudo -u pythonapp sed -i "s|OPENAI_API_KEY_PLACEHOLDER|'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'|g"  /opt/app/python-app.conf


echo "export OPENAI_API_KEY='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'" >> ~/.zshrc
source ~/.zshrc



