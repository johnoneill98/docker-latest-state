# Docker-Latest-State
This is some python scripts to show some basic information about Docker images

## Website

The website that used in the `docker.py` is the following
https://hub.docker.com/v2/repositories/library/?page=1&page_size=100

## `Docker.py`

`docker.py` is a python script that lets a user to call a command line argument that calls a function from `api.py`

## Formatting

To use the `docker.py` the user has to format the command line arguments as such

```
python3 docker.py <image_name>
```
The reason why it is python3 instead of python is because `docker.py` uses the urllib.request module that is not supported by python.

 ## Commands
 With `docker.py` the user have a variety of commands to implement.

### The Latest Version Command
```
$python3 docker.py <image-name> -l
```
This commands lets the user to see whatever version was the latest for that image
### The Last Updated  command
~~~
python3 docker.py <image-name>
~~~
This commands allows the user top see what eas the last updated version. Most people would think that the latest version is the last updated but that is not the case for some images in DockerHub's registry:

Example
```
$ python3 docker.py postgres -l
The version of postgres that was last updated is 9.6.18
The latest version of postgres is 13
```
### The Search Version Command
```
python3 docker.py <image_name> -v <version_number>
```
This command allows the user to search to see if the version of an image exists with Docker Hub
If the Version doesn't exist, the user will be prompted with all the current versions of the image and after that the latest version of the image
Example:
```
$ python3 docker.py mongo -v 24
The version of mongo that was last updated is 4.2.8
Version 24 is not a valid version of  mongo
Valid versions of mongo are
['3', '3.6', '3.6.17', '3.6.18', '4', '4.0', '4.0.18', '4.0.19', '4.2', '4.2.5', '4.2.6', '4.2.7', '4.2.8']

```

#### The help command
If the user needs help with the commands and doesn't want to return to this page, use this command
```

$ python3 docker.py
usage: docker.py [-h] [-v VERSION] [-l] image

This script takes a image and shows either the the latest version, the last
version that was updated of the image or if the version is a valid version

positional arguments:
  image       please enter a image name like so 'python3 docker.py
              <imagename>'

optional arguments:
  -h, --help  show this help message and exit
  -v VERSION  Please enter a image then its version number like so 'python3
              docker.py <imagename> -v <versionnumber>'
  -l          Please enter '-l' to get the latest version like so 'python3
              docker.py <imagename> -l'
```

