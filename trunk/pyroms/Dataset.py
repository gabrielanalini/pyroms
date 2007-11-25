'''A wrapper for netCDF4.Dataset and MFnetCDF4.Dataset

possible uses include:

with an input of a string:
  nc = pyroms.Dataset(file) # returns netCDF4.Dataset object based on file
  nc = pyroms.MFDataset(file) # returns MFnetCDF4.Dataset object based on file (with wildcard chars)

with an input of a list of files:
  nc = pyroms.Dataset(files) # returns MFnetCDF4.Dataset object based on list of files
  nc = pyroms.MFDataset(files) # returns MFnetCDF4.Dataset object based on list of files

with an input of a netCDF4.Dataset or MFnetCDF4.Dataset object:
  nc = pyroms.Dataset(nc) # passes through netCDF4.Dataset or MFnetCDF4.Dataset object
  nc = pyroms.MFDataset(nc) # passes through MFnetCDF4.Dataset object based on file (with wildcard chars)
'''

try:
    import netCDF4
    try:
        import MFnetCDF4
    except:
        import MFnetCDF4_classic as MFnetCDF4
    
    def Dataset(ncfile):
        """Return an appropriate netcdf object:
                netCDF4 object given a file string
                MFnetCDF4 object given a list of files
            
            A netCDF4 or MFnetCDF4 object returns itself."""
        if isinstance(ncfile, str):
            return netCDF4.Dataset(ncfile, 'r')
        elif isinstance(ncfile, list) or isinstance(ncfile, tuple):
            return MFnetCDF4.Dataset(sorted(ncfile))
        elif hasattr(ncfile, 'variables'):  # accept any oject with a variables attribute
            assert isinstance(ncfile.variables, dict), \
                   'variables attribute must be a dictionary'
            return ncfile
        else:
            raise TypeError, 'type %s not supported' % type(ncfile)
    
    Dataset.__doc__ = __doc__

    def MFDataset(ncfile):
        """Return an MFnetCDF4 object given a string or list.  A string is expanded
           with wildcards using glob.  A netCDF4 or MFnetCDF4 object returns itself."""
        if isinstance(ncfile, str):
            return MFnetCDF4.Dataset(ncfile)
        elif isinstance(ncfile, list) or isinstance(ncfile, tuple):
            return MFnetCDF4.Dataset(sorted(ncfile))
        elif hasattr(ncfile, 'variables'):  # accept any oject with a variables attribute
            assert isinstance(ncfile.variables, dict), \
                   'variables attribute must be a dictionary'
            return ncfile
        else:
            raise TypeError, 'type %s not supported' % type(ncfile)
            return MFnetCDF4.Dataset(files)
    
    MFDataset.__doc__ = __doc__

except:
    import pupynere
    import warnings
    
    warnings.warn('netCDF4 not found -- using pupynere.')
    
    def Dataset(ncfile):
        if isinstance(ncfile, str):
            return pupynere.NetCDFFile(ncfile)
        elif isinstance(ncfile, pupynere.NetCDFFile):
            return ncfile
        else:
            raise TypeError, 'type %s not supported' % type(ncfile)
    
    Dataset.__doc__ = __doc__


if __name__ == '__main__':
    pass
    # need some better testing...
        