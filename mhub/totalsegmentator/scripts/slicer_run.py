"""
-------------------------------------------------
MedicalHub - Slicer run of the Totalsegmentator
  pipeline
-------------------------------------------------

-------------------------------------------------
Author: Dennis Bontempi
Email:  dbontempi@bwh.harvard.edu
-------------------------------------------------
"""

import sys, os
sys.path.append('.')

from mhub.mhubio.Config import Config, DataType, FileType, CT, SEG
from mhub.mhubio.modules.importer.NrrdImporter import NrrdImporter
from mhub.mhubio.modules.convert.NiftiConverter import NiftiConverter
from mhub.mhubio.modules.organizer.DataOrganizer import DataOrganizer
from mhub.totalsegmentator.utils.TotalSegmentatorRunner import TotalSegmentatorRunner

# config
config = Config('/app/mhub/totalsegmentator/config/slicer_config.yml')
config.verbose = True  # TODO: define levels of verbosity and integrate consistently. 

# load NRRD file (ct:nrrd)
NrrdImporter(config).execute()

# convert (ct:nrrd -> ct:nifti)
NiftiConverter(config).execute()

# execute model (ct:nifti -> seg:nifti)
TotalSegmentatorRunner(config).execute()

# organize data into output folder
organizer = DataOrganizer(config)
organizer.setTarget(DataType(FileType.NIFTI, SEG), "/app/data/output_data/[d:roi].nii.gz")
organizer.execute()