from os import path
import sys


ROOT_FOLDER = path.abspath(
    path.join(
        path.dirname(__file__), '..'
    )
)
OUTPUT_FOLDER = path.join(ROOT_FOLDER, 'output')

sys.path.append(ROOT_FOLDER)
