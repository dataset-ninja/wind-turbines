Dataset **Wind Turbines** can be downloaded in Supervisely format:

 [Download](https://assets.supervise.ly/supervisely-supervisely-assets-public/teams_storage/n/6/9M/FJr2CNweBULi8GHXvyBYm9WwbgsORX6ojh716IzWj5afNduuWv7SjluY8A6pBRrSdSqnRmfjQDdnHkUmnTfrjTKd2Bs7zGg0KPLbaP4tW9Dr0zPwCbsLTnhgl5p6.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines', dst_path='~/dtools/datasets/Wind Turbines.tar')
```
The data in original format can be 🔗[downloaded here](https://www.kaggle.com/datasets/kylegraupe/wind-turbine-image-dataset-for-computer-vision/download?datasetVersionNumber=12)