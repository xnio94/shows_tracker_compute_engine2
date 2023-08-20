
# ***
sudo apt update

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
sudo apt --fix-broken install -y
wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
sudo mv chromedriver /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver


# or ***

sudo apt update ; wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb ; sudo dpkg -i google-chrome-stable_current_amd64.deb ; sudo apt --fix-broken install -y ; wget https://chromedriver.storage.googleapis.com/114.0.5735.90/chromedriver_linux64.zip ; unzip chromedriver_linux64.zip ; sudo mv chromedriver /usr/bin/chromedriver ; sudo chown root:root /usr/bin/chromedriver ; sudo chmod +x /usr/bin/chromedriver
