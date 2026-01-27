import argparse

from zakuro_cache.function import pure


@pure
def recur_fibo(n):
    return core(n, recur_fibo)


def _recur_fibo(n):
    return core(n, _recur_fibo)


def core(n, f):
    if n <= 1:
        return n
    else:
        res1, res2 = f(n - 1), f(n - 2)
        return res1 + res2


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process some integers.")
    parser.add_argument("--nterms", type=int, default=35)
    parser.add_argument("--nocache", action="store_true")
    args = parser.parse_args()

    f, header = (
        (_recur_fibo, "=====NO-CACHE=====")
        if args.nocache
        else (recur_fibo, "=====ZAKURO-CACHE=====")
    )
    print(f"\n\n{header}")
    [f(i) for i in range(args.nterms)]
