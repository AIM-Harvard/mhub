"""
-------------------------------------------------
MedicalHub - Run Module for LungMask.
-------------------------------------------------

-------------------------------------------------
Author: Dennis Bontempi
Email:  dbontempi@bwh.harvard.edu
-------------------------------------------------
"""

from mhub.mhubio.Config import Instance, InstanceData, DataType, FileType, SEG
from mhub.mhubio.modules.runner.ModelRunner import ModelRunner

import os, subprocess

class LungMaskRunner(ModelRunner):
    def runModel(self, instance: Instance) -> None:
        
        # data
        inp_data = instance.getData(DataType(FileType.NIFTI))

        # define model output folder
        out_dir = self.config.data.requestTempDir(label="lm-model-out")
        out_file_lungs = os.path.join(out_dir, "1_lungs.nii.gz")
        out_file_lobes = os.path.join(out_dir, "2_lunglobes.nii.gz")

        # bash command for the lung segmentation 
        bash_command  = ["lungmask"]
        bash_command += [inp_data.abspath]      # /path/to/input_file
        bash_command += [out_file_lungs]        # /path/to/ct.nii.gz
        bash_command += ["--modelname", "R231"] # specify lung seg model

        self.v("Running the lung segmentation.")

        # TODO: remove 
        self.v(">> run lungmask (R231): ", " ".join(bash_command))
        
        # run the lung segmentation model
        bash_return = subprocess.run(bash_command, check=True, text=True)


        # bash command for the lung lobes segmentation (fusion)
        bash_command  = ["lungmask"]
        bash_command += [inp_data.abspath]                  # /path/to/input_file
        bash_command += [out_file_lobes]                    # /path/to/ct.nii.gz
        bash_command += ["--modelname", "LTRCLobes_R231"]   # specify lung lobes seg model

        self.v("Running the lung lobes segmentation (with model fusion).")

        # TODO: remove 
        self.v(">> run lungmask (LTRCLobes_R231): ", " ".join(bash_command))
        
        # run the lung lobes segmentation model
        bash_return = subprocess.run(bash_command, check=True, text=True)


        # add output data to the instance
        for out_file in os.listdir(out_dir):

            # ignore non nifti files
            if out_file[-7:] != ".nii.gz":
                self.v(f"IGNORE OUTPUT FILE {out_file}")
                continue

            # meta
            meta = {
                "model": "LungMask",
                "roi": out_file[:-7]            # TODO: standardize (as with the whole DataType usecase & filtering!)
            }

            # create output data
            seg_data_type = DataType(FileType.NIFTI, SEG + meta)           
            seg_path = os.path.join(out_dir, out_file)
            seg_data = InstanceData(seg_path, type=seg_data_type)
            seg_data.base = "" # required since path is external (will be fixed soon)
            instance.addData(seg_data)
