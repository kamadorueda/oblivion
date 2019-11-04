"""Setup package."""

import distutils

distutils.core.setup(
    name='oblivion',
    packages=[
        'oblivion',
    ],
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'oblivion=oblivion.cli:cli',
        ],
    },
)
