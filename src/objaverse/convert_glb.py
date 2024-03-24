import numpy as np
import mitsuba as mi

from utils.pointflow_fig_colorful import visualize_pcl_as_xml

mi.set_variant("cuda_ad_rgb")

POINTFLOW_SAMPLE = "/rawdata3/ShapeNetCore.v2.PC15k/02747177/train/10839d0dc35c94fcf4fb4dee5181bee.npy"
OBJAVERSE_SAMPLE = "/rawdata3/objaverse/hf-objaverse-v1/glbs/000-000/0000ecca9a234cae994be239f6fec552.glb"

if __name__ == "__main__":
    sample = np.load(POINTFLOW_SAMPLE)
    visualize_pcl_as_xml(sample, "pointflow_sample.xml")
