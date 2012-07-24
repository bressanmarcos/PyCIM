import os

kwds = {}

if int(os.getenv('USE_DISTUTILS', 0)) != 0:
    from distutils.core import setup
    def find_packages():
        packages = []
        basedir = os.getcwd()
        for root, dirnames, filenames in os.walk(basedir):
            for dirname in dirnames:
                initfile = os.path.join(root, dirname, "__init__.py")
                if os.path.exists(initfile):
                    # python 2.4+
                    packages.append(os.path.relpath(initfile, basedir))
        packages = [ os.path.dirname(p).replace(os.path.sep, ".") for p in packages ]
        return sorted(packages)

    # To add the test data to the final package
    if int(os.getenv('INCLUDE_PACKAGE_DATA', 0)) != 0:
        kwds['package_data'] = { 'PyCIM.Test' : [ 'Data/*'], }
else:
    from setuptools import setup, find_packages
    kwds['include_package_data'] = False
    kwds['test_suite'] = "PyCIM.Test"
    kwds['zip_safe'] = True   
    

# Read the long description from the README.
thisdir = os.path.abspath(os.path.dirname(__file__))
f = open(os.path.join(thisdir, "README"))
kwds["long_description"] = f.read()
f.close()

setup(name="PyCIM",
      version="15.13.4",
      author="Richard Lincoln",
      author_email="r.w.lincoln@gmail.com",
      description="Python implementation of the Common Information Model.",
      license="MIT",
      url="http://www.pycim.org/",
      packages=find_packages(),
      **kwds)

# python setup.py sdist bdist_egg bdist_wininst bdist_msi upload
