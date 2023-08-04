import queue
import threading
import cv2

class CameraViewer(threading.Thread):
    def __init__(self, warehouse, window_name):
        threading.Thread.__init__(self)
        self.window_name = window_name
        self.running = True

        self.warehouse = warehouse

    def run(self):
        while self.running:
            try:
                frame = self.warehouse.get_nowait()

                if frame is not None:
                    cv2.imshow(self.window_name, frame)
            except queue.Empty:
                pass

            if cv2.waitKey(1) & 0xFF == ord('q'):
                self.stop()

    def stop(self):
        self.running = False
        cv2.destroyAllWindows()
