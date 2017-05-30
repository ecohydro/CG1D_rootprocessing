.. tutorial:

****************
Getting Started
****************

**I. SETTING UP**

First, download the 'Root_Processing' library, and place it in a directory of your choice.  The library should have the subdirectories 'Analyses', 'Misc', 'Notebook_Code', and 'test'.  

We will then create a fake dataset in order to run and test the analyses.  In your window, type the following:

	import sys
	wd = '/Users/Root_Processing'  #Specify where your directory is here.
	sys.path.append(wd+'/Analyses')
	sys.path.append(wd+'/Misc')
	from sampledata import sampledata
	sampledata(wd)

This will create a 'Sample_Data' subdirectory in your library, which will contain a 'raw' subdirecotyr with a set of 10 images, as well as a dark field and open beam image.

You will also notice a 'user_config' file created in the 'Root_Processing' library - this contains all the necessary parameters for each of the analyses conducted by this library.  Please check the documentation within each module for details.  

Also, be sure to *only change the entries following the colon for each parameter!*  Do not add any extra lines or modify the headings for each section.  

**II. RUNNING ANALYSES WITH 'RP_RUN'**

From here, we will use the 'RP_run' module, which will act as the top-level program for running any analyses of interest:

	from RP_run import RP_run

We will then specify the analyses of interest (you can choose from 'RP_stitch', 'RP_crop', 'RP_wc', 'RP_mask', 'RP_imagefilter', 'RP_distmap', 'RP_radwc', and 'RP_rootimage').  You can run these in any order, but make sure that you have the necessary images and analyses completed first (e.g. 'RP_radwc' requires the output from 'RP_wc', 'RP_imagefilter', and 'RP_distmap' in order to run):

	analysis_list = ['RP_stitch', 'RP_crop', 'RP_wc', 'RP_mask', 'RP_imagefilter', 'RP_distmap', 'RP_radwc', 'RP_rootimage']

Once this is complete, then simply run the module:
	
	RP_run(wd, analysis_list)


