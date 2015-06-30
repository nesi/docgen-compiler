Category: Scientific Software
Section: Examples
<!-- The above lines, specifying the category and section, must be present and
always comprising the first and second lines of the article respectively. -->

# Description

This block of text is where a brief description of the software and its
purposes might go, perhaps obtained from "module whatis" with manual revision
where desirable.

[Click here](http://www.example.com) to go to the home page.

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
	
	#SBATCH -A uoa99999
	#SBATCH 
	
	module load Foo/1.0.1-intel-2015.02
	srun bar

## Example script for the Fitzroy cluster

## Example script for the BlueGene/P cluster

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
