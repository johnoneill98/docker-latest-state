# Docker-Latest-State
This is some python scripts to show some basic information about Docker images

## Website

The website that used in the `api.py` is the following
https://hub.docker.com/v2/repositories/library/?page=1&page_size=100

## `Docker.py`

`docker.py` is a python script that lets a user to call a command line argument that calls a function from `api.py`

### Formatting

To use the `docker.py` the user has to format the command line arguments as such

```
python3 docker.py <command>
```
The reason why it is python3 instead of python is because `docker.py` uses the urllib.request module that is not supported by python.

 ### Commands
 With `docker.py` the user have a variety of commands to implement.

#### The Latest Version Command
```
$python3 docker.py -l <image-name>
```
This commands lets the user to get the information specific to the image they have entered.

It will return the whatever version was latest for that image
### The Last Updated  command
~~~
python3 docker.py -i <image-name>
~~~
This commands allows the user top see what eas the last updated version. Most people would think that the latest version is the last updated but that is not the case for some images in DockerHub's registry:

Example
```
$python3 docker.py -l postgres
The latest version of postgres is 13
$python3 docker.py -i postgres
Last updated version of postgres is 9.6.18
```
### The Search Version Command
```
python3 docker.py -l <image-name> -v <version-number>
```
This command allows the user to search to see if the version of an image exists with Docker Hub
If the Version doesn't exist, the user will be prompted with all the current versions of the image and after that the latest version of the image
Example:
```
$ python3 docker.py -l mongo -v 24
Version: ['24'] is not a valid version of  mongo
Valid versions of mongo are
['4.0.17', '4.2.5', '3.6.17', '4.2.6', '4.0.18', '4.2.7', '3', '3.6', '3.6.18', '4', '4.0', '4.0.19', '4.2', '4.2.8']
The latest version of mongo is 4.2.8
```
In order to find the versions the user must put `-l <image-name>` before teh version number

#### The help command
If the user needs help with teh commands and doesn't want to return to this page, use this command
```
$ python3 docker.py -h
usage: docker.py [-h] [--lastupdated, IMAGE] [--version VERSION]
                 [--latestversion LATEST]

This script takes a image and either shows the latest version of the image or
if the version is a valid version

optional arguments:
  -h, --help            show this help message and exit
  --lastupdated, IMAGE, -i IMAGE
                        Please enter an image to get the last updated version
  --version VERSION, -v VERSION
                        Please enter a image then its version number
  --latestversion LATEST, -l LATEST
                        Please enter an image to get the lastest version`

```


