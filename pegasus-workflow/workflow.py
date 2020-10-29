#!/usr/bin/env python3
import sys
import logging as log
from pathlib import Path

from Pegasus.api import *

log.basicConfig(level=log.DEBUG)

# --- Remove Output File From Previous Run ------------------------------------
output_file = Path(".") / "wf-output/output_file.txt"
try:
    output_file.unlink()
except FileNotFoundError:
    pass

# --- Transformation Catalog ---------------------------------------------------
hello_world = Transformation(
                name="hello_world", 
                site="local", 
                pfn=Path(".").resolve() / "hello_world.sh", 
                arch=Arch.X86_64,
                os_type=OS.LINUX,
                is_stageable=True
            )

# Require that this job is to be run in a specified container. (quotes are needed for image name)
# Omit UConn as that site was giving us problems.
#hello_world.add_condor_profile(requirements='GLIDEIN_Site =!= "UConn" && HAS_SINGULARITY == True')
#hello_world.add_profiles(Namespace.CONDOR, key="+SingularityImage", value='"/cvmfs/singularity.opensciencegrid.org/opensciencegrid/tensorflow-gpu:2.3-cuda-10.1"')

# Require that this job needs a GPU.
#hello_world.add_pegasus_profile(gpus=1)

tc = TransformationCatalog().add_transformations(hello_world)

# --- Workflow -----------------------------------------------------------------
job = Job(hello_world)
job.add_outputs(File("output_file.txt"))

wf = Workflow("osg-workflow")
wf.add_jobs(job)
wf.add_transformation_catalog(tc)

try:
    wf.plan(submit=True)\
    .wait()\
    .analyze()\
    .statistics()
except PegasusClientError as e:
    print(e.output)
    sys.exit(1)

# --- Resulting Output File ----------------------------------------------------
if output_file.exists():
    print("\x1b[1;34m" + ("*"*80) + ("\n* Workflow Output") + (62 * " ") + "*\n" + ("*"*80) + "\x1b[0m")
    with output_file.open("r") as f:
        print(f.read())
else:
    print("Cannot find {}, workflow must have failed...".format(output_file))
