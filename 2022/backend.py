import time
import os
import io
import re

## Section splitting
def paragraphs(text : str) : return(text.split("\n\n"))
def kRows(K : int) : "Creates sections of K rows."; return lambda W : list(W.splitlines()[k*K:(k+1)*K] for k in range(len(W.splitlines())//K))
lines = str.splitlines

## Parsing
def parseInts(text : str) -> tuple[int]: return tuple(map(int, re.findall(r"\d+", text)))
def parseLetters(text : str) -> tuple[str]: return tuple(map(str, re.findall(r"[a-zA-Z]", text)))

def run(function : callable, input):
    """Runs a function based on some inputs to get some nicely formatted answers. The function is expected to have as first argument an input file"""
    t0 = time.perf_counter()
    result = function(input)
    t1 = time.perf_counter()
    print(f"Answer: {result}           {(t1-t0) : .6f} seconds")
    return result

def test(function : callable, input, expectedResult):
    result = run(function, input)
    assert result == expectedResult, f"Test failed. Expected {expectedResult}, but got {result} instead."
    print("Test succeeded.")



def parseInput(input : str, parseMethod = None, sections = lines):
    print(f"{10*"_"} Input to be parsed {10*"_"}")
    for line in input.splitlines()[:5] : print(line)
    print("... and maybe more")
    print(20*"_")
    inputSections = sections(input)
    parsedInputs = list(map(parseMethod, inputSections)) if parseMethod else inputSections
    print(f"{10*"_"} Parsed input {10*"_"}")
    for parsedInput in parsedInputs[:5] : print(f"{parsedInput}")
    print("... and maybe more")
    print(20*"_")
    return parsedInputs
