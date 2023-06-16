# https://www.kaggle.com/datasets/kylegraupe/wind-turbine-image-dataset-for-computer-vision

import supervisely as sly


def convert_and_upload_supervisely_project(
    api: sly.Api, workspace_id: int, project_name: str
) -> sly.ProjectInfo:
    # * dataset_path = "Path to the local dir with dataset"

    # Function should read local dataset and upload it to Supervisely project, then return project info.

    raise NotImplementedError('Use "Convert YOLO v5 to Supervisely format" app instead.')
