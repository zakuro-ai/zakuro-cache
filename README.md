![zakuro Logo](imgs/zakuro.png)

--------------------------------------------------------------------------------

ZakuroCache is a Python package that provides two high-level features:
- A simple decorator to identify the pure functions you want to cache.
- A caching system that never repeat twice the same execution and return a cached result instead. 


You can reuse your favorite Python packages such as NumPy, SciPy and Cython to extend ZakuroCache integration.


## ZakuroCache modules

At a granular level, ZakuroCache is a library that consists of the following components:

| Component | Description |
| ---- | --- |
| **zakuro_cache** | Contains the implementation of the caching sytem. |
| **zakuro_cache.loggers** | Keep the print into an array during the fuction execution. |
| **zakuro_cache.function** | Pipeline to execute and store.|

## Installation

### Docker
To build the image with docker-compose
```
sh docker.sh
```

### Local
```
python setup.py install
```
## Performances
If you are in local env you can run:
```
python demo.py
```

You should be able to execute a benchmark:
```
=====ZAKURO-CACHE=====
0.03user 0.00system 0:00.03elapsed 97%CPU (0avgtext+0avgdata 15444maxresident)k
0inputs+128outputs (0major+2493minor)pagefaults 0swaps


=====NO-CACHE=====
10.18user 0.00system 0:10.18elapsed 99%CPU (0avgtext+0avgdata 15568maxresident)k
496inputs+128outputs (3major+2491minor)pagefaults 0swaps
```


## Getting-started
To apply the cache simply add the decorator to your functions.
```python
from zakuro_cache.function import pure

@pure
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        res1, res2 = recur_fibo(n - 1), recur_fibo(n - 2)
        return res1 + res2


if __name__ == "__main__":
    nterms = 35
    for i in range(nterms):
       print(recur_fibo(i))
```
