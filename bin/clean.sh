#!/bin/bash

find . -name __pycache__ | xargs rm -rf
find . -name .pytest_cache | xargs rm -rf
find . -name .ipynb_checkpoints | xargs rm -rf