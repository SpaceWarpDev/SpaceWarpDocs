# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sphinx_rtd_theme
import os

# run command to install sphinx-rtd-dark-mode
os.system("pip install sphinx-rtd-dark-mode")

project = 'SpaceWarpDocs'
copyright = '2023, SpaceWarpDev'
author = 'Sinon'
release = '1.0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_rtd_dark_mode"]

default_dark_mode = False

templates_path = ['_templates']
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"
#html_logo = "_static/logo.png"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# -- Options for Languages ---------------------------------------------
# Enable internationalization support
needs_sphinx = '3.0'
gettext_compact = False   # optional, to make .mo files smaller
language = 'en'           # the default language
