Group or Cluster Detection Algorithms
=====================================

-  This topic has become more and more important for the study of
   galaxy-halo connection.

Based on clustering of galaxies
-------------------------------

-  `sfof - Friends-of-Friends Galaxy Cluster Detection
   Algorithm <https://github.com/sfarrens/sfof>`__

   -  By `Samuel Farrens <https://sfarrens.github.io/>`__. SFoF is a
      friends-of-friends galaxy cluster detection algorithm that
      operates in either spectroscopic or photometric redshift space.
      The linking parameters, both transverse and along the
      line-of-sight, change as a function of redshift to account for
      selection effects.

Using the velocity (redshift information)
-----------------------------------------

-  [**FOG** - identifies locations of clusters by looking for the
   Finger-of-God effect]

   -  Also in Abdullah et al. 2018 (AWK18) introduced a new technique
      (GalWeight) to assign cluster membership.
   -  A catalog of 1870 clusters at 0.01 < z < 0.2 from SDSS DR13
      (**GalWCat19**) can be found
      `here <https://mohamed-elhashash-94.webself.net/galwcat>`__

Based on red-sequence of the cluster members
--------------------------------------------

redMaPPer: red-sequence Matched-filter Probabilistic Percolation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `redMaPPer - The Red-sequence Cluster
   Finder <https://github.com/erykoff/redmapper>`__

   -  By `Eli Rykoff <https://github.com/erykoff>`__. This is the
      open-source, python version of the red-sequence matched-filter
      Probabilistic Percolation (redMaPPer) cluster finder, originally
      described in Rykoff et al. (2014), with updates described in Rozo
      et al. (2015) and Rykoff et al. (2016).
   -  One of the most commonly used algorithm in recent years.

Papers:
^^^^^^^

-  `redMaPPer. I. Algorithm and SDSS DR8
   Catalog <https://ui.adsabs.harvard.edu/abs/2014ApJ...785..104R/abstract>`__
-  `redMaPPer II: X-Ray and SZ Performance Benchmarks for the SDSS
   Catalog <https://ui.adsabs.harvard.edu/abs/2014ApJ...783...80R/abstract>`__
-  `redMaPPer - III. A detailed comparison of the Planck 2013 and SDSS
   DR8 redMaPPer cluster
   catalogues <https://ui.adsabs.harvard.edu/abs/2015MNRAS.450..592R/abstract>`__
-  `redMaPPer - IV. Photometric membership identification of red cluster
   galaxies with 1 per cent
   precision <https://ui.adsabs.harvard.edu/abs/2015MNRAS.453...38R/abstract>`__

Calibration:
^^^^^^^^^^^^

Issues:
^^^^^^^

CAMIRA
~~~~~~

Test cluster finder in mock catalog
-----------------------------------

-  `pycymatch <https://github.com/sfarrens/pycymatch>`__

   -  **Pycymatch** is a cylindrical matching code for identifying
      matches between a catalogue of simulated dark matter haloes
      populated with galaxies and the results of a cluster detection
      algorithm run on said catalogue.
