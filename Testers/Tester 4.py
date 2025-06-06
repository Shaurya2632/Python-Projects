import io
import sys
from contextlib import redirect_stdout

f = io.StringIO()
with redirect_stdout(f):
	print("Hello, world!")
	print("This will be captured.")

output = f.getvalue()  # output is a string containing all printed text
print(output)
