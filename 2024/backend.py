import time
import os
import io
import re
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.patches
import numpy as np

run_results = list()

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
def ignoreLineBreaks(text : str) : return(text.replace("\n",""))

## Parsing
def parseInts(text : str) -> tuple[int]: return tuple(map(int, re.findall(r"\d+", text)))
def parseDigits(text : str) -> tuple[int]: return tuple(map(int, re.findall(r"\d", text)))
def parseLetters(text : str) -> tuple[str]: return tuple(map(str, re.findall(r"[a-zA-Z]", text)))
def parseWords(text : str) -> tuple[str] : return tuple(map(str, re.findall(r"[^ ]+", text)))

def run(function : callable, input, day : int, part : int, n_runs = 40, incorrect = False):
    """Runs a function based on some inputs to get some nicely formatted answers. The function is expected to have as first argument an input file"""
    run_times = []
    for _ in range(n_runs):
        t0 = time.perf_counter()
        result = function(input)
        t1 = time.perf_counter()
        run_times.append(t1-t0)
    if day != None:
        print(f"Answer for day {day} part {part}: {result}  Average time {sum(run_times)/len(run_times) : .6f} seconds")
        if incorrect:
            run_results.append({"Day" : day, "Part" : part, "Result" : "Incorrect", "Time" : None})
        else:
            run_results.append({"Day" : day, "Part" : part, "Result" : result, "Time" : sum(run_times)/len(run_times)})
    else:
        print(f"Answer: {result}           {sum(run_times)/len(run_times) : .6f} seconds")
    return result

def test(function : callable, input, expectedResult):
    result = run(function, input, day = None, part = None, n_runs = 1)
    assert result == expectedResult, f"Test failed. Expected {expectedResult}, but got {result} instead."
    print("Test succeeded.")


def parseInput(input : str, parseMethod = None, sections = lines, ignoreEmpty = False, surpress = False):
    if not surpress : print(f"{10*"_"} Input to be parsed {10*"_"}")
    if not surpress :
        for line in input.splitlines()[:5] : print(line)
    if not surpress : print("... and maybe more")
    if not surpress : print(20*"_")
    inputSections = sections(input)
    parsedInputs = list(map(parseMethod, inputSections)) if parseMethod else inputSections
    if ignoreEmpty : parsedInputs = [parsedInput for parsedInput in parsedInputs if len(parsedInput) >= 1]
    if not surpress : print(f"{10*"_"} Parsed input {10*"_"}")
    if not surpress :
        for parsedInput in parsedInputs[:5] : print(f"{parsedInput}")
    if not surpress : print("... and maybe more")
    if not surpress : print(20*"_")
    if len(parsedInputs) == 1 : parsedInputs = parsedInputs[0]
    return parsedInputs

def overall_results():
    return pd.DataFrame(run_results)

def total_avg_runtime():
    return f"The total runtime is on average {pd.DataFrame(run_results)['Time'].sum() : .2f} seconds"

def complexity_increase_per_day():
    df = pd.DataFrame(run_results)
    grouped_df = df[df["Result"] != 'Incorrect'].groupby("Day").apply(lambda x : x.max()/x.min())
    return(grouped_df["Time"].transpose())

def plot_results():
    day_gap = 1.3
    part_gap = 0.4
    bar_width = 0.95*part_gap
    fig, axs = plt.subplots(figsize = (6,6))
    days = np.arange(len(run_results) // 2)
    day_strings = [f"Day {day+1}" for day in days]
    patches = [matplotlib.patches.Patch(facecolor = "blue", label = "Part 1"),
               matplotlib.patches.Patch(facecolor = "orange", label = "Part 2")]
    for problem in run_results:
        day, part, result, time = problem.values()
        color = "blue" if part == 1 else "orange"
        if result == "Incorrect" : continue
        bar = axs.bar(day_gap*(day) + part_gap*(part-1), height = time, width = bar_width, color = color)
        axs.bar_label(bar, padding = 3, fmt = "{:.2}")
    axs.set_xticks(day_gap*(days+1) + 0.5*bar_width, day_strings)
    axs.set_ylim(0, 1)
    axs.legend(handles = patches)
    axs.set_ylabel("Run time (seconds)")