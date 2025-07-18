# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
from datetime import datetime 

sys.path.insert(0, os.path.abspath('../../'))
sys.path.insert(0, os.path.abspath('../../python/'))
# sys.path.insert(0, os.path.abspath('../../python/qvl'))
# for x in os.walk('../../../python'):
#   sys.path.insert(0, x[0])
#sys.path.insert(1, os.path.abspath('./common/'))

print(sys.path)


# -- Project information -----------------------------------------------------

year = datetime.now().year

project = "Quanser Interactive Labs API Documentation"
copyright = str(year) + ', Quanser'
author = 'Quanser'

# The full version, including alpha/beta/rc tags
# release number.year.dayInCalendar
release = '2.25.171'

# To deal with all the "duplicate label errors"
suppress_warnings = ['autosectionlabel.*']

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx_rtd_theme',
    'sphinx.ext.autosectionlabel',
    'sphinx.ext.doctest',
    'sphinx.ext.duration',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.viewcode',
    #'sphinx_collapse',
    'sphinx_panels',
    'sphinx_tabs.tabs',
    'sphinx.ext.napoleon'
    #'sphinx_toolbox',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.

#import sphinx_rtd_theme #sphinx_theme
html_theme = 'sphinx_rtd_theme' #'stanford_theme'
# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
#html_theme_path = [sphinx_theme.get_html_theme_path('stanford_theme')]
html_static_path = ['css'] #previously _static
#html_css_files = [ 'css']
html_theme_options = {
    'style_nav_header_background': 'white', #'#e21b22',
    'logo_only': True
}
html_logo = 'pictures/QL.png'

sphinx_tabs_disable_tab_closing = True

autodoc_preserve_defaults = True
autodoc_mock_imports = ['quanser', 'pyqtgraph', 'PyQT6']
