#!/bin/bash
apt install mu-editor vim vlc gimp inkscape codium snapd
dpkg -i filius.deb
dpkg -i logisim-evolution.deb
apt -f install
snap install freeplane-mindmapping
snap install drawio
