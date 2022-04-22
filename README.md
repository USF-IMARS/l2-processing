# l2-processing
Python notebooks for doing the L2 processing, create means, do mapping.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/USF-IMARS/l2-processing/main)


# setup
## OCSSW
### path & env setup
Before being able to use OCSSW as required by some of the methods here, your environment needs to be configured. This includes ensuring that the right files are accessible in your $PATH. This can be done automatically every time you log in by editing some special files in your home directory.

**for those using `bash`**:
add the following lines to the end of the `.bashrc` file in your home directory
```
export OCSSWROOT=/opt/ocssw/--git-base
source $OCSSWROOT/OCSSW_bash.env
```

**for those using `tcsh`**:
OCSSW does not provide a script for setting up with `tcsh`, so you must do the setup for `bash` above and switch to using bash before working.
To start a bash prompt from a tcsh prompt enter `/bin/bash`, or simply `bash`.
