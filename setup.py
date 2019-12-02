from distutils.core import setup
from distutils.extension import Extension

# To install library to Python site-packages run "python setup.py install"

setup(name='pycococreatortools',
    packages=['pycococreator'],
    package_dir = {'pycococreator': 'pycococreator'},
    version='0.1.0',
    description = 'Tools to create COCO datasets',
    url = 'https://github.com/Faresx/pycococreator',
    author = 'fares',
    author_email = 'fyzxst@gmail.com',
    download_url = 'https://github.com/Faresx/pycococreator/archive/0.1.0.tar.gz',
    keywords = ['coco', 'dataset', 'machine-learning'],
    install_requires=[
        'numpy', 'pillow', 'scikit-image'
    ],
)
