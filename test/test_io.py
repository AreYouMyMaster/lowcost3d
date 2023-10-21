from utils.io import read_glb


class TestReadGlb:

    def test_read_glb(self):
        POINTFLOW_SAMPLE = "/rawdata3/ShapeNetCore.v2.PC15k/02747177/train/10839d0dc35c94fcf4fb4dee5181bee.npy"
        OBJAVERSE_SAMPLE = "/rawdata3/objaverse/hf-objaverse-v1/glbs/000-000/0000ecca9a234cae994be239f6fec552.glb"

        readed = read_glb(OBJAVERSE_SAMPLE)
        print(readed)
