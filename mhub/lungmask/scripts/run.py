"""
-------------------------------------------------
MedicalHub - run the LungMask pipeline locally
-------------------------------------------------

-------------------------------------------------
Author: Dennis Bontempi
Email:  dbontempi@bwh.harvard.edu
-------------------------------------------------
"""

import sys, os
sys.path.append('.')

from mhub.mhubio.Config import Config, DataType, FileType, CT, SEG
from mhub.mhubio.modules.importer.UnsortedDicomImporter import UnsortedInstanceImporter
from mhub.mhubio.modules.importer.DataSorter import DataSorter
from mhub.mhubio.modules.convert.NiftiConverter import NiftiConverter
from mhub.mhubio.modules.convert.DsegConverter import DsegConverter
from mhub.mhubio.modules.organizer.DataOrganizer import DataOrganizer
from mhub.lungmask.utils.LungMaskRunner import LungMaskRunner

# clean-up
import shutil
shutil.rmtree("/app/data/sorted", ignore_errors=True)
shutil.rmtree("/app/data/nifti", ignore_errors=True)
shutil.rmtree("/app/tmp", ignore_errors=True)
shutil.rmtree("/app/data/output_data", ignore_errors=True)

# config
config = Config('/app/mhub/lungmask/config/config.yml')
config.verbose = True  # TODO: define levels of verbosity and integrate consistently. 

# import
UnsortedInstanceImporter(config).execute()

# sort
DataSorter(config).execute()

# convert (ct:dicom -> ct:nifti)
NiftiConverter(config).execute()

# execute model (ct:nifti -> seg:nifti)
LungMaskRunner(config).execute()

# convert (seg:nifti -> seg:dicomseg)
DsegConverter(config).execute()

# organize data into output folder
organizer = DataOrganizer(config, set_file_permissions=sys.platform.startswith('linux'))
organizer.setTarget(DataType(FileType.NIFTI, CT), "/app/data/output_data/[i:SeriesID]/[path]")
organizer.setTarget(DataType(FileType.DICOMSEG, SEG), "/app/data/output_data/[i:SeriesID]/lungmask.seg.dcm")
organizer.execute()