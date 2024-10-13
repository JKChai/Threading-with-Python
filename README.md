# Threading-with-Python

Just wanna to playaround with Threads as Python 3.13 provide ability to make GIL optional 🤯

## CPU BOUND VS I/O BOUND

**CPU BOUND** refers to the time it takes to complete a task, job, process is primarily determined by the speed of CPU 

**I/O BOUND** refers to the time it takes to complete a task, job, process is primarily determined by the speed of I/O subsytem such as reading data from a disk

[Reference StackOverflow](https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)

## Global Interpreter Lock 

Only allow one thread at a time through CPyton interpreter as a way to ensure thread safety, as back then multithreading was not that common.

In Python 3.13, GIL is now optional and can bet set from the command line or Python script. Note that only interpreter such as CPython with `--disable-gil` build configuration can enable this feature.

```shell
# Command Line Option
# disable with flag 0; enable with flag 1 
py3 -X gil=0 ./main.py
```

```py
# Scripting Option
import os
os.environ["PYTHON_GIL"] = "0" 
```

Use the new System module function to check if GIL is enabled.

```py
import sys

sys._is_gil_enabled()
```

[Reference Wiki Python](https://wiki.python.org/moin/GlobalInterpreterLock)

[Reference PEP 703](https://peps.python.org/pep-0703/)

[Reference Python Docs](https://docs.python.org/3/whatsnew/3.13.html)


## Multithreading vs Multiprocessing

This has been a truly confusing topic for me especially Multithreading in Python with GIL.

Based on my understanding, Python multi-threading spawn multiple threads within a process that has the shared resources but with their own register and stack. 

In Python with GIL, GIL will lock a thread and release another thread one at a time, which limits only one thread through the interepreter, that is, one thread will start then the other then the next etc. and then will finish one after another.

Multi-processing differs in the sense that it is running on different processes for each CPU and will require some overhead to setup the resources including one interpreter for one process which allow the program to run in parallel. 

With the emergence of diabling GIL, Multi-threading and Multi-processing seems to be bluring as Multi-threading used to be Concurrent and Multi-processing is Parallel. The point is that multi-threading with **NO GIL** seems to be running parallel too as it doesn't have to wait for the Acquire and Realease of GIL. The only different that I can see with no GIL is that multi-threading should be faster than multi-processing as it uses shared resources  (i.e., same memory space) within a process reducing the need for setting up new resources. Without GIL, Python Multi-Threading seems to be Concurrent and Parallel as it can now fire up multiple cores for different tasks. 

[Reference Geek for Geek](https://www.geeksforgeeks.org/difference-between-multithreading-vs-multiprocessing-in-python/)

> Working-In-Progress... 🔨

