from pathlib import Path
from typing import Union

from pygltflib import GLTF2, BufferFormat

Pathlike = Union[Path, str]


def read_glb(file: Pathlike):
    obj = GLTF2().load(file)
    obj.convert_buffers(BufferFormat.BINARYBLOB)
    return obj
