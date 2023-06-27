Dataset **Wind Turbines** can be downloaded in Supervisely format:

 [Download](https://assets.supervisely.com/supervisely-supervisely-assets-public/teams_storage/b/q/Ov/6cpD1jxxcFauc594dR7xyLGzWnrwu0IxmyT9Jv90XfruTqLpFem6wlFs8D1w6AuxpnqRGx7fRnsdCdG9pnqDNdZPx63rxIQcGAI6PayVPyQTl0xC2uUGO1kn39YU.tar)

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