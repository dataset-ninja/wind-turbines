Dataset **Wind Turbines (by Kyle Graupe)** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/v/j/PJ/BE7vZvfICYdY4KGQucMCsLW7Laeday85LjqzQxsFaguzQgpbYF6l0Nd9HE0Ef4CjanS7pzNs4uW0rW6aAIE3Vo64mMTtgwpzvJGqEuYj1LSCucI7Dr5MoMGY22RQ.tar)

As an alternative, it can be downloaded with *dataset-tools* package:
``` bash
pip install --upgrade dataset-tools
```

... using following python code:
``` python
import dataset_tools as dtools

dtools.download(dataset='Wind Turbines (by Kyle Graupe)', dst_dir='~/dataset-ninja/')
```
Make sure not to overlook the [python code example](https://developer.supervisely.com/getting-started/python-sdk-tutorials/iterate-over-a-local-project) available on the Supervisely Developer Portal. It will give you a clear idea of how to effortlessly work with the downloaded dataset.

The data in original format can be [downloaded here](https://www.kaggle.com/datasets/kylegraupe/wind-turbine-image-dataset-for-computer-vision/download?datasetVersionNumber=12).