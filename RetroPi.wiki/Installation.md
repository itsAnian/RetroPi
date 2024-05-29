## 1. Installation of Raspi OS Legacy 64 bit - !Bullseye!

Download the Raspberry Pi Imager to install and format the SD-card.

For the OS you have to go to Raspberry Pi OS and search for the Legacy 64 bit with the Bullseye version.

Then pick the SD-card you want to format.

Before you hit write, you should adjust the extended options and configure retropie as hostname and as name, pick a password and adjust the Language settings.


## 2. First boot might take a while

After the boot you have to connect to the wifi, you can do it in the commandline `sudo raspi-conifg` or in the gui.

The you should get the newest updates for the installed applications with the command
`sudo apt update; sudo apt upgrade`

If you want to control the Pi remotely you have to enable ssh on the pi, you can again do it in the commandline or in the gui.

## 3. Installation of the Matrix repository

To get the Matrix repository you have to paste this command into the commandline, this gets the installation-scripts, which are executed afterwards.

    curl https://raw.githubusercontent.com/adafruit/Raspberry-Pi-Installer-Scripts/main/rgb-matrix.sh >rgb-matrix.sh
    sudo bash rgb-matrix.sh

Then you are getting questions asked, which you have to answer, according to your device

Do you want to install the the Matrix drivers? - y

Which hardware do you have? - 2

Do you want to install the additional module? - y

Do you want Quality or Sound? - 1

Then you are asked, if your answers were right. - y

After the installation you are asked if you want to reboot right away.

## 4. The blacklist of the soundmodule

Switch off on-board sound (`dtparam=audio=off` in `/boot/config.txt` with `sudo nano /boot/config.txt`). External USB sound adapters work, and are much better quality anyway, so that is recommended if you happen to need sound.

For improved quality you have to add `isolcpus=3` at the end of the line of `/boot/cmdline.txt` with sudo nano `/boot/cmdline.txt` (needs to be in the same as the other arguments, no newline). This will use the last core only to refresh the display then, but it also means, that no other process can utilize it then.

## 5. Installation of the games in this repository

For the Installation of our game repo you have to go into the terminal and enter `git clone https://github.com/INF2023AI-Python/RetroPi.git`, which clones our repo onto the Pi.

## 6. Scoreboard integration

For the scoreboard integration you have to move to the RetroPi folder in the terminal and enter `sudo chmod +666 score.json`. Without this, our games are not abled to work. If there is an update you have to execute this command again, otherwise the programm will crash trying to write into the score file.

## 7. Add our games to autostart

To add RetroPi to the autostart, you just have to `sudo nano /etc/rc.local` and add `sudo bash /home/retropie/RetroPi/autostart.sh &` in front of the `exit 0`

After a reboot the Pi is set up to always run RetroPi on startup.