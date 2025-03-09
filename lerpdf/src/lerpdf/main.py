#!/usr/bin/env python
from lerpdf.crew import LerpdfCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {"pasta_pdf": "src/lerpdf/Exemplos"}
    LerpdfCrew().crew().kickoff(inputs=inputs)