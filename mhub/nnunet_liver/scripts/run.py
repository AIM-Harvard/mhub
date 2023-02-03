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

from mhub.mhubio.Config import Config, DataType, FileType, CT, SEG
from mhub.mhubio.modules.importer.UnsortedDicomImporter import UnsortedInstanceImporter
from mhub.mhubio.modules.importer.DataSorter import DataSorter
from mhub.mhubio.modules.convert.NiftiConverter import NiftiConverter
from mhub.mhubio.modules.runner.NNUnetRunner import NNUnetRunner
from mhub.mhubio.modules.organizer.DataOrganizer import DataOrganizer

# clean-up
import shutil
shutil.rmtree("/app/data/sorted", ignore_errors=True)
shutil.rmtree("/app/data/nifti", ignore_errors=True)
shutil.rmtree("/app/tmp", ignore_errors=True)
shutil.rmtree("/app/data/output_data", ignore_errors=True)

# config
config = Config('/app/mhub/platipy/config/config.yml')
config.verbose = True  # TODO: define levels of verbosity and integrate consistently. 
config.debug = True

# import
UnsortedInstanceImporter(config).execute()

# $(pwd)/mhub:/app/mhub

# sort
DataSorter(config).execute()

# convert (ct:dicom -> ct:nifti)
NiftiConverter(config).execute()

# execute model (nnunet)
runner = NNUnetRunner(config)
runner.input_type = DataType(FileType.NIFTI, CT)
runner.nnunet_model = '3d_lowres'
runner.nnunet_task = 'Task003_Liver'
runner.execute()

# organize data into output folder
organizer = DataOrganizer(config, set_file_permissions=sys.platform.startswith('linux'))
organizer.setTarget(DataType(FileType.NIFTI, CT), "/app/data/output_data/image.nii.gz")
organizer.setTarget(DataType(FileType.NIFTI, SEG), "/app/data/output_data/liver.nii.gz")
organizer.setTarget(DataType(FileType.DICOMSEG, SEG), "/app/data/output_data/liver.seg.dcm")
organizer.execute()
