from functools import lru_cache


@lru_cache(None)
def fab(n):

    print(n)

    return None


fab(10)
fab(10)
fab(10)
fab(9)
fab(9)
