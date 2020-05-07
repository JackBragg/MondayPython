    #!  /usr/bin/env python2
    #

    from netCDF4 import Dataset
    import matplotlib.pyplot as plt
    from mpl_toolkits.basemap import Basemap
    import numpy as np
    import os
    import glob
    import calendar

    #*** Setup Global Variables
    nlon = 1440
    nlat = 720

    startY = 1982
    endY = 2015

    #*** Setup Data File Directory Name
    dirname = './'

    #*** Calculate how many days of data files
    nt = 0
    for i in range(startY,endY+1):
       if calendar.isleap(i):
         nt = nt + 366
       else:
         nt = nt + 365

    sst_all=np.empty((nt,nlat/2,nlon/2))

    # Pre-define latitude and longitude grid
    lats = [-89.875+0.5*x for x in range(0, nlat/2)]
    lons = [-179.875+0.5*x for x in range(0, nlon/2)]

    # Read SST using the netCDF4 module.
    idx = 0
    for i in range(startY, endY+1):
      for j in range(1, 366):
         for filename in glob.glob(dirname+str(i)+'/'+"{0:0>3}".format(j)+'/*.nc'):
           ncin = Dataset(filename, 'r')
           sst = ncin.variables['analysed_sst'][:]
           sst_all[idx,:,:] = sst[0,0:nlat:2,0:nlon:2]
           ncin.close()

    # Linear trend calculation
    sst=np.empty((idx))
    x = range(idx)
    sst_rate=np.empty((nlat/2,nlon/2))

    for i in range(nlon/2):
      for j in range(nlat/2):
        sst[:] = sst_all[0:idx,j,i]
        z = np.polyfit(x, sst, 1)
        sst_rate[j,i] = z[0]*3650.0

    #*** Plot the result
    plt.figure()

    m = Basemap(projection='cyl', llcrnrlon=min(lons), llcrnrlat=min(lats),
            urcrnrlon=max(lons), urcrnrlat=max(lats))
    x, y = m(*np.meshgrid(lons, lats))
    clevs = np.linspace(-0.5, 0.5, 21)
    cs=m.contourf(x, y, sst_rate.squeeze(), clevs, cmap=plt.cm.RdBu_r)
    m.drawcoastlines()
    m.fillcontinents(color='#000000',lake_color='#99ffff')

    cb = plt.colorbar(cs, orientation='horizontal')
    cb.set_label('SST Changing Rate (deg/decade)', fontsize=12)
    plt.title('SST Changing Rate (degC/decade)', fontsize=16)

    plt.show()
