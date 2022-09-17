"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
import pathlib
import versioneer
try:
    import py2exe
except ImportError:
    print("Can't find py2exe, will not be able to run py2exe")

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / "README.md").read_text(encoding="utf-8")

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name="sampleproject",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),  # Required
    python_requires=">=3.7, <4",
    entry_points={  # Optional
        "console_scripts": [
            "sample=sample:main",
        ],
    },
    console=[{"script": "scripts/sample.py"}],
    options={"py2exe": {"includes": ["sample"]}},
)
