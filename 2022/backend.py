import time
import os
import io
def run(function : callable, input):
    """Runs a function based on some inputs to get some nicely formatted answers. The function is expected to have as first argument an input file"""
    t0 = time.perf_counter()
    result = function(input)
    t1 = time.perf_counter()
    print(f"Answer: {result}           {(t1-t0) : .6f} seconds")
    return result

def test(function : callable, input, expectedResult):
    result = run(function, input)
    assert result == expectedResult, "Test failed..."
    print("Test succeeded.")

def parseInput(input : str | io.TextIOWrapper, parseFunction = str.splitlines, **kwargs):
    if type(input) == io.TextIOWrapper : input = input.read()
    inputElements = input if not parseFunction else parseFunction(input, **kwargs)
    return inputElements

