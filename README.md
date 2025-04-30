# Building detection using Satellite imagery in South India
This project detects buildings on Sentinel 2 satelite images and was trained using YOLOv8 and Roboflow. The models were evluated on satellite data covering parts of Tamil Nadu.
The models correspond to the labeling methods: The first used manual labeling, the second and third ones automated labeling.
### Google
 https://docs.google.com/document/d/1rwxETUBSJR45rE4G4-ERb-VCAmlVL5FeIzWFk-3Yh3U/edit?usp=sharing
### Overleaf 
 [https://www.overleaf.com/6567118731jkrgfyjkprfj#cb308f](https://www.overleaf.com/2887651616xwmcxyxshpwk#ae2f4a)
## Data Aquisition
To obtain the sentinel-2 data, [this](data/tile_download_script.py) Google Earth Engine script was created. In order to use it, one has to register to Google Cloud, create a project and use tile_download_script.py on the [Google Earth Engine Editor](https://code.earthengine.google.com. )
The data is made up of .tif files of the specified region.
## Data Preperation
Now the .tif files need to be split into smaller tiles in order to reduce the amount of labels on one tile and increase readability. The next step converts the .tif files into .jpg. The third does the automatic labeling. The first version creates bounding boxes around every single instance (fine), the second version merges nearby instances (condensed). The last steps upload the labeled data to Roboflow. The data preparation can be done on this [Google Colab](data/TileConvertingAndLabeling.ipynb)
and requieres a connected Google account. For manual labeling we used [Make Sense AI](https://www.makesense.ai/).
## Model Training
Once the data has been prepared, the training can begin. We used the [YOLOv8 Object Detection Google Colab](https://colab.research.google.com/github/roboflow-ai/notebooks/blob/main/notebooks/train-yolov8-object-detection-on-custom-dataset.ipynb) from Ultralytics linked to our Roboflow account. We modified the Colab in order to incorporate our Google Drive and removed unused features. This version can be found [here](training/modified_yolov8_object_detection.ipynb). 
