import time
import os
import io
def run(function : callable, **kwargs):
    """Runs a function based on some inputs to get some nicely formatted answers. The function is expected to have as first argument an input file"""
    t0 = time.perf_counter()
    result = function(**kwargs)
    t1 = time.perf_counter()
    print(f"Completed in {t1 - t0 : .2f} seconds.")
    print(f"Answer: \n{result}")
    return result

def test(function : callable, expectedResult, **kwargs):
    result = run(function, **kwargs)
    assert result == expectedResult, "Test failed..."
    print("Test succeeded.")

def parseInput(input : str | io.TextIOWrapper, parseFunction = str.splitlines, printAll = False, *args):
    if type(input) == io.TextIOWrapper :
        print(f"[Parse of {input.name}]")
    else:
        print(f"[Parse]")
    if type(input) == io.TextIOWrapper : input = input.read()
    inputElements = parseFunction(input, *args)
    for inputElement in inputElements[:5] if not printAll else inputElements:
        print(inputElement)
    if not printAll : print(".\n"*4)
    return 

