"""Convert Cpra to Spra."""

from ..chromacmapper import ChromAcMapper
from .cpra import Cpra
from .spra import Spra


class CpraToSpraConverter:

    def __init__(self, chrom_ac_mapper: ChromAcMapper):
        self.chrom_ac_mapper = chrom_ac_mapper

    def convert(self, cpra: Cpra) -> Spra:
        ac = self.chrom_ac_mapper.chrom_to_ac(chr=cpra.chrom)
        spra = Spra(ac=ac, pos=cpra.pos, ref=cpra.ref, alt=cpra.alt)
        return spra
