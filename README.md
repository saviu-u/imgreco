# ImgReco #

This project is made for UNIP Computer Science, 6th semester

---
This project uses an endpoint to receive a base64 image with some parameters and returns a base64 image with the respective recognitions

# Installation

Even with docker, you **HAVE TO USE** [Git Large File Storage](https://git-lfs.github.com/), the model this project uses is a quite heavy yolo5 model, so it's a requirement, you could also replace the file for a yolo.h5 file of your own (do that to your own risk)

We highly encourage using docker, just "compose" it up and you are good to go

# Endpoints

Path                  | Method | Return | Description |
----------------------|--------|--------|-------------|
/types                | GET    | json   | All types of recognitions available
/retrieve             | POST   | json   | Returns recognized image
/                     | GET    | doc    | Opens a stream with a webcam (main page)

The _/retrive_ receive two parameters


* "frame" which requires a base64 string
* "allowed_objects" which is a list of possible recognition objects 

---

## Students ##
* Gabriel Casaroto
* Sávio Cangussu
* Francisco Roque
* Guilherme Henrique F Rosa
* Raphael Basse
