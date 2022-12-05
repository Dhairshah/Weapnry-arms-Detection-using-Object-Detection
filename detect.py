import argparse
import time
from pathlib import Path

import cv2
import torch
import torch.backends.cudnn as cudnn
from numpy import random

from PyQt5 import QtCore
from PyQt5.QtGui import QImage
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from models.experimental import attempt_load
from utils.datasets import LoadStreams, LoadImages
from utils.general import check_img_size, check_requirements, check_imshow, non_max_suppression, apply_classifier, \
    scale_coords, xyxy2xywh, strip_optimizer, set_logging, increment_path
from utils.plots import plot_one_box
from utils.torch_utils import select_device, load_classifier, time_synchronized, TracedModel

from threading import Thread
from sms import send_sms

class ThreadClass(QtCore.QThread):

    info_signal = QtCore.pyqtSignal(str)
    pic_signal = QtCore.pyqtSignal(QImage)
    alarm_signal = QtCore.pyqtSignal(int)

    def __init__(self, parent, source, weights, base_class):
        super(ThreadClass, self).__init__(parent)
        self.weights = weights
        self.source = source
        self.base_class = base_class

    def run(self):
        with torch.no_grad():
            self.detect()

    def stop(self):
        # Releasing the LoadStreams
        self.dataset.destroy()

        # Terminating the Thread
        self.terminate()

    def detect(self):
        imgsz = 640
        device = torch.device('cuda:0')
        half = device.type != 'cpu'  # half precision only supported on CUDA

        # Load model
        model = attempt_load(self.weights, device, self.info_signal)  # load FP32 model
        stride = int(model.stride.max())  # model stride
        imgsz = check_img_size(imgsz, s=stride)  # check img_size

        # Printing model architecture
        print('Model Architecture :- \n', model)

        if half:
            model.half()  # to FP16

        cudnn.benchmark = True  # set True to speed up constant image size inference
        self.dataset = LoadStreams(self.source, img_size=imgsz, stride=stride)

        # Get names and colors
        names = model.module.names if hasattr(model, 'module') else model.names
        colors = [[random.randint(0, 255) for _ in range(3)] for _ in names]

        # SMS (2 second) timer
        self.start_time = -1

        # Alarm
        self.sms_send = True

        for path, img, im0s, vid_cap in self.dataset:
            img = torch.from_numpy(img).to(device)
            img = img.half() if half else img.float()  # uint8 to fp16/32
            img /= 255.0  # 0 - 255 to 0.0 - 1.0
            if img.ndimension() == 3:
                img = img.unsqueeze(0)

            if self.base_class.get_start_stop_signal() == 1:

                # Inference
                t1 = time_synchronized()
                with torch.no_grad():   # Calculating gradients would cause a GPU memory leak
                    pred = model(img, augment=False)[0]
                t2 = time_synchronized()

                # Apply NMS
                pred = non_max_suppression(pred)
                t3 = time_synchronized()

                # Process detections
                for i, det in enumerate(pred):  # detections per image
                    p, s, im0, frame = path[i], '%g: ' % i, im0s[i].copy(), self.dataset.count
                    gn = torch.tensor(im0.shape)[[1, 0, 1, 0]]  # normalization gain whwh
                    class_names = []
                    
                    if len(det):
                        # Rescale boxes from img_size to im0 size
                        det[:, :4] = scale_coords(img.shape[2:], det[:, :4], im0.shape).round()

                        # Print results
                        for c in det[:, -1].unique():
                            n = (det[:, -1] == c).sum()  # detections per class
                            s += f"{n} {names[int(c)]}{'s' * (n > 1)}, "  # add to string
                            class_names.append(names[int(c)])

                        # Write results
                        for *xyxy, conf, cls in reversed(det):
                            label = f'{names[int(cls)]} {conf:.2f}'
                            plot_one_box(xyxy, im0, label=label, color=colors[int(cls)], line_thickness=1)

                    # Alarm
                    if len(class_names) == 0:
                        self.alarm_signal.emit(0)
                        self.sms_send = True
                        self.start_time = -1
                    else:
                        # Red alarm only for Gun and Knife class
                        for class_name in class_names:
                            if class_name == 'Gun' or class_name == 'Knife':
                                # Alarm
                                self.alarm_signal.emit(1)

                                # SMS (2 second)
                                if self.start_time == -1:
                                    self.start_time = time.time()
                                self.stop_time = time.time()
                                
                                if int(self.stop_time - self.start_time) == 2:
                                    if self.sms_send == True:
                                        self.sms_send = False
                                        print('Sending SMS!')
                                        sms_thread = Thread(target = send_sms)
                                        sms_thread.start()                                    

                    print(class_names)
                    #print(f'{s}Done. ({(1E3 * (t2 - t1)):.1f}ms) Inference, ({(1E3 * (t3 - t2)):.1f}ms) NMS')

                # Convert and Display
                Image = cv2.cvtColor(im0, cv2.COLOR_BGR2RGB)
                FlippedImage = Image

                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(self.base_class.get_screen_width(), self.base_class.get_screen_height(), Qt.KeepAspectRatio)

                self.pic_signal.emit(Pic)
            else:
                self.alarm_signal.emit(0)
                im1 = im0s[0].copy()

                # Convert and Display
                Image = cv2.cvtColor(im1, cv2.COLOR_BGR2RGB)
                FlippedImage = Image
                
                ConvertToQtFormat = QImage(FlippedImage.data, FlippedImage.shape[1], FlippedImage.shape[0],QImage.Format_RGB888)
                Pic = ConvertToQtFormat.scaled(self.base_class.get_screen_width(), self.base_class.get_screen_height(), Qt.KeepAspectRatio)
                
                self.pic_signal.emit(Pic)
