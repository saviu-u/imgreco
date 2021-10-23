# ImgReco #

This project is made for the 6th semester of Computer Cience from UNIP

---
This project uses a endpoint to receive a base64 image with some parameters and returns a base64 image with the respective recognitions

# Installation

Even with docker, you **HAVE TO USE** [Git Large File Storage](https://git-lfs.github.com/), the model this project uses is a quite heavy yolo5 model, so it's a requirement, you could also replace the file for a yolo.h5 file of your own (do that to your own risk)

We highly encourage using docker, just "compose" it up and you are good to go

# Endpoints

Path                  | Method | Return | Description |
----------------------|--------|--------|-------------|
/types                | GET    | json   | All types of recognitions available
/retrieve             | POST   | json   | Returns recognized image
/stream (Debug Pages) | GET    | doc    | Opens a stream with a webcam (Don't use in production)
/view   (Debug Pages) | GET    | doc    | Receives a webcam (Don't use in production)

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