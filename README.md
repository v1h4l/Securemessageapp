

  / \ / \ / \ / \ / \ / \   / \ / \ / \ / \ / \ / \ / \
 ( S | e | c | u | r | e ) ( M | e | s | s | a | g | e )
  \_/ \_/ \_/ \_/ \_/ \_/   \_/ \_/ \_/ \_/ \ / \ / \ /

# A simple message app with Qt5 framework
With encryption to make communication secure
###########################################

secure message app is a simple chat room script in python. This App uses AES encryption for secured data transfer over public network. 
It consist of two scripts a server and a client. Run the server.py in a system so that the client msgapp.py can connect from remote systems 
with the correct password. 
You can edit and change password, host, port and view mode.
If One wants to redistribute or learn from the program, I have included 2 python scripts (Message_client.py, Message_Server.py) that 
shows simple server and client to connect and run the program with ease.

# Installation
  first things first
   # Installing dependencies and requirements

     # Unix
      $  sudo apt-get install python3.x
       >  where x in the version of python, I recoment the latest https://www.python.org/downloads/
       # installing pip
        > see https://pip.pypa.io/en/stable/installing/ Depending on your python version
       # How to install PyQt5 on Linux?
         $ python --version
        # On Ubuntu Linux / Debian Linux you can use the command:
         $ sudo apt-get install python3-pyqt5
        # For CentOS 7 use the command:
         $ yum install qt5-qtbase-devel 
        # For RPM-based systems (Redhat-based)
         $ yum install PyQt5
    # after installation  for your own learning time i recommend https://pythonbasics.org/pyqt/

    # Windows
    > Go to windows command prompt
    > installing python if not already installed.
      Visit https://www.python.org/downloads/windows/ and download your choice of python version i recommend 3.8.1
       follow windows python installation process here https://www.howtogeek.com/197947/how-to-install-python-on-windows/
     # PyQt5 installation
     $ pip install PyQt5 >> for python2.x
     $ pip3 install PyQt5 >> for python 3.x
     # for more information about PyQt5
     >  see https://riverbankcomputing.com/static/Docs/PyQt5/installation.html

     
# after you have finished setting up your environment. You are good to go.

################################################
# Server.py usage

$ python3.x server.py


##################################################
# msgapp.py usage

$ python.3.x msgapp.py
#Screenshots
https://github.com/v1h4l/Securemessageapp/blob/master/Screenshots/test-1.jpg

#Unit test result
1. Done testing found in server.py
   port setting could not connect with clientdue to misconfigured ip addr>
   Screenshot here
1. failed test due to connection timeout
  Screenshot




Enjoy and feel free to report any Bug or updates, Thank you.




