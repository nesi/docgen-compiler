Category: Available Software
Section: Stubs
<!-- The above lines, specifying the category and section, must be present and
always comprising the first and second lines of the article respectively. -->

# Description
<!--This is a placeholder for a description. Do not edit.-->

[Click here](http://www.example.com) to visit the home page.

# Available modules
<!--This is a placeholder for an automatically generated table. Do not edit.-->

# Licensing requirements

This paragraph is a place for us to describe the licensing conditions under
which this software package is made available to NeSI users. This could be
anything from a brief statement that the software is released under the GPL to
an elaborate mapping of versions to institutions, departments and research
groups. If the latter, the paragraph should end with a note like the following
to researchers: If you have any questions regarding your eligibility to access
this software package or any particular version of it, please contact [our
support desk](mailto:support@nesi.org.nz).

# Example scripts

## Example script for the Pan cluster

	#!/bin/bash
	
	#SBATCH     --job-name=MyFooJob
	#SBATCH      --account=nesi99999
	#SBATCH         --time=01:00:00
	#SBATCH --cpus-per-task=1
	#SBATCH   --mem-per-cpu=4096
	#SBATCH       --workdir=/projects/nesi99999/MyFooJob
	#SBATCH        --output=MyFooJob.out
	#SBATCH         --error=MyFooJob.err
	#SBATCH     --mail-type=ALL
	#SBATCH     --mail-user=j.bloggs@example.com
	#SBATCH     --mail-user=jblo123@example.ac.nz
	
	module load Foo/1.2.3
	
	foo -bar MyInput.dat

## Example script for the Fitzroy cluster

	#!/bin/bash
	
	#@ job_name = MyFooJob
	#@ account_no = nesi99999
	#@ class = General
	#@ wall_clock_limit = 01:00:00
	#@ job_type = serial
	#@ initialdir = /hpcf/working/nesi99999/MyFooJob
	#@ output = $(job_name).out
	#@ error = $(job_name).err
	#@ notification = always
	#@ notify_user = j.bloggs@example.com
	#@ queue
	
	module load Foo/1.2.3
	
	foo -bar MyInput.dat

## Example script for the UC HPC Power7 cluster

	#!/bin/bash
	
	#@ job_name = MyFooJob
	#@ account_no = nesi99999
	#@ group = UC
	#@ class = p7linux
	#@ wall_clock_limit = 01:00:00
	#@ initialdir = /hpc/scratch/nesi99999/MyFooJob
	#@ output = $(job_name).out
	#@ error = $(job_name).err
	#@ notification = always
	#@ notify_user = j.bloggs@example.com
	#@ queue
	
	module load Foo/1.2.3
	
	foo -bar MyInput.dat

# Further notes

**This section will not always be needed. Its purpose is to provide us with a
place to put special, advanced or supplementary information (for example, for R
or Python, which have many tips and tricks that we may wish to share with the
user community).**

Lorem ipsum dolor sit amet, consectetur adipiscing elit.  Donec a erat in mi
bibendum tempus eu nec odio. Proin facilisis nunc id ante feugiat, ac
sollicitudin leo pretium. Vivamus vestibulum magna et ante volutpat, semper
dignissim magna posuere. Sed at urna elit. Mauris rutrum, ante id malesuada
gravida, lorem mauris convallis lorem, ut venenatis massa est pulvinar massa.
Nullam rhoncus mi iaculis vulputate pellentesque. Curabitur augue felis,
venenatis eget enim non, maximus condimentum nisl. Curabitur justo quam,
sagittis malesuada bibendum sit amet, fermentum nec nulla. Ut varius ipsum ac
lacus porttitor, sed imperdiet nisi egestas. This text tests accented and other
special characters: Café naïve œsophagus
