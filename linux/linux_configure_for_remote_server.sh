sudo apt update
sudo apt upgrade -y

sudo apt autoremove -y

sudo apt install wget
sudo apt install make

echo '### install and configure git ###'
sudo apt install git -y
git config --global user.name ArtemErmulin
git config --global user.email artem.ermulin@ya.ru

echo '### install \'bashmarks\' ###'
git clone git://github.com/huyng/bashmarks.git ~/Downloads/bashmarks
cd ~/Downloads/bashmarks
make install
cd
echo $'# bashmarks\nsource ~/.local/bin/bashmarks.sh\n' >> ~/.bashrc

echo '### install pyenv and python version ###'
sudo apt install gcc -y
sudo apt install curl -y
sudo apt install git-core -y
sudo apt install gcc -y
sudo apt install zlib1g-dev -y
sudo apt install libbz2-dev -y
sudo apt install libreadline-dev -y
sudo apt install libsqlite3-dev -y
sudo apt install libssl-dev -y
sudo apt install libffi-dev -y
sudo apt install liblzma-dev -y
git clone https://github.com/pyenv/pyenv.git $HOME/.pyenv
git clone https://github.com/yyuu/pyenv-virtualenv.git   $HOME/.pyenv/plugins/pyenv-virtualenv
echo $'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo $'export PATH="$PYENV_ROOT/bin:$PATH"\n' >> ~/.bashrc
echo $'if command -v pyenv 1>/dev/null 2>&1; then' >> ~/.bashrc
echo $'  eval "$(pyenv init -)"' >> ~/.bashrc
echo $'fi' >> ~/.bashrc

echo '### remove conflict alias ###'
sed -i 's/alias l=/#alias l=/g' ~/.bashrc

source ~/.bashrc

echo '### install python 3.7.9 ###'
pyenv install 3.7.7
pyenv global 3.7.7
pip install --upgrade pip
