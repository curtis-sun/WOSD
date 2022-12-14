import numpy as np
import struct
import os

def downsample(fn):
    if os.path.exists("data/" + fn + "_50M_uint64") and os.path.exists("data/" + fn + "_50M_uint32"):
        return

    print("Downsampling 50M", fn)
    if os.path.exists("data/" + fn + "200M_uint64"):
        d_64 = np.fromfile("data/" + fn + "_200M_uint64", dtype=np.uint64)[1:]
        nd_64 = d_64[::2]
        with open("data/" + fn + "_100M_uint64", "wb") as f:
            f.write(struct.pack("Q", len(nd_64)))
            nd_64.tofile(f)
        nd_64 = d_64[::4]
        with open("data/" + fn + "_50M_uint64", "wb") as f:
            f.write(struct.pack("Q", len(nd_64)))
            nd_64.tofile(f)
        nd_64 = d_64[::8]
        with open("data/" + fn + "_25M_uint64", "wb") as f:
            f.write(struct.pack("Q", len(nd_64)))
            nd_64.tofile(f)
        nd_64 = d_64[::16]
        with open("data/" + fn + "_12500K_uint64", "wb") as f:
            f.write(struct.pack("Q", len(nd_64)))
            nd_64.tofile(f)
    
    if os.path.exists("data/" + fn + "200M_uint32"):
        d_32 = np.fromfile("data/" + fn + "_200M_uint32", dtype=np.uint32)[1:]
        nd_32 = d_32[::2]
        with open("data/" + fn + "_100M_uint32", "wb") as f:
            f.write(struct.pack("Q", len(nd_32)))
            nd_32.tofile(f)
        nd_32 = d_32[::4]
        with open("data/" + fn + "_50M_uint32", "wb") as f:
            f.write(struct.pack("Q", len(nd_32)))
            nd_32.tofile(f)
        nd_32 = d_32[::8]
        with open("data/" + fn + "_25M_uint32", "wb") as f:
            f.write(struct.pack("Q", len(nd_32)))
            nd_32.tofile(f)
        nd_32 = d_32[::16]
        with open("data/" + fn + "_12500K_uint32", "wb") as f:
            f.write(struct.pack("Q", len(nd_32)))
            nd_32.tofile(f)

downsample("books")
downsample("fb")
downsample("osm_cellids")
downsample("wiki_ts")
