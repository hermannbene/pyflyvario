Experimental bluetooth variometer for paragliding using the XCTRack App or FlyMe. 
Communication based on LK8EX1 flight instrument protocol.

Hardware recommendation. 
- Raspberry Pi Zero W
- Bosch BMP280 barometer, newer sensor models to be tested. 


How to prepare Raspberry Pi for pairing with your phone. 
Get bluetooth serial of phone. XX:XX:XX:XX:XX:XX phoneaddr

bluetoothctl 
discoverable on
pair 
trust phoneaddr

sudo rfcomm watch hci0 


Autostart com port on Raspberry Pi.
sudo rfcomm watch hci0 & add to: /etc/rc.local

Add main.py to autostart. 
