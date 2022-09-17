from py2exe import freeze

freeze(
    console=[{"script": "scripts/sample.py"}],
    options={"py2exe": {"includes": ["sample"]}},
)
