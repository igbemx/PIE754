# -*- coding: utf-8 -*-
#
# This file is part of the SoftiPIE754 project
#
#
#
# Distributed under the terms of the GPL license.
# See LICENSE.txt for more info.

""" PI E-754 Tango Device Server

PI E-754 Tango Device Server
"""

# PyTango imports
import tango
from tango import DebugIt
from tango.server import run
from tango.server import Device
from tango.server import attribute, command
from tango.server import device_property
from tango import AttrQuality, DispLevel, DevState
from tango import AttrWriteType, PipeWriteType
# Additional import
# PROTECTED REGION ID(SoftiPIE754.additionnal_import) ENABLED START #
# PROTECTED REGION END #    //  SoftiPIE754.additionnal_import

__all__ = ["SoftiPIE754", "main"]


class SoftiPIE754(Device):
    """
    PI E-754 Tango Device Server

    **Properties:**

    - Device Property
        ctrl_host
            - Host name or IP address of the controller.
            - Type:'DevString'
        offset
            - Type:'DevDouble'
        sign
            - Type:'DevShort'
        axis_name
            - Type:'DevString'
    """
    # PROTECTED REGION ID(SoftiPIE754.class_variable) ENABLED START #
    # PROTECTED REGION END #    //  SoftiPIE754.class_variable

    # -----------------
    # Device Properties
    # -----------------

    ctrl_host = device_property(
        dtype='DevString',
        default_value="172.16.205.6"
    )

    offset = device_property(
        dtype='DevDouble',
        default_value=50.0
    )

    sign = device_property(
        dtype='DevShort',
        default_value=1
    )

    axis_name = device_property(
        dtype='DevString',
        mandatory=True
    )

    # ----------
    # Attributes
    # ----------

    Position = attribute(
        dtype='DevDouble',
        access=AttrWriteType.READ_WRITE,
    )

    Velocity = attribute(
        dtype='DevDouble',
        access=AttrWriteType.READ_WRITE,
    )

    DialPosition = attribute(
        dtype='DevDouble',
        access=AttrWriteType.READ_WRITE,
        display_level=DispLevel.EXPERT,
    )

    OnTarget = attribute(
        dtype='DevBoolean',
    )

    ServoOn = attribute(
        dtype='DevBoolean',
        access=AttrWriteType.READ_WRITE,
        memorized=True,
        hw_memorized=True,
    )

    PosError = attribute(
        dtype='DevDouble',
    )

    PosTolerance = attribute(
        dtype='DevDouble',
        access=AttrWriteType.READ_WRITE,
        memorized=True,
        hw_memorized=True,
    )

    Acceleration = attribute(
        dtype='DevDouble',
        access=AttrWriteType.READ_WRITE,
    )

    # ---------------
    # General methods
    # ---------------

    def init_device(self):
        """Initialises the attributes and properties of the SoftiPIE754."""
        Device.init_device(self)
        # PROTECTED REGION ID(SoftiPIE754.init_device) ENABLED START #
        self.__position = 0.0
        self.__velocity = 0.0
        self.__dial_position = 0.0
        self.__on_target = False
        self.__servo_on = False
        self.__pos_error = 0.0
        self.__pos_tolerance = 0.0
        self.__acceleration = 0.0
        # PROTECTED REGION END #    //  SoftiPIE754.init_device

    def always_executed_hook(self):
        """Method always executed before any TANGO command is executed."""
        # PROTECTED REGION ID(SoftiPIE754.always_executed_hook) ENABLED START #
        # PROTECTED REGION END #    //  SoftiPIE754.always_executed_hook

    def delete_device(self):
        """Hook to delete resources allocated in init_device.

        This method allows for any memory or other resources allocated in the
        init_device method to be released.  This method is called by the device
        destructor and by the device Init command.
        """
        # PROTECTED REGION ID(SoftiPIE754.delete_device) ENABLED START #
        # PROTECTED REGION END #    //  SoftiPIE754.delete_device
    # ------------------
    # Attributes methods
    # ------------------

    def read_Position(self):
        # PROTECTED REGION ID(SoftiPIE754.Position_read) ENABLED START #
        """Return the Position attribute."""
        return self.__position
        # PROTECTED REGION END #    //  SoftiPIE754.Position_read

    def write_Position(self, value):
        # PROTECTED REGION ID(SoftiPIE754.Position_write) ENABLED START #
        """Set the Position attribute."""
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.Position_write

    def read_Velocity(self):
        # PROTECTED REGION ID(SoftiPIE754.Velocity_read) ENABLED START #
        """Return the Velocity attribute."""
        return self.__velocity
        # PROTECTED REGION END #    //  SoftiPIE754.Velocity_read

    def write_Velocity(self, value):
        # PROTECTED REGION ID(SoftiPIE754.Velocity_write) ENABLED START #
        """Set the Velocity attribute."""
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.Velocity_write

    def read_DialPosition(self):
        # PROTECTED REGION ID(SoftiPIE754.DialPosition_read) ENABLED START #
        """Return the DialPosition attribute."""
        return self.__dial_position
        # PROTECTED REGION END #    //  SoftiPIE754.DialPosition_read

    def write_DialPosition(self, value):
        # PROTECTED REGION ID(SoftiPIE754.DialPosition_write) ENABLED START #
        """Set the DialPosition attribute."""
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.DialPosition_write

    def read_OnTarget(self):
        # PROTECTED REGION ID(SoftiPIE754.OnTarget_read) ENABLED START #
        """Return the OnTarget attribute."""
        return self.__on_target
        # PROTECTED REGION END #    //  SoftiPIE754.OnTarget_read

    def read_ServoOn(self):
        # PROTECTED REGION ID(SoftiPIE754.ServoOn_read) ENABLED START #
        """Return the ServoOn attribute."""
        return self.__servo_on
        # PROTECTED REGION END #    //  SoftiPIE754.ServoOn_read

    def write_ServoOn(self, value):
        # PROTECTED REGION ID(SoftiPIE754.ServoOn_write) ENABLED START #
        """Set the ServoOn attribute."""
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.ServoOn_write

    def read_PosError(self):
        # PROTECTED REGION ID(SoftiPIE754.PosError_read) ENABLED START #
        """Return the PosError attribute."""
        return self.__pos_error
        # PROTECTED REGION END #    //  SoftiPIE754.PosError_read

    def read_PosTolerance(self):
        # PROTECTED REGION ID(SoftiPIE754.PosTolerance_read) ENABLED START #
        """Return the PosTolerance attribute."""
        return self.__pos_tolerance
        # PROTECTED REGION END #    //  SoftiPIE754.PosTolerance_read

    def write_PosTolerance(self, value):
        # PROTECTED REGION ID(SoftiPIE754.PosTolerance_write) ENABLED START #
        """Set the PosTolerance attribute."""
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.PosTolerance_write

    def read_Acceleration(self):
        # PROTECTED REGION ID(SoftiPIE754.Acceleration_read) ENABLED START #
        """Return the Acceleration attribute."""
        return self.__acceleration
        # PROTECTED REGION END #    //  SoftiPIE754.Acceleration_read

    def write_Acceleration(self, value):
        # PROTECTED REGION ID(SoftiPIE754.Acceleration_write) ENABLED START #
        """Set the Acceleration attribute."""
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.Acceleration_write

    # --------
    # Commands
    # --------

    @command(
        dtype_out='DevString',
    )
    @DebugIt()
    def GetIDN(self):
        # PROTECTED REGION ID(SoftiPIE754.GetIDN) ENABLED START #
        """
        Gets the IDN of the connected controllers.

        :return:'DevString'
        """
        return ""
        # PROTECTED REGION END #    //  SoftiPIE754.GetIDN

    @command(
        dtype_out='DevString',
    )
    @DebugIt()
    def GetError(self):
        # PROTECTED REGION ID(SoftiPIE754.GetError) ENABLED START #
        """
        Gets the error codes from the controllers.

        :return:'DevString'
        """
        return ""
        # PROTECTED REGION END #    //  SoftiPIE754.GetError

    @command(
    )
    @DebugIt()
    def AcknError(self):
        # PROTECTED REGION ID(SoftiPIE754.AcknError) ENABLED START #
        """
        Acknowledge the errors and clean up the device state and status.

        :return:None
        """
        pass
        # PROTECTED REGION END #    //  SoftiPIE754.AcknError

# ----------
# Run server
# ----------


def main(args=None, **kwargs):
    """Main function of the SoftiPIE754 module."""
    # PROTECTED REGION ID(SoftiPIE754.main) ENABLED START #
    return run((SoftiPIE754,), args=args, **kwargs)
    # PROTECTED REGION END #    //  SoftiPIE754.main


if __name__ == '__main__':
    main()
