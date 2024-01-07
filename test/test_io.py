from utils.io import read_glb_meshes
import open3d as o3d


class TestReadGlb:

    def test_read_glb(self):
        OBJAVERSE_SAMPLE = "/rawdata3/objaverse/hf-objaverse-v1/glbs/000-000/0000ecca9a234cae994be239f6fec552.glb"
        vertices = read_glb_meshes(OBJAVERSE_SAMPLE)
        for name, vertex in sorted(vertices.items()):
            print(name, vertex.shape)

        # visualization
        name, val = vertices.popitem()
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(val.T)
        o3d.io.write_point_cloud("./test/test.ply", pcd)
