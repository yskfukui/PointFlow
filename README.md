# PointFlow

**Generator of a point cloud movie.**
## Install
- numpy
- scipy
- pillow (for example code to load/save image)

## Comand line example
```
python .\point_generator.py --input ./movie/input.mp4 --output ./movie/output.mp4
```

## Parameter
- ```--input``` ：Path of input video
- ```--output```：Path of output video
- ```--bcolor```：Background color
- ```--pcolor```：Points color
- ```--pointsize```：Point size