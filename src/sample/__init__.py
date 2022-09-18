from . import _version
__version__ = _version.get_versions()['version']

def main():
    """Entry point for the application script"""
    print(f"Sample v{__version__}")
