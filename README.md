# RIT-iRODS-clients
Client-applications and libraries for iRODS.

## Contents
* `iping` --- iRODS client app for usage in Nagios monitoring.
* `...`
 
## Usage (compiling)
Follow instructions below to get a working `iping` binary.

**Dependencies:** This requires *irods-dev* and *irods-runtime* packages installed on your system. 

```
cd ~
git clone https://github.com/MaastrichtUniversity/rit-irodsclients.git

cd ~/rit-irodsclients/iping/src
make install

cd ~/rit-irodsclients/iping/build

# execute as user 'irods'
./iping                              
./iping -h icat.example.org -p 1247 
```

## Usage (packaging)
Follow instructions below to package the `iping` binary in a .deb-package

```
cd ~/rit-irodsclients 
sudo cp iping/build/iping packaging/rit-irods-clients_1.0.0/usr/bin
sudo dpkg-deb --build packaging/rit-irods-clients_1.0.0
```

To install the package:
```
sudo dpkg -i packaging/rit-irods-clients_1.0.0.deb
```

Confirm installation:
```
which iping     # should return '/usr/bin/iping'
```