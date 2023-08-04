import cv2
from cam import Cam
from viewer import CameraViewer


if __name__ == "__main__":
    print("Starting camera data stream and imaging.")

    camera = cv2.VideoCapture(0)

    camera_stream1 = Cam(0, 1)
    camera_stream2 = Cam(0, 10)
    camera_stream3 = Cam(0, 60)

    camera_viewer1 = CameraViewer(camera_stream1.warehouse, "Cam1")
    camera_viewer2 = CameraViewer(camera_stream2.warehouse, "Cam2")
    camera_viewer3 = CameraViewer(camera_stream3.warehouse, "Cam3")

    camera_stream1.start()
    camera_stream2.start()
    camera_stream3.start()

    camera_viewer1.start()
    camera_viewer2.start()
    camera_viewer3.start()

    while True:
        if cv2.waitKey(1) & 0xFF == ord('q'):
            camera_stream1.stop()
            camera_stream2.stop()
            camera_stream3.stop()
            break

    camera_stream1.join()
    camera_stream2.join()
    camera_stream3.join()

    camera.release()

    print("The program has ended.")
