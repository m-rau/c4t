from setuptools import find_packages

try:
    from core4.setup import setup
except:
    try:
        from core4.script.installer.core4.setup import setup
    except:
        from setuptools import setup

import c4t

setup(
    name="c4t",
    version=c4t.__version__,
    packages=find_packages(exclude=['docs*', 'tests*']),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        "core4 @ git+https://github.com/plan-net/core4.git@develop"
    ]
)