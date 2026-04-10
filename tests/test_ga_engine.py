
import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.ga_engine import GeneticAlgorithm

@pytest.fixture
def ga():
    return GeneticAlgorithm(pop_size=10, mutation_rate=0.1)

def test_calculate_fitness(ga):
    assert ga.calculate_fitness([1, 1, 1, 0, 0, 0, 0, 0]) == 3

def test_population_size():
    assert len(GeneticAlgorithm(pop_size=50).population) == 50

def test_crossover_length(ga):
    assert len(ga.crossover([1]*8, [0]*8)) == 8

def test_invalid_mutation():
    with pytest.raises(ValueError):
        GeneticAlgorithm(mutation_rate=5.0)

def test_selection_count(ga):
    assert len(ga.select_parents()) == 2

