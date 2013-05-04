from distutils.core import setup
setup(
    name='python-sensuclient',
    version='0.0',
    author='Chris LaRose',
    author_email='cjlarose@iplantcollaborative.org',
    packages=['sensuclient'],
    install_requires=[
        'requests',
    ]
)
