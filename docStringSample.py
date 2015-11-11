import numpy as np

class something: 

    def firstFunction(self):
        """
        This some frigging function
        """
    def secondFunction(self):
        """
        This some second frigging function
        
        
        - **parameters**, **types**, **return** and **return types**::
    
              :param arg1: description
              :param arg2: description
              :type arg1: type description
              :type arg1: type description
              :return: return description
              :rtype: the return type description
    
        - and to provide sections such as **Example** using the double commas syntax::
    
              :Example:
    
              followed by a blank line !
    
          which appears as follow:
    
          :Example:
    
          followed by a blank line
    
        - Finally special sections such as **See Also**, **Warnings**, **Notes**
          use the sphinx syntax (*paragraph directives*)::
    
              .. seealso:: blabla
              .. warnings also:: blabla
              .. note:: blabla
              .. todo:: blabla
    
        .. note::
            There are many other Info fields but they may be redundant:
                * param, parameter, arg, argument, key, keyword: Description of a
                  parameter.
                * type: Type of a parameter.
                * raises, raise, except, exception: That (and when) a specific
                  exception is raised.
                * var, ivar, cvar: Description of a variable.
                * returns, return: Description of the return value.
                * rtype: Return type.
    
        .. note::
            There are many other directives such as versionadded, versionchanged,
            rubric, centered, ... See the sphinx documentation for more details.
    
        Here below is the results of the :func:`function1` docstring.
        """
    
