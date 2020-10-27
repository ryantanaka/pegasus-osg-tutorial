#!/usr/bin/env python3
import sys
import logging as log
from pathlib import Path

from Pegasus.api import *

log.basicConfig(level=log.DEBUG)

# --- Transformation Catalog ---------------------------------------------------
hello_world = Transformation(
                name="hello_world", 
                site="local", 
                pfn=Path(".").resolve() / "hello_world.sh", 
                arch=Arch.X86_64,
                os_type=OS.LINUX,
                is_stageable=True
            )

tc = TransformationCatalog().add_transformations(hello_world)

# --- Workflow -----------------------------------------------------------------
job = Job(hello_world)
job.add_outputs(File("output_file.txt"))

wf = Workflow("osg-workflow")
wf.add_jobs(job)

try:
    wf.plan(submit=True)\
    .wait()\
    .analyze()\
    .statistics()
except PegasusClientError as e:
    print(e.output)
    sys.exit(1)

# --- Resulting Output File ----------------------------------------------------
output_file = Path(".") / "wf-output/output_file.txt"
if output_file.exists():
    print("*"*80)
    print("* Workflow Output")
    print("*"*80)
    with output_file.open("r") as f:
        print(f.read())
