import argparse
import cv2
import numpy as np
from tqdm import tqdm
import os
import moviepy.editor as mp


class PointFlow:
    def __init__(
        self,
        input_path: str,
        output_path: str,
        bcolor: tuple,
        pcolor: tuple,
        pointsize: int,
    ):
        self.cap = cv2.VideoCapture(input_path)
        self.width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        self.height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        self.totalframecount = int(self.cap.get(cv2.CAP_PROP_FRAME_COUNT))
        self.bcolor = bcolor
        self.pcolor = pcolor
        self.radius = pointsize
        self.input_path = input_path
        self.output_path = output_path
        self.mid_path = f"{os.path.splitext(self.output_path)[0]}_noaudio.mp4"
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        self.video = cv2.VideoWriter(
            self.mid_path, fourcc, fps, (self.width, self.height)
        )

    def _set_audio(self, srcfile, imgfile, outfile):
        clip_input = mp.VideoFileClip(srcfile)
        clip_input.audio.write_audiofile("audio.mp3")
        clip = mp.VideoFileClip(imgfile).subclip()
        clip.write_videofile(outfile, audio="audio.mp3")
        os.remove(self.mid_path)
        os.remove("audio.mp3")

    # 各kpを描画する関数
    def _draw(self, img: np.ndarray, kps) -> np.ndarray:
        for kp in kps:
            pt = (int(kp.pt[0]), int(kp.pt[1]))
            cv2.circle(img, pt, self.radius, self.pcolor, thickness=-1)
        return img

    # AKAZE特徴点を抽出する関数
    def _akaze(self, frame: np.ndarray) -> np.ndarray:
        akaze = cv2.AKAZE_create(threshold=0.0001)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        kps, _ = akaze.detectAndCompute(gray, None)

        img = np.full((self.height, self.width, 3), self.bcolor, dtype=np.uint8)
        img_akaze = self._draw(img, kps)
        return img_akaze

    def __call__(self):
        for _ in tqdm(range(self.totalframecount)):
            is_image, frame = self.cap.read()
            if is_image:
                img = self._akaze(frame)
                self.video.write(img)
        self.cap.release()
        self.video.release()
        self._set_audio(self.input_path, self.mid_path, self.output_path)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator of feature points movie.")
    parser.add_argument("--input", type=str, required=True, help="Input file path")
    parser.add_argument("--output", type=str, required=True, help="Output file path")
    parser.add_argument(
        "--bcolor", type=tuple, default=(0, 0, 0), help="Background color"
    )
    parser.add_argument(
        "--pcolor", type=tuple, default=(255, 255, 255), help="Points color"
    )
    parser.add_argument("--pointsize", type=int, default=5, help="point radius")
    args = parser.parse_args()

    pointflow = PointFlow(
        args.input, args.output, args.bcolor, args.pcolor, args.pointsize
    )
    pointflow()
