Dataset **Wind Turbines (by Kyle Graupe)** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/z/d/JE/LIupfHG8kz86rcGUM2y2Xl2CMCt50ZLhdwPdSyNVIRO3orzYCiWJBF8bq8O2JmKdIWVTaOLsuVvXvgfdfak8sBFzRWcn99RoQXfkjJ5NpR6xIemc3yEfZJOPP4DN.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines (by Kyle Graupe)', dst_path='~/dtools/datasets/Wind Turbines (by Kyle Graupe).tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/kylegraupe/wind-turbine-image-dataset-for-computer-vision/download?datasetVersionNumber=12)