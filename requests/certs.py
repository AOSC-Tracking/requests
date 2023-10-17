#!/usr/bin/env python

"""
requests.certs
~~~~~~~~~~~~~~

This module returns the preferred default CA certificate bundle. There is
only one — the one from the certifi package.

If you are packaging Requests, e.g., for a Linux distribution or a managed
environment, you can change the definition of where() to return a separately
packaged CA bundle.

This AOSC-patched package returns "/etc/ssl/ca-bundle.crt" provided by the
ca-certs package.
"""

def where():
    """Return the absolute path to the system CA bundle."""
    return '/etc/ssl/ca-bundle.crt'

if __name__ == "__main__":
    print(where())
