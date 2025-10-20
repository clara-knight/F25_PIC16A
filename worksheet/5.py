def product(*args, **kwargs):
    kwargs["result"] = 1

    for n in args:
        kwargs["result"] *= n
    print(kwargs["result"])


product(1, 2, 3, result=0)
