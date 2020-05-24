[Unit]
Description=Standby
 
[Service]
Type=simple
WorkingDirectory=/home/volumio
ExecStart=/usr/local/bin/python3 -u /home/volumio/NR1-UI/Standby.py
StandardOutput=syslog
StandardError=syslog
SyslogIdentifier=Standby-Service
User=volumio
Group=volumio
 
[Install]
WantedBy=multi-user.target