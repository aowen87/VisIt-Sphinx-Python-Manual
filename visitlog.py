# Visit 3.0.0b log file
ScriptVersion = "3.0.0b"
if ScriptVersion != Version():
    print "This script is for VisIt %s. It may not work with version %s" % (ScriptVersion, Version())
visit.ShowAllWindows()
