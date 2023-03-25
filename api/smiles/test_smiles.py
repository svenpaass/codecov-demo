from .smiles import Smiles


def test_smile():
    assert Smiles.smiles() == ":)"


def test_frown():
    assert Smiles.frown() == ":("
