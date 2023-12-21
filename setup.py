from setuptools import setup, find_packages

setup(
    name='GP_Sinkhorn',
    package_dir = {"": "gp_sinkhorn"},
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
