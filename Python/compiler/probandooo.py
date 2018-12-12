import re

reg_exp = "^({|}|\\(|\\)|;|-|!|~)"
result = re.match(reg_exp,"}");

print(result.group(0))
