# Precision Timing HLA Specification  
#### Written by J. May  
##### Version: 1.0  

## Introduction

The Precision Timing System HLA provides the user interface and functional logic for timing control of laser systems running the Precision Timing Laser Locker ATCA system. It inherits some functional structure from the first generation of the system that was written and maintained, correspondingly, for the first generation laser locker system.

This document presents a functional specification for the application. It includes some of the logical structure of framework as needed/useful. Also included is a design specification for the various user facing interfaces.

For the sake of brevity, the following abbreviations will be used in this document:

PTS - Precision Timing System
CP - Common Platform ATCA system developed by TID
LL - Laser Locker; the hardware and firmware system responsible for the rf synchronization of a connected laser system and the control of the output time of said laser

## Requirements
### Controls

**Set desired output laser time (phase) in femtoseconds**
This is the primary user control for setting the desired output time of the laser system. The use case for the time control varies between system installations (particularly when used for an injector laser as opposed to an experiment laser). Therefore two inputs are presented. This control is a straight value for the output time relative to the reference trigger for the system.
GUI element: active input field
User level: basic user (core function set)

**Set desired output laser time via relative phase**
This is the primary user control for setting the desired output time of the laser system in relative units. The use case for the time control varies between system installations. In the case of injector lasers, often units relative to the master rf reference phase are desired. This control converts values to desired femtoseconds based on an offset value and the desired phase conversion. Operators in a control room will typically find the necessary output time which will have some very large value. We provide the ability to add a soft offset to this value so that they can work with small numbers after zeroing the offset.
GUI element: active input field
User level: basic user
Calculation details:

**Enable/disable the RF locking (synchronization) functionality**
Enable or disable the firmware rf locking feedback within the CP hardware and firmware
GUI element: should be presented as a toggle button
User level: basic user (core function set)

**Enable/disable timing control functionality**
Enable or disable the controls that adjust trigger delays for coarse timing and the phase control for setting the laser to the desired femtosecond-scale output time value
GUI element: float value input in units of picoseconds
User level: basic user (core function set)

**Execute system calibration**
Initiate a calibration of the laser phase relative to the event or pattern system
GUI element: push button
User level: advanced user

**Set reference frequency**
In the case of systems where relative control of the laser phase (relative to a reference RF framework) is desired, the appropriate frequency is set by this control. This should not change once set, and should be considered an advanced setup step.
GUI element: float input field in MHz
User level: advanced user

**Set offset value**
Provided as a convenience function, or quality of life improvement for users, the offset value drives the mechanism by which a user can change to just making small phase angle changes to the laser timing, instead of worrying about absolute numbers or making large time-domain time shifts.
GUI element: float input field in time
User level: advanced user

**Set current time to thirty degrees**
Additional convenience function for further setting the offset value (above) in a single step. The applicability of this function varies, as some machines are designed to run on-crest wrt RF, and others off-crest.
GUI element: push button
User level: advanced user

**Show firmware register values**
Display a sub-panel of firmware register values
GUI element: push button
User level: advanced user

**Show basic user help file**
Display a sub-panel with the help information for the system
GUI element: push button
User level: basic user

**Show advanced user help file**
Display a sub-panel with the help information for the advanced user functionality
GUI element: push button
User level: advanced user

**Show CP installation information**
Dispplay a sub-panel with the CP and ATCA information for the system being controlled
GUI element: push button
User level: advanced user99999

### Display Values

| Readback                          | Unit  | Precision  | Panel       |
|-----------------------------------|-------|------------|-------------|
| Phase Noise                       | fs    | 2          | Basic User  |
| RF Input Voltage                  | V     | 2          | Basic User  |
| Laser Diode Input Voltage         | V     | 2          | Basic User  |
| Delay Readback Value              | ps    | 2          | Basic User  |
| Piezo Amplifier Voltage Readback  | V     | 2          | Basic User  |
| Chamber Motor Position Readback   | um    | 3          | Basic User  |
| Measured Frequency                | MHz   | 3          | Basic User  |

## Calibration Process

## Firmware Management

Any change to firmware for the installed systems should follow existing EED software deployment policies for review and management. No firmware releases should be deployed without the completion of an impact study that needs to include the 

_____________________

# EIC Laser Timing  
## Tasks Remaining  

**Written by J. May**  
*2019-08-23 15:56:02*  

This description represents the extent fo the remaining work for the EIC Injector Laser Timing system. This is not intended to be an exhaustive list, but provides preliminary guidance for considering the remaining work. Items described here are to be accompanied by CATER entries for completion tracking.  

As of 2019-08-23, the HLA and hardware system are commissioned such that they are capable of primary phase control, but do not yet have the components installed and/or configured that are necessary to enable directed timing control. The components that are necessary for completion include the deployment of a time interval counter looking at a new photodiode measuring the output time of the injector laser mpa. We also need to install a trigger re-synchronizer unit that provides the clean reference time measurement. Once this hardware is available, then the modification of the python code to a version that enables time control is necessary. Following this, some development time is necessary to write the calibration and bucket detection sub-routines appropriate to this new laser and timing topology.  

1. Install TIC  
1. Install TGRS  
1. Commission hardware through to active PVs  
1. Update Python  
1. Deploy new panel code 
1. Complete documentation   