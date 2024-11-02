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
    print(f"{10*"-"} Input -> {len(input.splitlines())} lines {10*"-"}")
    for string in input.splitlines()[:10] : print(string)
    print("And maybe more...")
    print(20*"-")
    inputElements = input if not parseFunction else parseFunction(input, **kwargs)
    print(f"{10*"-"} Parsed -> {len(inputElements)} sections {10*"-"}")
    for inputElement in inputElements[:5] : print([inputElement])
    print("And maybe more...")
    print(20*"-")
    return inputElements

