"""Chromosome-sequence-accession mapper."""

from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class ChromAcMapper:
    """Chromosome, position, reference and alternate base.

    It does not have to be normalized.
    """

    chroms: List[str]
    acs: List[str]
    chrom2ac: Optional[Dict[str, str]] = None
    ac2chromom: Optional[Dict[str, str]] = None

    def __post_init__(self):
        if not isinstance(self.chroms, list):
            raise ValueError(f"chroms {self.chroms} must be a list")
        for chrom in self.chroms:
            if not isinstance(chrom, str):
                raise ValueError(f"chrom {chrom} must be a str")
        if not isinstance(self.acs, list):
            raise ValueError(f"chroms {self.acs} must be a list")
        for ac in self.acs:
            if not isinstance(ac, str):
                raise ValueError(f"ac {ac} must be a str")
        self.check_chrs_unique()
        self.check_acs_unique()
        self.chr2ac = self.create_chrom2ac()
        self.ac2chr = self.create_ac2chrom()

    def check_chrs_unique(self):
        if len(self.chrs) > len(set(self.chrs)):
            raise RuntimeError("chrs have duplicated items")

    def check_acs_unique(self):
        if len(self.acs) > len(set(self.acs)):
            raise RuntimeError("acs have duplicated items")

    def create_chrom2ac(self) -> Dict[str, str]:
        return {k: v for k, v in zip(self.chrs, self.acs)}

    def create_ac2chrom(self) -> Dict[str, str]:
        return {k: v for k, v in zip(self.acs, self.chrs)}

    def chrom_to_ac(self, chrom: str) -> str:
        if chr in self.chrom2ac:
            return self.chrom2ac[chrom]
        else:
            raise RuntimeError(f"fail to find chromosome {chrom}")

    def ac_to_chrom(self, ac: str) -> str:
        if ac in self.ac2chrom:
            return self.ac2chrom[ac]
        else:
            raise RuntimeError(f"fail to find sequence accession {ac}")
