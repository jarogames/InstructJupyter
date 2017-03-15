Experiences with packages
---------------------------

See the main README.md for the timeline of installations.

There are 3 methods known to me:
------------------------------

 * aptitude - many packages are installable by this - *e.g. python3-tk, python3-imaging-tk, python3-pil.imagetk*

 * pip3 install - useful modifiers pip3 install --upgrade,  pip3 install --user
   *e.g. staticmap* - first you need to `aptitude install python3-pip`

 * setup.py - once the package is unzipped and there is just setup.py file, 
    `python3 setup.py install`  *e.g. PhidgetsPython*



