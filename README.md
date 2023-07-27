# Risk-Analysis-Language-Model

## Installing:
To install run the following command:
```
!pip install "git+https://github.com/sb-lucas/Risk-Matrix.git"
```
## Opening:
Import the package and call the constructor.
```
from risk_analysis import Matrix
generator = Matrix()
```
## Basic Functions:
You can call 'getImpact()' and 'getFrequency()' methods passing a string as an argument in order to get its analysis.
```
generator.getImpact("Example String")
generator.getFrequency("Example String")
```
## Example with simple data:
```
reports = ["Example1",
           "Example2",
           "Example3",
           "Example4",
           "Example5"]

impacts = []
frequencies = []

for report in reports:
  impacts.append(generator.getImpact(report))
  frequencies.append(generator.getFrequency(report))
```
