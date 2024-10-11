# Threading-with-Python

Just wanna to playaround with Threads as Python 3.13 provide ability to make GIL optional 🤯

## CPU BOUND VS I/O BOUND

**CPU BOUND** refers to the time it takes to complete a task, job, process is primarily determined by the speed of CPU 

**I/O BOUND** refers to the time it takes to complete a task, job, process is primarily determined by the speed of I/O subsytem such as reading data from a disk

[Reference 1](https://stackoverflow.com/questions/868568/what-do-the-terms-cpu-bound-and-i-o-bound-mean)

# Global Interpreter Lock 

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
[Reference PEP 703](ttps://peps.python.org/pep-0703/)
[Reference Python Docs](https://docs.python.org/3/whatsnew/3.13.html)

> Working-In-Progress... 🔨

