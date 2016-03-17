Category: Available Software
Section: Stubs
Title: <<PACKAGENAME>>
<!-- The above lines, specifying the category, section and title, must be
present and always comprising the first three lines of the article. -->

[TOC]

# Description
<!--This is a placeholder for a description. Do not edit.-->

The <<PACKAGENAME>> home page is at [http://www.example.com](http://www.example.com).

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

```bash
#!/bin/bash

#SBATCH --job-name      <<PACKAGENAME>>_job
#SBATCH --account       nesi99999
#SBATCH --time          01:00:00
#SBATCH --mem-per-cpu   4G
#SBATCH --output        <<PACKAGENAME>>_job.%j.out # Include the job ID in the names
#SBATCH --error         <<PACKAGENAME>>_job.%j.err # of the output and error files

module load <<PACKAGENAME>>/1.2.3

foo -bar MyInput.dat
```

## Example script for the Fitzroy cluster

```bash
#!/bin/bash

#@ job_name         = <<PACKAGENAME>>_job
#@ account_no       = nesi99999
#@ class            = General
#@ wall_clock_limit = 01:00:00
#@ initialdir       = /hpcf/working/nesi99999/<<PACKAGENAME>>_job
#@ output           = $(job_name).$(jobid).out
#@ error            = $(job_name).$(jobid).err
#@ queue

# LoadLeveler has an annoying habit of transferring parts of the user's
# environment as it existed at the time of submission to the job. Clear any
# loaded modules.
module purge

module load <<PACKAGENAME>>/1.2.3

foo -bar MyInput.dat
```

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
