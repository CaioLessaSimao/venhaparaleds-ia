#!/usr/bin/env python
from lerpdf.crew import LerpdfCrew

def run():
    # Replace with your inputs, it will automatically interpolate any tasks and agents information
    inputs = {"pasta_pdf": "/home/caio/ledsDesafio/venhaparaleds-ia/lerpdf/src/lerpdf/Exemplos"}
    LerpdfCrew().crew().kickoff(inputs=inputs)