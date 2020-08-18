

# first stage testing
# actual message app


#Unix automation script
# for debian
echo -e "Installing python3.8 in debian/ubuntu"

sudo apt-get install python3.8
pause 2


echo "Installing PyQt5"
sudo apt-get install python3-pyqt5
pause 2
echo "done"



echo "running Server first"
xterm sudo python3.8 server.py &

 
echo "running client"
sudo python3.8 msgapp.py


#testing  itc connectivity

#Secondly testing the learning script

echo "running server for the learning script"
# server command

xterm -e sudo python3.8 Message_Server.py
pause 3

# running client

xterm -e sudo python3.8 Message_client.py

echo "Done"

