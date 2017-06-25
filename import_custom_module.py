
# pylint: skip-file
# Import a custom module

import printModule

printModule.handlePrintName( 'Swapnil' )


# Or

from printModule import *

handlePrintName( 'Swapnil' )


# Or import package
import PhoneFunctions

PhoneFunctions.Imei()
PhoneFunctions.PhoneNumber()