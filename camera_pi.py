import io
import time
import picamera
from base_camera import BaseCamera

class Camera(BaseCamera):
    @staticmethod
    def frames():
        with picamera.PiCamera() as camera:
            time.sleep(2)
            camera.vflip = True
            stream = io.BytesIO()
            for foo in camera.capture_continuous(stream, 'jpeg', use_video_port=True):

                # return current frame
                stream.seek(0)
                yield stream.read()

                #reset stream for next frame
                stream.seek(0)
                stream.truncate()
