Get bluetooth serial of phone. XX:XX:XX:XX:XX:XX phoneaddr

How to prepare Raspberry Pi for pairing with your phone. 

bluetoothctl 
discoverable on
pair 
trust phoneaddr

sudo rfcomm watch hci0 


Autostart com port on Raspberry Pi.
sudo rfcomm watch hci0 & add to: /etc/rc.local

Add main.py to autostart. 
