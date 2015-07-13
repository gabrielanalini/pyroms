**pyroms** is a suite of tools for working with the Regional Ocean Modeling System.  A grid class allows creation, reading and writing of model grids.  Other tools are included to facilitate analysis and visualization of model output.

The modules include:

**boundaryclick** - Interactive boundary generation for use with Gridgen, a MATLAB-based  orthogonal grid generator.

**Dataset** - A wrapper for netCDF4.Dataset and MFnetCDF4.Dataset

**depths** - Calculates regular depths from S-coordinate depths and parameters.

**focus** - Creates focus elements for use with Gridgen.

**greatcircle** - Calculates great circle distances.

**grid** - Creates a ROMS input grid.

**gshhs** - Reads Global Self-consistant Hierarchical High-resolution Shorelines (GSHHS) binary files.

**ocean** - Calculates density as a function of salinity, temperature, and pressure.  Also calculates O2 saturation concentrations for a given temperature and pressure at STP.

**ocean\_time** -

**polyclick** - Interactive polygon generation.

**polygeom** - Calculates if a point lies within a given polygon.

**pupynere** - a PUre PYthon NEtcdf REader

**roms\_tools** - Tools for working with ROMS model input and output including:

  * rot2d - Rotates vectors by an angle.
  * nanmask - Obtains the land/ocean mask.
  * zatr - Finds z at rho points.
  * zatw - Finds z at w points.
  * scoordr - Finds z at rho points.
  * scoordw - Finds z at w points.
  * isoslice - Calculates a horizontal or vertical slice of a property.
  * shrink - Shrinks an array to fit a specified shape.
  * zslice -
  * iso\_integrate -
  * surface -
  * transect - Interpolates a property on a horizontal grid to a transect.
  * N2 - Calculates the stratification frequency given rho and z.
  * arg\_nearest - Returns the indices of the N-dim arrays closes to a given N-dim vector.
  * nc\_gls\_dissipation - Calculates the dissipation based on TKE, GLS and the GLS scheme parameters.
  * nc\_N2 - Calculates the buoyancy frequency squared.
  * nc\_curl -
  * nc\_div -
  * nc\_pstrain -

**step3d\_t** -

**velocity** - Calculates vector velocities from u and v components.

