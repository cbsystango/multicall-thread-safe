from setuptools import setup

setup(
    long_description="""
        # Thread Safe Multicall

        Thread Safe multicall for seam less integration with dockerized containers,  [multicall](https://github.com/banteg/multicall.py) module  doesn't allow threaded execution, here we address that issue and create a configuration option to enable or disable multithreaded execution.

        To enable Thread Safe Execution of Multicall configure enviornment variable `ASYNC_W3=0` 
    """
)
