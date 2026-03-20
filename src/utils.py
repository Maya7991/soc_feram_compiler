import torchvision.models as models

MODEL_MAP = {
            "resnet18": models.resnet18,
            # "resnet20": models.resnet20,
        }

NUM_BLOCKS = 112