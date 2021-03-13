import sys
import pkgutil
import pkg_resources
print(sys.builtin_module_names)
print()

print(dir(__builtins__))
print()

print(list(pkg_resources.working_set))
print()

help('modules')
