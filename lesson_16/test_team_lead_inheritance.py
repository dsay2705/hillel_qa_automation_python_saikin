import pytest
from .homework_16 import TeamLead

def test_inherit_atributes():
    tl = TeamLead("Danylo", 9999, "Development", "Python", 9)

    assert hasattr(tl, "name")
    assert hasattr(tl, "salary")
    assert hasattr(tl, "department")
    assert hasattr(tl, "programming_language")
    assert hasattr(tl, "team_size")
