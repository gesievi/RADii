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
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Radii Documentation'
copyright = '2023, ETH Zuerich Chair of Gramazio & Kohler'
author = 'Gereon Sievi'

# The full version, including alpha/beta/rc tags
release = '0.37'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    ]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', "tutorial/grashopper/documentation_rst/Vorlage.rst", "conf2.py", "index2.rst", "readme.rst"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'

html_theme_options =  {
    'fixed_sidebar' : 'False',
    'github_banner' : 'False' ,
    'github_repo'   : "RADii",
    'github_button' : 'true',
    'github_user'   : 'gesievi/',
    'show_relbars' : 'False',
    'show_related' : 'True',
    'font_family'   : 'OfficeCodePro-Regular.otf',

}

# things that i have not gotten to work so far
#'logo': '/tutorial/grashopper/images/Icons/logo.png', 
# font_family = {"../docs/_Font/OfficeCodePro/OfficeCodePro-Medium.oft"}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_Font']


# Prolog for linking between files https://www.sphinx-doc.org/en/master/usage/configuration.html#confval-rst_prolog
# the Radii Logo can be called with |xyz|
rst_prolog = """

.. _RadiiViewer: https://gesievi.github.io/Radii_doc/tutorial/Viewer_PC/documentation_rst/0_Viewer.html
.. _RadiiGrashopper: https://gesievi.github.io/Radii_doc/tutorial/grashopper/documentation_rst/01_Components_Overview.html
.. _Setup: https://gesievi.github.io/Radii_doc/tutorial/Setup/install_setup.html

.. _Radii Grashopper Win/Mac: https://radii.info/download/plugin/RADii.zip
.. _Radii Capture Win/Mac: https://radii.info/download/plugin/RADiiCapture.zip
.. _Windows 10+: https://radii.info/download/standard/RADii%20Viewer%20Setup.zip
.. _macOS X: https://apps.apple.com/app/id1505325031
.. _VR .apk: https://radii.info/download/vr/RADii%20Viewer%20VR.zip

.. _Connect: https://gesievi.github.io/Radii_doc/tutorial/grashopper/documentation_rst/02_connect.html
.. _PublishGeometry: https://gesievi.github.io/Radii_doc/tutorial/grashopper/documentation_rst/03_publish_geometry.html
.. _PublishMaterial: https://gesievi.github.io/Radii_doc/tutorial/grashopper/documentation_rst/04_publish_material.html

.. _RadiiViewer: https://gesievi.github.io/Radii_doc/tutorial/Viewer_PC/documentation_rst/0_Viewer.html
.. _ConnectMenu: https://gesievi.github.io/Radii_doc/tutorial/Viewer_PC/documentation_rst/1_Connect.html

"""