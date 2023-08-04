import time
import cv2
import queue
import threading

class Cam(threading.Thread):
    def __init__(self,camId,fps):
        threading.Thread.__init__(self)
        self.camId = camId
        self.fps = fps
        self.camera = cv2.VideoCapture(self.camId, cv2.CAP_DSHOW)
        self.running = True
        self.warehouse = queue.Queue()

        self.slowness = 1/fps

    def stop(self):
        self.running: False
        self.camera.release()


    def run(self):
        while self.running:
            ret, frame = self.camera.read()
            if ret:
                self.warehouse.put(frame)

            if cv2.waitKey(1) & 0XFF == ord("q"):
                self.stop()

            time.sleep(self.slowness)





