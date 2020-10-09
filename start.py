# Open Python3 and import package
from inkycal import Inkycal

# tell the Inkycal class where your settings file is
ink = Inkycal('.', render = False)
# render means rendering (showing) on the ePaper. Setting render = False will not show anything on the ePaper

# test if Inkycal can be run correctly, running this will show a bit of info for each module
ink.test()

# If there were no issues, you can run Inkycal nonstop:
ink.run()