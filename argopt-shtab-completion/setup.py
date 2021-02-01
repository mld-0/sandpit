
import re
from setuptools import setup

version = re.search(
    '^__version__\s*=\s*"(.*)"',
    open('greeter/__main__.py').read(),
    re.M
    ).group(1)


setup(
    name='greeter',
    entry_points={
    'console_scripts': [
        'greeter=greeter.__main__:cligreet'
    ],
    },
)

