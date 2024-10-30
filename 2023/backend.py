import time
def run(function : callable, **kwargs):
    """Runs a function based on some inputs to get some nicely formatted answers. The function is expected to have as first argument an input file"""
    t0 = time.perf_counter()
    result = function(**kwargs)
    t1 = time.perf_counter()
    print(f"Completed in {t1 - t0 : .2f} seconds.")
    print(f"Answer: \n{result}")
