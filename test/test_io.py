import numpy as np
import open3d as o3d

from utils.io import read_glb_meshes

OBJAVERSE_SAMPLE = "/rawdata3/objaverse/hf-objaverse-v1/glbs/000-000/0000ecca9a234cae994be239f6fec552.glb"


class TestReadGlb:

    def test_read_glb(self):
        vertices = read_glb_meshes(OBJAVERSE_SAMPLE)
        pts = []
        for name, vertex in sorted(vertices.items()):
            pts.append(vertex)
        pts = np.hstack(pts)

        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(pts.T)
        print(pcd.points)
        # assert pcd.points.shape == (7013, 3)
