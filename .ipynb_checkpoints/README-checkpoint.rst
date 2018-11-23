Starting environment
--------------------

Start jupyter lab

    python -m jupyter lab

Execute cell: shift + Enter


Python 2 to 3
-------------

* Dictionaries preserve order from 3.7 version.

* Install module future to migrate python code.

    futurize py2sample.py

  Show the changes required on py2sample.py file.
  

PEP8
----
conda install pylint
pylint --generate-rcfile > .pylintrc
conda install -c conda-forge black
(the repos can be configured in ~/.condarc file)

Memory profile
--------------
conda search pympler
conda install pympler
conda install matplotlib
conda install memory_profiler