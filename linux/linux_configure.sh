. linux_configure_for_remote_server.sh

echo '### install chrome ###'
wget -O ~/Downloads/chrome.deb https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i ~/Downloads/chrome.deb
sudo apt install -f
rm ~/Downloads/chrome.deb

echo '### instal vscode ###'
wget -q https://packages.microsoft.com/keys/microsoft.asc -O- | sudo apt-key add
sudo add-apt-repository "deb [arch=amd64] https://packages.microsoft.com/repos/vscode stable main"
sudo apt update
sudo apt install code


echo '### install sublime text ###'
wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | sudo apt-key add
sudo apt-add-repository "deb https://download.sublimetext.com/ apt/stable/"
sudo apt install sublime-text

