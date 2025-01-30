Dataset **Wind Turbines (by Kyle Graupe)** can be downloaded in [Supervisely format](https://developer.supervisely.com/api-references/supervisely-annotation-json-format):

 [Download](https://assets.supervisely.com/remote/eyJsaW5rIjogImZzOi8vYXNzZXRzLzEwNDRfV2luZCBUdXJiaW5lcyAoYnkgS3lsZSBHcmF1cGUpL3dpbmQtdHVyYmluZXMtKGJ5LWt5bGUtZ3JhdXBlKS1EYXRhc2V0TmluamEudGFyIiwgInNpZyI6ICI0VzI3U3FrRUJYbjZ6bm5nSGJpYVhWRFJCU2V1azNocXJxeTgwempEa3VZPSJ9)

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