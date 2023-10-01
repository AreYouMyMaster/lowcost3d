import os
import objaverse
import multiprocessing

if __name__ == "__main__":
    objaverse.BASE_PATH = "/rawdata3/objaverse/"
    objaverse._VERSIONED_PATH = os.path.join(objaverse.BASE_PATH, "hf-objaverse-v1")

    uids = objaverse.load_uids()
    processes = multiprocessing.cpu_count()
    objects = objaverse.load_objects(uids=uids, download_processes=processes)
