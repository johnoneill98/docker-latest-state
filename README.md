# Docker-Latest-State
This is some python scripts to show some basic information about Docker images

## Website

The website that used in the `api.py` is the following
https://hub.docker.com/v2/repositories/library/?page=1&page_size=100

## `Argument.py`

`Argument.py` is a python script that lets a user to call a command line argument that calls a function from `api.py`

### Formatting

To use the `argument.py` the user has to format the command line arguments as such

```
python3 argument.py <command>
```
The reason why it is python3 instead of python is because `api.py` uses the urllib.request module that is not supported by python.
So, if a user tries to that they will get this error message

```
python argument.py -h
Traceback (most recent call last):
  File "argument.py", line 5, in <module>
    import api
  File "/home/john/docker-latest/docker-latest-state/api.py", line 3, in <module>
    import urllib.request
ImportError: No module named request
```
 ### Commands
 With `argument.py` the user have a variety of commands  to implement.

#### The Search Command
```
python3 argument.py -i <image-name>
```
This commands lets the user to get the information specific information about the image they have entered.

It will return the latest version of the image

#### The help command
If the user needs help with teh commands and doesn't want to return to this page, use this command
```
python3 argument.py -h
Correct formatting is 'python3 argument.py -i <imageName>' for looking up an image
```
#### Error Checking
 If a user puts an incorrect command teh will receive this message
```
python3 argument.py -help
If you need help, type 'python3 argument.py -h'
```


