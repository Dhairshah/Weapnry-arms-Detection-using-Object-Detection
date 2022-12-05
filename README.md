# Training Steps
* Create 2 folders named "train" and "val".
* Create 2 more folders inside train and val named "images" and "labels".
* Copy paste all the images and their labels which you want to train, inside the images and labels folder of train folder.
* Copy paste all the images and their labels which you want to validate, inside the images and labels folder of val folder.
* Copy paste this train and val folder inside data folder.
* Inside data folder create a new .yaml file or make a copy of the existing coco.yaml file.
* Inside this .yaml file give the path of train and val folders, number of classes and the name of classes.
* Now go to cfg and then training folder. Create a new .yaml file or make a copy of the existing yolov7.yaml file.
* Change the nc: parameter inside this .yaml file to the number of classes you are going to provide for training.
* Now execute the train.py file with following command
```
python train.py --workers 1 --device 0 --batch-size 4 --epochs 100 --img-size 640 640 --data data/custom_data.yaml --hyp data/hyp.scratch.custom.yaml --cfg cfg/training/yolov7-custom.yaml --name yolov7-custom --weights yolov7.pt
```
(Note: Change the batch size if large number gives error)