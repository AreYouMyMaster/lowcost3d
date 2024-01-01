"""
Please refer to https://github.com/KhronosGroup/glTF-Tutorials/blob/master/gltfTutorial/README.md
"""
import struct
from pathlib import Path
from typing import Union

import numpy as np
from pygltflib import GLTF2, BufferFormat, Node

Pathlike = Union[Path, str]
Gltf = GLTF2


def retrieve_vertices_from_buffer(obj: Gltf, mesh_id: int) -> np.ndarray:
    mesh = obj.meshes[mesh_id]
    vertices = []
    for primitive in mesh.primitives:
        # get the binary data for this mesh primitive from the buffer
        accessor = obj.accessors[primitive.attributes.POSITION]
        buffer_view = obj.bufferViews[accessor.bufferView]
        buffer = obj.buffers[buffer_view.buffer]
        data = obj.get_data_from_buffer_uri(buffer.uri)

        for i in range(accessor.count):
            index = buffer_view.byteOffset + accessor.byteOffset + i * 12  # the location in the buffer of this vertex
            d = data[index:index + 12]  # the vertex data
            v = struct.unpack("<fff", d)  # convert from base64 to three floats
            vertices.append(v)

    vertices = np.array(vertices).T
    assert vertices.ndim == 2 and vertices.shape[0] == 3
    return vertices


def get_point_clouds(obj: Gltf, node_id: int, transform: np.ndarray = np.ones((4, 4), dtype=float)):
    """Recursively apply translation to the leaf-most nodes"""
    collections = {}
    node = obj.nodes[node_id]
    transform = np.matmul(transform, np.array(node.matrix).reshape((4, 4))) if node.matrix else transform
    if node.mesh is not None:
        vertices = retrieve_vertices_from_buffer(obj, node.mesh)
        collections[node.name] = np.matmul(transform[:3, :3], vertices) + transform[3, :3, None]
    if node.children:
        for child in node.children:
            collections.update(get_point_clouds(obj, node_id=child, transform=transform))
    return collections


def read_glb_meshes(file: Pathlike):
    obj = GLTF2().load(file)
    obj.convert_buffers(BufferFormat.BINARYBLOB)
    assert_msg = "accept only single object for the scope of this project"
    assert len(obj.scenes) == 1 and len(obj.scenes[0].nodes) == 1, assert_msg
    root_node_id = obj.scenes[0].nodes[0]
    point_cloud = get_point_clouds(obj, root_node_id)
    return point_cloud
