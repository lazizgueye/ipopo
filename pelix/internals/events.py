#!/usr/bin/env python
# -- Content-Encoding: UTF-8 --
"""
Event beans for Pelix.

:author: Thomas Calmant
:copyright: Copyright 2013, isandlaTech
:license: GPLv3
:version: 0.5.4
:status: Alpha

..

    This file is part of iPOPO.

    iPOPO is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    iPOPO is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with iPOPO. If not, see <http://www.gnu.org/licenses/>.
"""

# Module version
__version_info__ = (0, 5, 4)
__version__ = ".".join(str(x) for x in __version_info__)

# Documentation strings format
__docformat__ = "restructuredtext en"

# ------------------------------------------------------------------------------

# Pelix utility modules
from pelix.utilities import Deprecated

# ------------------------------------------------------------------------------

class BundleEvent(object):
    """
    Represents a bundle event
    """

    INSTALLED = 1
    """The bundle has been installed."""

    STARTED = 2
    """The bundle has been started."""

    STARTING = 128
    """The bundle is about to be activated."""

    STOPPED = 4
    """
    The bundle has been stopped. All of its services have been unregistered.
    """

    STOPPING = 256
    """The bundle is about to deactivated."""

    STOPPING_PRECLEAN = 512
    """
    The bundle has been deactivated, but some of its services may still remain.
    """

    UNINSTALLED = 16
    """The bundle has been uninstalled."""

    UPDATED = 8
    """The bundle has been updated. (called after STARTED) """

    UPDATE_BEGIN = 32
    """ The bundle will be updated (called before STOPPING) """

    UPDATE_FAILED = 64
    """ The bundle update has failed. The bundle might be in RESOLVED state """


    def __init__(self, kind, bundle):
        """
        Sets up the event
        """
        self.__kind = kind
        self.__bundle = bundle


    def __str__(self):
        """
        String representation
        """
        return "BundleEvent({0}, {1})".format(self.__kind, self.__bundle)


    def get_bundle(self):
        """
        Retrieves the modified bundle
        """
        return self.__bundle


    def get_kind(self):
        """
        Retrieves the kind of event
        """
        return self.__kind

# ------------------------------------------------------------------------------

class ServiceEvent(object):
    """
    Represents a service event
    """

    REGISTERED = 1
    """ This service has been registered """

    MODIFIED = 2
    """ The properties of a registered service have been modified """

    UNREGISTERING = 4
    """ This service is in the process of being unregistered """

    MODIFIED_ENDMATCH = 8
    """
    The properties of a registered service have been modified and the new
    properties no longer match the listener's filter
    """

    def __init__(self, kind, reference, previous_properties=None):
        """
        Sets up the event

        :param kind: Kind of event
        :param reference: Reference to the modified service
        :param previous_properties: Previous service properties (for MODIFIED
                                    and MODIFIED_ENDMATCH events)
        """
        self.__kind = kind
        self.__reference = reference

        if previous_properties is not None \
        and not isinstance(previous_properties, dict):
            # Accept None or dict() only
            previous_properties = {}

        self.__previous_properties = previous_properties


    def __str__(self):
        """
        String representation
        """
        return "ServiceEvent({0}, {1})".format(self.__kind, self.__reference)


    def get_previous_properties(self):
        """
        Returns the previous values of the service properties, meaningless if
        the the event is not MODIFIED nor MODIFIED_ENDMATCH.
        
        :return: The previous properties of the service
        """
        return self.__previous_properties


    def get_service_reference(self):
        """
        Returns the reference to the service associated to this event
        
        :return: A ServiceReference object
        """
        return self.__reference


    def get_kind(self):
        """
        Returns the kind of service event (see the constants)
        
        :return: the kind of service event
        """
        return self.__kind


    @Deprecated("ServiceEvent: get_type() must be replaced by get_kind()")
    def get_type(self):
        """
        **DEPRECATED:** Use get_kind() instead
        
        Retrieves the kind of service event.
        """
        return self.__kind
