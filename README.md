# ascii-proxy
A proxy that converts images in html to ascii

INSTALL
raspberry pi w/raspbian:

OS DEPENDENCIES:
sudo apt-get install git
sudo apt-get install jp2a
sudo apt-get install imagemagick
sudo apt-get install libssl-dev
sudo apt-get install python-dev libxml2-dev libxslt-dev
sudo apt-get install libssl-dev

PYPY:
cd /opt/
sudo curl -O https://bitbucket.org/pypy/pypy/downloads/pypy-2.6.0-linux-armhf-raspbian.tar.bz2
sudo tar xjf pypy-2.6.0-linux-armhf-raspbian.tar.bz2
sudo ln -s pypy-2.6.0-linux-armhf-raspbian pypy
sudo chown -R pi: pypy-2.6.0-linux-armhf-raspbian

CREATE VIRTUALENV:
cd ~
virtualenv -p /opt/pypy/bin/pypy ~/pypy_env
source ~/pypy_env/bin/activate

PYTHON DEPENDENCIES:
pip install -r requirements.txt

RUN:
cd ~/ascii-proxy
mitmdump --anticache -s ascii_images.py 

USE TEXT BROWSER:
sudo apt-get install lynx
export http_proxy="http://localhost:8080/"
lynx http://www.gizmag.com/
