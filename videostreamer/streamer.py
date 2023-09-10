from flask import Flask, render_template, Response

class VideoStreamer:
    def __init__(self, video_file_path):
        self.app = Flask(__name__)
        self.video_file_path = video_file_path

        @self.app.route('/')
        def index():
            """Video streaming home page."""
            return render_template('index.html')

        @self.app.route('/video_feed')
        def video_feed():
            """Video streaming route. Put this in the src attribute of an img tag."""
            return Response(self.gen(), mimetype='multipart/x-mixed-replace; boundary=frame')

    def gen(self):
        """Video streaming generator function."""
        with open(self.video_file_path, 'rb') as video:
            data = video.read(1024)
            while data:
                yield (b'--frame\r\n'
                       b'Content-Type: video/mp4\r\n\r\n' + data + b'\r\n')
                data = video.read(1024)

    def run(self):
        self.app.run(host='0.0.0.0', threaded=True)

# Additional code to allow Flask to use external templates and static folders
import os
import sys

template_dir = os.path.abspath('templates')
static_dir = os.path.abspath('static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

sys.modules['flask'].Flask = app


# from videostreamer import VideoStreamer

# streamer = VideoStreamer("path_to_your_video.mp4")
# streamer.run()
