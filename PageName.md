# PYROMS IS DEAD --- LONG LIVE OCTANT #

In an effort to be more inclusive to the GETM ( http://www.getm.net ) community, I have changed the name of pyroms to octant (and started a new code branch).  You can find it here:

http://octant.googlecode.com

Please head on over there, and check out the new code.


Thanks,

-Rob


---



#summary Pyroms is a suite of tools for working with the Regional Ocean Modeling System.

# Introduction #

The tools are based on [python](http://python.org), [numpy](http://numpy.scipy.org/) (with the full [scipy](http://www.scipy.org) package also recommended), [matplotlib](http://matplotlib.sourceforge.net) (with the [basemap toolkit](http://matplotlib.sourceforge.net/matplotlib.toolkits.basemap.basemap.html)), and [netcdf4-python](http://code.google.com/p/netcdf4-python/).  The grid generation is based on the command line utility [gridgen](http://www.marine.csiro.au/~sakov/).  All of these packages should be installed for your best and most fulfilling pyroms experience.

# Installation #

## Obtaining and Installing the Prerequisites ##

### gridgen ###

The command-line program **gridgen** is an orthogonal grid generator for the interiors of polygonal regions.  It is used for generating grids for our regional, coastal and estuarine hydrodynamic models, and can be obtained from:

http://www.marine.csiro.au/~sak007/

The full functionality of **gridgen** requires that you also install **gridutils**, which in turn requires **nn** and **csa** for full software satisfaction.  You can install **gridgen** without these, but it's easier to install full functionality at the start than to attempt to backtrack later.  To do so, download `gridgen.tar.gz`, `gridutils.tar.gz`, `csa.tar.gz` and `nn.tar.gz`, all of which are available on the indicated page.

Once you have downloaded these source code packages, you compile and install them as follows (with the following commands assuming that you have root access to install the programs for systemwide use):

```
tar xzvf csa.tar.gz
cd csa
./configure
make
su
make install
exit
cd ..
tar xzvf nn.tar.gz
cd nn
./configure
make
su
make install
exit
cd ..
tar xzvf gridutils.tar.gz
cd gridutils
./configure
make
su
make install
exit
cd ..
tar xzvf gridgen.tar.gz
cd gridgen
./configure
make
su
make install
exit
```

### netcdf4-python ###

This is a Python interface to the netCDF3 and netCDF4 libraries which, unsurprisingly, also need to be obtained and installed.  To avoid descending the prerequisite hierarchy all the way down to "obtain a computer," we'll just assume that netCDF3 and netCDF4 are already installed on our system.  It's not a trivial task to install them (as well as the HDF5 library required by netCDF4), but there's plenty of good advice on how to do so at the main **netCDF** site at:

http://www.unidata.ucar.edu/software/netcdf/

and the **netcdf-python** site at:

http://code.google.com/p/netcdf4-python/

The **netcdf4-python** package can be obtained from either the official releases page:

http://code.google.com/p/netcdf4-python/downloads/list

or via the following **Subversion** command:

`svn checkout http://netcdf4-python.googlecode.com/svn/trunk/ netcdf4-python-read-only`

with the former offering a more stable release, and the latter a bleeding-edge version which probably has more functionality.

Assuming you took the latter option, installation is as follows.  Note carefully that the `/opt/hdf5` and `/opt/netcdf4` are just placeholders in these instructions.  These are the locations where the netCDF4 and HDF5 libraries are installed, and will almost certainly be different on your system.  And they **must** be specified as the installation script will not look for them.

```
cd netcdf4-python-read-only
export HDF5_DIR=/opt/hdf5
export NETCDF4_DIR=/opt/netcdf4
python setup.py build
su
python setup.py install
exit
```

### numpy and scipy ###

The **numpy** and **scipy** packages can be thought of as Matlab without the fees, i.e. a free
system for performing numerical and scientific calculations.  They can be downloaded from:

http://www.scipy.org/Download

which also gives the choice of official releases or Subversion repository checkouts.  Assuming again that you choose the latter, they can be obtained via:

```
svn co http://scipy.org/svn/numpy/trunk numpy
svn co http://scipy.org/svn/scipy/trunk scipy
```

which will download the latest source code into subdirectories named `numpy` and `scipy`.  It would be a very good idea to read the installation instructions available at the Scipy site before you perform the following greatly simplified instructions.  There are additional packages that can be installed to enhance both the performance and functionality of **numpy** and **scipy**, and it is a very good idea to do so.  But we will not give those instructions here, again to avoid getting lost too far down the branching prerequisite trail.  That being said, here are the quickie installation instructions:

```
cd numpy
python setup.py build
su
python setup.py install
exit
cd ../scipy
python setup.py build
su
python setup.py install
exit
```

### matplotlib and basemap ###

These are graphics packages built on top of **numpy** and **scipy**, with the former providing various 1-D to 3-D graphics capabilities, and the latter adding geographical capabilities. See the **matplotlib** home page at:

http://matplotlib.sourceforge.net/

for further edification, and download them from Sourceforge:

http://sourceforge.net/project/showfiles.php?group_id=80706

Once you have the latest versions, at this writing `matplotlib-0.98.0.tar.gz` and `basemap-0.99.tar.gz`, you can install them via the following commands.  Once again, it is advisable to read the installation instructions available at the site to see if you want to go beyond the basic installation procedure to provide additional functionality.

```
tar xzvf matplotlib-0.98.0.tar.gz
cd matplotlib-0.98.0
python setup.py build
su
python setup.py install
exit
cd ..
tar xzvf basemap-0.99.tar.gz
cd basemap-0.99
python setup.py build
su
python setup.py install
exit
```


## Obtaining and Installing pyroms ##

The **pyroms** source code is obtained using the Subversion networked versioning system via the command:

```
svn checkout http://pyroms.googlecode.com/svn/trunk/ pyroms-read-only
```

which will download the source code into the subdirectory `pyroms-read-only`.  You can change the directory name in the `svn` command to just `pyroms` or any other arbitrary name you desire.

Once you have downloaded the code, the following commands will compile and install **pyroms** into your local Python library hierarchy.

```
cd pyroms-read-only
python setup.py build
su
python setup.py install
exit
```

You can now test if it has been properly installed by invoking the Python command-line interpreter:

```
python
[...]
>>> import pyroms
```

If you get no error messages when you enter `import pyroms` from within the interpreter, then you have successfully installed **pyroms**.