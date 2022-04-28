"""
    Importing all the modules needed for Lottery program
"""

try:
    import pandas as pd
    from datetime import datetime as dt
except:
    print("One/more packages are not available to import")

if __name__ == '__main__':
    print("Packages were imported from this standalone module file")
else:
    print("Packages were imported from modules/imports.py")