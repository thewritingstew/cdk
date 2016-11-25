try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
        'description': 'This is a text-based game with default levels designed by elementary school students.',
        'author': 'Richard Stewart',
        'url': 'https://www.github.com/thewritingstew/cdk',
        'download_url': '',
        'author_email': 'richard.o.stewart@gmail.com',
        'version': '0.1',
        'install_requires': ['nose'],
        'packages': ['cdk'],
        'scripts': [],
        'cdk': 'cdk'
    }

setup(**config)
