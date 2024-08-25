from setuptools import setup, find_packages

setup(
    name='masonry_grid',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'Pillow',
    ],
    entry_points={
        'console_scripts': [
            'masonry-grid=masonry_grid.masonry:main',
        ],
    },
)
