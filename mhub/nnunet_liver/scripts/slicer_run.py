"""
-------------------------------------------------
MedicalHub - run the PP pipeline locally
-------------------------------------------------

-------------------------------------------------
Author: Leonard Nürnberg
Email:  leonard.nuernberg@maastrichtuniversity.nl
-------------------------------------------------
"""

import sys, os
sys.path.append('.')

from mhub.mhubio.Config import Config, DataType, FileType, SEG
from mhub.mhubio.modules.importer.NrrdImporter import NrrdImporter
from mhub.mhubio.modules.convert.NiftiConverter import NiftiConverter
from mhub.mhubio.modules.runner.NNUnetRunner import NNUnetRunner
from mhub.mhubio.modules.organizer.DataOrganizer import DataOrganizer

# config
config = Config('/app/mhub/nnunet_liver/config/config.yml')
config.verbose = True  

# import nrrd data provided by slicer
NrrdImporter(config).execute()

# convert (ct:dicom -> ct:nifti)
NiftiConverter(config).execute()

# execute model (nnunet)
NNUnetRunner(config).execute()

# organize data into output folder available to slicer
organizer = DataOrganizer(config)
organizer.setTarget(DataType(FileType.NIFTI, SEG), "/app/data/output_data/liver.nii.gz")
organizer.execute()
