# Intro to Snakeviz
Snakeviz is a tool to visualize the report of the standard Python profiler cProfile.

#How to launch Snakeviz

Snakeviz generated two charts by default 
- icicle chart
- sunburst chart
but we can change the chart from the dropdown. All individual lines of profiling will be shown as the table below visualization.

##    Icicle Chart
 The icicle chart uses rectangles to represent the time taken by functions. We can see that the total time taken by our script is ~8.38 seconds. The rectangles for fast_random_generator, slow_random_generator and very_slow_random_generator are shown inside of rectangle of main_func(). We can further click on a rectangle of any of that functions and it'll be set as root rectangle and all sub-functions called inside it'll be as rectangles below it. The rectangles are organized like a tree structure in a fashion in which they were called and the width of the rectangle represents the time taken by that function in the caller function of that function.
  
##  Sunburst Chart
 The sunburst chart uses the angular extent of arc to represent the time taken by functions. We can see exactly same way as icicle chart that arc of fast_random_generator, slow_random_generator and very_slow_random_generator are shown inside extent of arc of main_func(). We can click on any arc and that arc will become a root arc and functions called inside it'll be shown as arcs around it.



## Chart commands
On the left you can find buttons:

-    Function Information: We can hover over the rectangle in the icicle chart or arc in the sunburst chart and it'll show which information of function which it represents on the left side. It'll show the name of the function, cumulative time, file in which the function is present, line number on which it gets called, and directory of file.
-    Call Stack: The Call Stack button present on top right represents the call stack. If we click on any rectangle or arc then the chart will make that node as the root node and all sub-nodes will show functions called inside it. It'll take us deep into that function. If we have gone deep into functions analyzing them one by one and want to know our stack path then we can click on the Call Stack button and it'll show us call stack. We can also click on any entry in it and it'll take us to that level.
-    Stats Table: The stats table looks exactly the same as that of output generated by cProfile. It'll be displayed below chart. Each of the lines of the state table is clickable representing function calls and when we click on any line that line will be made root node of the chart and all functions called inside it will be shown as sub-nodes. Please feel free to visit our tutorial on cProfile which explains what each column means in this table in-depth.
-    Reset Root: If we have changed the root of the chart by clicking on the row of the stats table than we can click on this button to reset the root to the original.
-    Reset Zoom: If we have zoomed into profiling by clicking in on any rectangle or arc then we can reset it by clicking this button.

-    Style: The style has two options for two chart types
        Icicle
        Sunburst
-    Depth: The Depth dropdown lets us select how deep into call stack snakeviz goes when creating a visualization. The calls below this depth won't be shown into the chart until we click on one of the top functions which call it. We can increase profile depth and that many levels will be shown in the chart at once.
-    Cutoff: The Cutoff dropdown can let us decide whether to display function calls which takes up very little time of their parent’s cumulative time. If we set CutOff to some value then for each function we check for the ratio of its cumulative time and its parent’s cumulative time. If the ratio is less than the cutoff value then that function will be displayed but the chart won't be constructed for sub-functions inside of that function which means that we can't click on that function anymore to see time spent on sub-functions inside it. If we set a high cutoff then the chart will be generated faster as many sub-charts won't be generated.
