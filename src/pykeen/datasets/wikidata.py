"""Wikidata(raw from OpenKE resource) datasets."""

from typing import Optional

from .base import PathDataSet, TarFileRemoteDataSet

__all__ = [
    'WIKIDATA'
]


class WIKIDATA(PathDataSet):

    def __init__(self, **kwargs):
        super().__init__(
            training_path='/local/scratch/Wikidata/train.tsv',
            testing_path='/local/scratch/Wikidata/test.tsv',
            validation_path='/local/scratch/Wikidata/valid.tsv',
            **kwargs,
        )