"""
code gently modified from original source at 
https://github.com/erikbern/ann-benchmarks/blob/18ba39b6a4af1243b26bf5fedc6c5c7ced791d70/ann_benchmarks/datasets.py
"""

import h5py
import os

from urllib.request import urlretrieve


def download(src, dst):
    if not os.path.exists(dst):
        # TODO: should be atomic
        print('downloading %s -> %s...' % (src, dst))
        urlretrieve(src, dst)


def get_dataset_fn(dataset):
    if not os.path.exists('data'):
        os.mkdir('data')
    return os.path.join('data', '%s.hdf5' % dataset)


def get_dataset(which):
    hdf5_fn = get_dataset_fn(which)
    try:
        url = 'http://ann-benchmarks.com/%s.hdf5' % which
        download(url, hdf5_fn)
    except:
        print("Cannot download %s" % url)
    hdf5_f = h5py.File(hdf5_fn, 'r')

    # here for backward compatibility, to ensure old datasets can still be used with newer versions
    dimension = hdf5_f.attrs['dimension'] if 'dimension' in hdf5_f.attrs else len(hdf5_f['train'][0])

    return hdf5_f, dimension
