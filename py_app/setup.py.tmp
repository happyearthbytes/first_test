from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / "README.rst").read_text(encoding="utf-8")

setup(
    name='test_app',
    version='0.1.0',
    description='Python Distribution Utilities',
    long_description=long_description,
    author='Greg Ward',
    author_email='gward@python.net',
    url='https://www.python.org/sigs/distutils-sig/',
    packages=find_packages(where="app"),
    include_package_data=True,
    package_dir={'': 'app'},
    package_data={'app': ['data/*.dat']},
    data_files=[('bitmaps', ['bm/b1.gif', 'bm/b2.gif']),
                ('config', ['cfg/data.cfg'])],
    classifiers=[
        "Development Status :: 3 - Alpha",
        'Environment :: Console',
        'Environment :: Web Environment',
        'Intended Audience :: End Users/Desktop',
        'Intended Audience :: Developers',
        "License :: OSI Approved :: MIT License",
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Topic :: Software Development :: Bug Tracking',
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
    ],
    keywords="sample, setuptools, development",
    python_requires=">=3.7, <4",
    entry_points={
        "console_scripts": [
            "test_app=app.__main__:main",
        ],
    },
    project_urls={
        "Source": "https://github.com/pypa/sampleproject/",
    },
)
