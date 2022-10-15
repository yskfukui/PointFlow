import argparse
import cv2
import numpy


class PointFlow:
    def __init__(
        self,
        input_path: str,
        output_path: str,
        bcolor: tuple = [255, 0, 0],
        pcolor: tuple = [0, 255, 0],
    ):
        self.cap = cv2.VideoCapture(input_path)
        width = int(self.cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fps = int(self.cap.get(cv2.CAP_PROP_FPS))
        fourcc = cv2.VideoWriter_fourcc("m", "p", "4", "v")
        self.video = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    def __call__(self):
        cnt = 0
        while True:
            is_image, frame = self.cap.read()
            if is_image:
                print(cnt)
            else:
                break
            cnt += 1
            if cnt > 10:
                break
        self.cap.release()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generator of feature points movie.")
    parser.add_argument("--input", required=True, help="Input file path")
    parser.add_argument("--output", required=True, help="Output file path")
    parser.add_argument("--bcolor", help="Background color")
    parser.add_argument("--pcolor", help="Points color")
    args = parser.parse_args()

    a = PointFlow(args.input, args.output, args.bcolor, args.pcolor)
    a()
