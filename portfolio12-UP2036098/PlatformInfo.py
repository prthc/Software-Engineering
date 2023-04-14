import platform

# Info: https://docs.python.org/3/library/platform.html
print("=" * 80)
print("uname: ", platform.uname())
print("=" * 80)
print("platform: %s" % platform.platform())
print("=" * 80)
print("System: %s" % platform.system())
print("Node: %s" % platform.node())
print("Release: %s" % platform.release())
print("Version: %s" % platform.version())
print("Machine: %s" % platform.machine())
print("Processor: %s" % platform.processor())
print("=" * 80)
