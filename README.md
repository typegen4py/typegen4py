### TYPEGEN4PY  statically infering return types for library functions

## Dependency:
   Python 3.7+

## Data Preparation
`unzip top-10.zip`

## To Test Benchmark
`python run.py bench 2` where 2 is the case number. You can also specify other case numbers

## To Test Groundtruth
`python run.py eval `


## To use this tool
`python run.py gen  lib-data-dir ` where lib-data-dir is the location of your uncompressed wheel file folder. Please note the input of typegen4py is supposed to be uncompressed wheel file.

## To obtain RQ2 results
 After downloading top-10 library sources, you can run our tool with gen mode. Specifying the root folder of library source as the input for gen mode, our tool will produce the results in the paper.

## Miscellaneous
* The `pre-study-raw-data.csv` file contain the statistical results for each of libraries in our preliminary study.
* The `cfg` folder is the implementation of backward anaysis with control flow graph. 
* Rule-based mining is included in the `run.py`. 
* The `ast_factory` are all manuputions of abstract files.

