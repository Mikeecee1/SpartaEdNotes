## Steps to connecting mongoDB server to EC2 Instance ##

*Note to self use paste not Ctrl V in terminal!*

**Create instance & connect**

1. Create instance of EC2 on aws using key value pair
2. Use Ubuntu 24.04 (Depending on usage)
3. Create security group (or reuse if already set up) making sure SSH is set to myIP only 
4. Launch instance
5. Connect to bash terminal (cd into .ssh folder for key)
6. Copy connection command from 

**Set up Mongodb on instance**

1. Run commands to check if mongoDB is running
    `mongod --version`
    `mongosh`
    This will check if the mongodb server & shell are installed
2. If not running run these commands to install require tools
    - Installs required tools  
    `sudo apt update && sudo apt install -y gnupg curl`
    - Adds mongo db repository  
    `curl -fsSL https://pgp.mongodb.com/server-8.0.asc | sudo gpg -o /usr/share/keyrings/mongodb-server-8.0.gpg --dearmor`
    - Move generated key to correct location  
    `sudo mv server-8.0.asc.gpg /usr/share/keyrings/mongodb-server-8.0.gpg`
    - Tells Ubuntu where to download MongoDB packages from (command should echo back in terminal)  
    `echo "deb [ arch=amd64,arm64 signed-by=/usr/share/keyrings/mongodb-server-8.0.gpg ] https://repo.mongodb.org/apt/ubuntu noble/mongodb-org/8.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-8.0.list`  

3. Install MongoDB
    Run this Command  
    `sudo apt update`  
    Then  
    `sudo apt install -y mongodb-org`  

**Start MongoDB**
   
   - To start MongoDB run  
    `sudo systemctl start mongod`  
   - Check status  
    `sudo systemctl status mongod`  
   - terminal message should include (or similar)  
    `Active: active (running)`  

**Restart Instance**

 After stopping an instance:  
    - Restart instance from aws
    - SSH into it  
    `ssh -i your-key.pem ubuntu@<EC2_PUBLIC_IP>`  
    - Check mongoDb is working  
    `sudo systemctl status mongod`  
    - If not running  
    `sudo systemctl start mongod`  
    - To work directly with server(optional)   
    `mongosh`  
    - Before connecting to Compass this command ensures MongoDB starts when instance is restarted  
    `sudo systemctl enable mongod`  

**Useful Commands**  

use <dbsname>  
show dbs  




    -

    `
