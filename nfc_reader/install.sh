#!/bin/sh
name='nfc_reader'
sudo cp ${name}.service /etc/systemd/system/
sudo chown root:root /etc/systemd/system/${name}.service
sudo chmod 644 /etc/systemd/system/${name}.service

sudo mkdir /opt/${name}
sudo cp -r ./bin /opt/${name}/
sudo chown root:root /opt/${name}/bin/autoexec.sh
sudo chmod 755 /opt/${name}/bin/autoexec.sh

sudo systemctl daemon-reload
sudo systemctl enable ${name}.service
sudo systemctl status ${name}.service
