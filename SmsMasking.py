#!/usr/bin/env python
# -*- coding: ASCII -*-
import urllib2
import urllib

"""SMSMasking Wrapper v1.0 for smsmasking API class

   url:
   http://smsmasking.ca

"""
__author__ = "Andrey Ferriyan"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Andrey Ferriyan"
__email__ = "andrey.silversburg@gmail.com"
__status__ = "Development"


class SmsMaskingAPI(object):
    """
            The SmsMasking Class
    """

    def __init__(self, sender, number, message):
        """Initialization of class."""
        self.API = 'http://smsmasking.ca/api.html'
        self.sender = sender
        self.number = number
        self.message = message

    def send(self):
        """send the message."""
        data = urllib.urlencode({'sender': self.sender, 'number': self.number, 'message': self.message})
        u = urllib2.urlopen(self.API, data)
        for line in u.readline():
			print line
