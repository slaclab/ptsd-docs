# Introduction
# Important Notes
The Digital Interface Module is often not a drop-in replacement, given the firmware that is loaded on the module can perform a wide range of functions. In general, the user needs to verify ahead of time that the correct firmware is loaded on the module before deploying for operation. However, in the future, we may deploy functional blocks that will allow the firmware to identify what images are loaded on a given module making it easier for the end user to determine configuration.

The DITM module contains components that may be export restricted depending on the intended country the module is being taken to. Before offsite use, consult your LTMS contact to confirm whether or not your system is restricted from transport to a given country.
# Description and Features
The Digital Interface Module (DITM) is a flexible development platform coupled to an analog ADC/DAC board that, in its default application, implements the feedback term in the laser rf-locking system, and provides the primary control on oscillator phase. The digital board utilizes a Xilinx Vertex 6 FPGA, and is designed to be used within either a conventional VHDL/Verilog development environment, or in a Matlab/Simulink plus SystemGenerator workflow developed as part of the design of this module. As a result of supporting these two workflows, this module is an attempt at making a widely configurable platform for general use in labs and experiments.

The analog board that is packaged in a standard DITM module includes four ADCs and four DACs. These are used for eternal I/O. More information on these channels is provided in the section "Electrical Characteristics."

The DITM module is designed to operate in the SRS SIM900 mainframe, and is two mainframe units wide. The module is built into the SRS SIM9B2 component. The Module includes the following interfaces:
|Interfaces||
|---|---|
|1x | Jtag interface|
|1x | RS-422 interface|
|1x | SFP interface|
|4x | LEMO-00 front panel connectors (two input, two output)|
|8x | SMA front panel connectors (four input, four output)|
|1x | Dsub-15 mainframe interface (back panel)|
|1x | Dsub-9 external interface (back panel)|

# Operation Details
This section will describe operation of the DITM module only within the context of the LTMS used for rf-locking and timing control of a laser. For information regarding the DITM configured with other firmware versions, refer to the documentation for that firmware and variant.

The DITM module has six primary interfaces used in operation with a laser system. The primary inputs are:
1. Enable/Disable locking
- This opens and closes the feedback loop used to rf-lock the laser
2. Motor step increment
- This control accepts counts from the IQPC module, stepping the phase offset of the feedback term. The resolution of a single step is set in the firmware of the module, and is typically configured to be ~383 urad per step, equal to approximately 16 fs.
3. Motor step direction
- Simply sets the direction to increment the phase
4. Feedback error gain scaling
- This control is provided to switch the diagnostic "error output" signal between a high resolution and full scale mode.
5. Signal 1 input
6. Signal 2 input

[diagram of front panel and back panel with interface callouts](#TODO:2)

These last two signals are the primary inputs to the phase-locking feedback loop. These inputs are processed to generate a relative phase difference. This difference is effectively inverted and output to the DAC 0 channel as the correction necessary to minimize the phase difference plus the requested phase position provided by the user.

In typical operation, this feedback is sent to the control input of a piezomotor driver which in turn drives a piezomotor controlling a mirror in the oscillator laser cavity that sets the cavity length. By modulating the cavity length, the total cavity rep rate is controlled, and my adjusting the cavity rep rate (or oscillator frequency) over time, the system adjusts phase.

The DITM module, configured for standard operation in an LCLS-I laser system, is intended for inputs signals at 250 kHz, which are provided by the front end receiver module (RECV).

In addition to the feedback correction term, three monitor outputs are provided on DAC channels 1-3:
|Channel|Function|
|---|---|
|1|Input 1 amplitude|
|2|Input 2 amplitude|
|3|Amplitude of phase error (set by the Feedback error gain scaling control input)|

# Configuration
## Installation
**Installing a digital module in an installation that has been running analog phase control and feedback modules.**

Many systems around the facility have been commissioned with analog modules for phase control and locking. The following procedure should be used for replacing the analog modules with the digital module.

1. Unlock system
- Switch automatic operation to "manual" (ie. disable the automatic mode operation). This will keep the locking logic from trying to operate while the hardware is disabled.
- Switch rf lock mode to "disabled".
2. Remove signals
3. Remove analog modules
- Remove PLLM module.
- Remove PHDT module.
- Remove IQPS module.
- Remove IQPC module. As of this document revision, the IQPC module is still used for communication with the DITM module. However, a modified version of the controller is used, so the existing one needs to be removed.
4. Power down SIM900 crate
5. Modify back panel wiring

|Site-Specific Wiring Details|
|---|
|A typical installation of the locking hardware will use din rail mounted interface modules to break out the back panel connectors of the locking system modules. At SLAC we use a variety of ADC and DAC modules to interface the locking hardware with the control system. The specific choice of modules is up to those maintaining control systems for a given facility. This description assumes the use of Acromag ADCs and DACs (IP330 and IP231). Vendor-specified procedures should be followed for wiring up connections. For more information, see either SLAC documentation or vendor manuals.|

The following pins are used on the digital module back panel dsub-9 connector:

|Wiring Pinout Description||
|----|---|
|1 (3-rtn) | RF Lock Enable|
|2 (5-rtn) | readback gain. In current operation, this can be tied together (grounding pin 2). However, if a DAC channel is available, wiring this up to the control system will allow for control of readback levels, if desired.|

[Picture of back panel with connectors](#TODO:2)

6. Install DITM module and IQPC module
7. Configure IQPC module

|IQPC Firmware Note|
|---|
|When the IQPC module is first booted in a given control system environment, certain boot procedures will be triggered depending on the configuration of the environment. When installed into the LCLS experiment ("photon") system, the internal smart motor controller is designed to connect to the control system and load a firmware image that, until a factory reset, will be used every time the module is booted. This firmware includes save-restore and position updating information. The accelerator-side controls system is not configured to deploy this firmware. Therefore, an IQPC module that has been previously on the photon controls system must be factory reset and fully reconfigured before being used elsewhere.|

The primary configuration change required for the module is setting party mode and step scaling for 14 bits per 2*pi radians. Party mode can be configured by connecting to the module via an RS-422 adapter or via the Digi Portserver TS MEI ("Digi") used to communicate with the controller. More information can be found at : FAQ for IMS and MForce
If connecting via a Digi, the Digi configuration should be as follows:

**Digi Configuration**
|Option|Setting|
|---|---|
|a. Baud Rate| 9600|
|b. Data Bits| 8|
|c. Parity| NONE|
|d. Stop Bits| 1|
|e. Flow Control| NONE|
|f. Communication | Set for EIA-422/EIA-485 communication|
|g. Pin Out| Un-terminated and 4-wire|
|h. Alternate Pin-out|Enable alternate pin-out for 4-wire mode|
|i. Transmission Control| Always keep transmitter enabled|
|j. telnet|Telnet to Telnet TCP Port (21xx - where xx is digi serial port number)|

When starting with a virgin IQPC, or with one of unknown origin, the configuration should be cleared and re-loaded using the following command sequence:
IQPC MForce Controller Configuration Commands
Enter these commands one-by-one into your terminal window:

1. FD\<Enter> or 1FD\<Ctrl-J> if the controller is in party mode, to factory reset it.
1. S7=49,0\<Enter> to enable step and direction output (this also sets S8 to 49,0)
1. CM=1\<Enter> to enable clock mode out
1. CW=0\<Enter> to minimize clock pulse width
1. DN="1"\<Enter> to set the device name to "1"
1. EM=2\<Enter> to disable local echo and the prompt
1. PY=1\<Enter> to enable party mode
1. 1S\<Ctrl-J> to save all settings to NVRAM

The controller should be power-cycled after this sequence and all settings checked for consistency before deployment.

While telnet'ed to the controller, PR AL <Enter> will print out the complete configuration for the controller. A specific parameter can be substituted for AL. If the device is in party mode, the equivalent command is 1PR AL<Ctrl-J>.

8. Connect front panel connections

- Front panel connections (DITM)
- AIN0 <- From Diode
- AIN1 <- From RF Reference
- AOUT0 -> Piezo Amplifier
- AOUT1 -> Diode Power RB
- AOUT2 -> RF Pwr RB
- AOUT3 -> Phase Error RB
- DIN0 -> Direction
- DIN1 -> Step

Front panel connections (IQPC)
- C -> Step (connect to DITM DIN1)
- D -> Direction (connect to DITM DIN0)

Typically, attenuation should be added to the RF Reference and Diode inputs to the digital module. This has tended to be between 6 and 10 dB for both channels, depending on the signal amplitude.

9. Power on SIM900 mainframe. Front panel LEDs on the digital module should indicate either sufficient or out of range signals for the reference and diode RF. If low levels are indicated, or the control system readbacks read <2V or >4V, adjust attenuation to bring the levels within this range.

|Out of Range Voltages|
|---|
|In the case the signal levels supplied are outside the range of the module, the readbacks are programmed to read -1 V (confirm this).|

10. Verify locking functionality
11. Verify phase control functionality

## Startup
In general, the LTMS modules designed to be used in the SIM 900 Mainframe are hot-swappable, but in most cases, we recommend shutting the mainframe down before removing, or more importantly, installing a DITM module. The firmware that is typically installed on the DITM often has startup protection components (such that systems are brought up in the correct order). However, in the most conservative sense, it is safer to power down the mainframe before installing the module.

[Notes on startup procedure](#TODO:2)
## Shutdown
## Usage
|Front Panel LEDs|
|---|
|The front panel LEDs will not indicate whether signal levels are sufficient for operation unless both Reference and Diode signals are present.|
[closeup picture of leds with callouts](#TODO:2)

## Settings for Operation
# Cabling and Pinouts
# Absolute Maximum Ratings
# Electrical Characteristics
# Typical Performance Characteristics
# Software
## List of Software
## Description of Software
# Implementation Details
# Revisions
# Electrical
## Schematics
## Fabrication
## Loading Instructions
# Mechanical
## Fabrication
# Troubleshooting
# Resources
# Web Links
# Documents
# Software Details
## Software Documentation
# Testing and Production
## Procedure
**Testing Setup**
Testing the DITM module requires the following test equipment:
1. SIM 900 mainframe
2. Dsub-15 extension configurable
2. SIM 940 Rb Source
3. 2x AFG or RF CW Source capable of generating a 250 kHz or 1MHz tone (depending on variant of DITM module); One of these sources should have externally controlled phase modulation capability
4. 3x BNC T adapters
5. 10x cables (probably BNC terminated RG-58)
6. Oscilloscope

Additionally, to test phase control, you'll need either an IQPC phase control module (another part of the LTMS system), an Atom server correctly configured for communication with the DITM module (see section)[set correct section reference](#todo) , or a revision of the DITM module that includes the communcation channel.

**Test of General Functionality**
Testing general functionality of the DITM module includes testing the following:
1. Communications
2. Power supply and boot up
3. Programming and boot sequence
4. Firmware revision reporting

**Test of LTMS Functionality**
Testing of the LTMS functionality in the DITM module depends on testing the output of the module with specific input parameters. Specifically, testing covers the following:
1. Input monitoring and LED operation
2. Feedback output term
3. Diagnostic readback output
4. Enable/Disable operation
5. Gain scaling

## V&V Traveler
## Production Record
