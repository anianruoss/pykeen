"""DBPEDIA Subset datasets.
source: see paper: 
"""

from typing import Optional

from .base import PathDataSet, TarFileRemoteDataSet

__all__ = [
    'DBPEDIA_FAN'
]


class DBPEDIA_FAN(PathDataSet):

    def __init__(self, **kwargs):
        super().__init__(
            training_path='/local/scratch/dbpedia_fan/train2id.tsv',
            testing_path='/local/scratch/dbpedia_fan/test2id.tsv',
            validation_path='/local/scratch/dbpedia_fan/val2id.tsv',
            **kwargs,
        )