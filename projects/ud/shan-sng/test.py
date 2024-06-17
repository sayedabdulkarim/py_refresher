try:
    import numpy
    print(f'NumPy is installed, version: {numpy.__version__}')
except ImportError:
    print('NumPy is not installed')

try:
    import pandas
    print(f'Pandas is installed, version: {pandas.__version__}')
except ImportError:
    print('Pandas is not installed')

try:
    import matplotlib
    print(f'Matplotlib is installed, version: {matplotlib.__version__}')
except ImportError:
    print('Matplotlib is not installed')
