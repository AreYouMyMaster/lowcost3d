import os

import objaverse

if __name__ == "__main__":
    objaverse.BASE_PATH = "/rawdata2/objaverse/"
    objaverse._VERSIONED_PATH = os.path.join(objaverse.BASE_PATH, "hf-objaverse-v1")

    uids = ["001200d8ec8d46efbd5bfd0337f7dc7f"]
    annotations = objaverse.load_annotations(uids)
    print(annotations)

