from setuptools import setup, find_packages

setup(
    name='GP_Sinkhorn',
    packages=find_packages(),
    install_requires=[
        'torch',
        'tqdm',
        'numpydoc',
        'seaborn',
        'celluloid',
        'pyro-api',
        'pyro-ppl',
        'jupyter',
        'GPy',
        'pods'
    ]
)
