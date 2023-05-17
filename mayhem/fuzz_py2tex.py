#!/usr/bin/python3
import atheris
import sys
from pytexit import py2tex

def TestOneInput(data):
    fdp = atheris.FuzzedDataProvider(data)

    expr = fdp.ConsumeUnicodeNoSurrogates(100)

    try:
        py2tex(expr)
    except SyntaxError:
        pass
    except ValueError:
        pass
    except TypeError:
        pass

atheris.instrument_all()
atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()