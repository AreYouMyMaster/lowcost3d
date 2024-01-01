from utils.io import read_glb_meshes
import torch


class TestReadGlb:

    def test_read_glb(self):
        OBJAVERSE_SAMPLE = "/rawdata3/objaverse/hf-objaverse-v1/glbs/000-000/0000ecca9a234cae994be239f6fec552.glb"
        vertices = read_glb_meshes(OBJAVERSE_SAMPLE)
        for name, vertex in sorted(vertices.items()):
            print(name, vertex.shape)
        print(len(vertices))
