from packaging import version
import openai 
import os

OPENAI_API_KEY = os.environ("OPENAI_API_KEY")



required_version = version.parse("1.1.1")
current_version = version.parse(openai.__version__)

print(current_version)

if current_version < required_version:
    raise ValueError("Incompatible")
else:
    print("compatible")



