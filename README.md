# PointFlow

**Generator of a point cloud movie.**
## Install
```
git clone https://github.com/yskfukui/PointFlow.git
cd PointFlow
pip install -r requirements.txt
```


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