from line_profiler import LineProfiler

lprofiler = LineProfiler()

lp_wrapper = lprofiler(main_func)

lp_wrapper()
