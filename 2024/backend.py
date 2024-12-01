import time
import os
import io
import re


run_results = dict()

## Section splitting
def paragraphs(text : str) : return(text.split("\n\n"))
def kRows(K : int) : "Creates sections of K rows."; return lambda W : list(W.splitlines()[k*K:(k+1)*K] for k in range(len(W.splitlines())//K))
def columns(text : str) :
    """Splits the text into rows and returns the columns, assuming there are spaces between each column"""
    rows = text.splitlines()
    columns = ["" for _ in range((max(map(len, rows))))] # placeholder
    for i in range(len(rows)):
        for j in range(len(rows[i])):
            columns[j] += rows[i][j]
    return columns
lines = str.splitlines

## Parsing
def parseInts(text : str) -> tuple[int]: return tuple(map(int, re.findall(r"\d+", text)))
def parseLetters(text : str) -> tuple[str]: return tuple(map(str, re.findall(r"[a-zA-Z]", text)))
def parseWords(text : str) -> tuple[str] : return tuple(map(str, re.findall(r"[^ ]+", text)))

def run(function : callable, input, day : int, part : int):
    """Runs a function based on some inputs to get some nicely formatted answers. The function is expected to have as first argument an input file"""
    t0 = time.perf_counter()
    result = function(input)
    t1 = time.perf_counter()
    if day != None:
        print(f"Answer for day {day} part {part}: {result}           {(t1-t0) : .6f} seconds")
        run_results.update({f"Day {day} part {part}" : {"result" : result, "time" : (t1-t0)}})
    else:
        print(f"Answer: {result}           {(t1-t0) : .6f} seconds")
    return result

def test(function : callable, input, expectedResult):
    result = run(function, input, day = None, part = None)
    assert result == expectedResult, f"Test failed. Expected {expectedResult}, but got {result} instead."
    print("Test succeeded.")


def parseInput(input : str, parseMethod = None, sections = lines, ignoreEmpty = False, surpress = False):
    if not surpress : print(f"{10*"_"} Input to be parsed {10*"_"}")
    for line in input.splitlines()[:5] : print(line)
    if not surpress : print("... and maybe more")
    if not surpress : print(20*"_")
    inputSections = sections(input)
    parsedInputs = list(map(parseMethod, inputSections)) if parseMethod else inputSections
    if ignoreEmpty : parsedInputs = [parsedInput for parsedInput in parsedInputs if len(parsedInput) >= 1]
    if not surpress : print(f"{10*"_"} Parsed input {10*"_"}")
    for parsedInput in parsedInputs[:5] : print(f"{parsedInput}")
    if not surpress : print("... and maybe more")
    if not surpress : print(20*"_")
    if len(parsedInputs) == 1 : parsedInputs = parsedInputs[0]
    return parsedInputs
