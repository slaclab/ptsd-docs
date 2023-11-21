Title

Document Revision:
Template Revision:

Table of Contents

Important Notes
Description and Features

The digital interface module, also referred to as either the DSP module (for digital signal processing) or digital timing module is a multipurpose module developed as part of the laser timing module system. It contains a general purpose FPGA and a basic set of I/O channels. It also provides varied communication channels/protocols for programming and interfacing with the module and onboard firmware, including a SFP port. The module is designed to operate in the SRS SIM900 Mainframe, a general purpose lab component framework which, in comparison to more exhaustive frameworks like VME or ATCA/uTCA, is relatively inexpensive to deploy and support.

In addition, the module was developed, at least originally, to support firmware authoring and deployment using Matlab and Simulink, along with Vivado's System Generator pipeline to make it easier for scientists and engineers to deploy FPGA-based DSP solutions.

The first generation of the module has extensive operational hours having served as the core feedback processor for the laser rf-locking and timing system for lasers used in multiple facilities at SLAC for over five years, in addition to being used in additional implementations. All told this is likely greater than 500,000 hours, with one or two module failures during that time.

PCBs  

The module contains two boards, separating digital and analog circuits. The digital board contains the bulk of the general purpose I/O and communication channels, as well as the FGPA and associated components. The analog board provides the ADCs and DACs.

Digital Board Highlights
FPGA: Xilinx Kintex-7 FPGA Datasheet

SFP socket, with firmware to drive general purpose or high-rate dedicated network communication
Serial communication for debugging
JTAG access for loading firmware
2x channels of digital input (via front panel LEMO-00)
2x channels of digital output (via front panel LEMO-00)
Analog Board Highlights
4x 16-Bit ADCs Datasheet

4x 18-Bit DACs Datasheet

Operation Details
Configuration
Installing a digital module in an installation that has been running analog phase control and feedback modules.

Many systems around the facility have been commissioned with analog modules for phase control and locking. The following procedure should be used for replacing the analog modules with the digital module.

Unlock system
Switch automatic operation to "manual" (ie. disable the automatic mode operation). This will keep the locking logic from trying to operate while the hardware is disabled.
Switch rf lock mode to "disabled".
Remove signals
Remove analog modules
Remove PLLM module.
Remove PHDT module.
Remove IQPS module.
Remove IQPC module. As of this document revision, the IQPC module is still used for communication with the DITM module. However, a modified version of the controller is used, so the existing one needs to be removed.
Power down SIM900 crate

Modify back panel wiring

A typical installation of the locking hardware will use din rail mounted interface modules to break out the back panel connectors of the locking system modules. At SLAC we use a variety of ADC and DAC modules to interface the locking hardware with the control system. The specific choice of modules is up to those maintaining control systems for a given facility. This description assumes the use of Acromag ADCs and DACs (IP330 and IP231). Vendor-specified procedures should be followed for wiring up connections. For more information, see either SLAC documentation or vendor manuals.

The following pins are used on the digital module back panel dsub-9 connector:

1 (3-rtn) : RF Lock Enable
2 (5-rtn) : readback gain. In current operation, this can be tied together (grounding pin 2). However, if a DAC channel is available, wiring this up to the control system will allow for control of readback levels, if desired.




Install DITM module and IQPC module

Configure IQPC module

When the IQPC module is first booted in a given control system environment, certain boot procedures will be triggered depending on the configuration of the environment. When installed into the LCLS experiment ("photon") system, the internal smart motor controller is designed to connect to the control system and load a firmware image that, until a factory reset, will be used every time the module is booted. This firmware includes save-restore and position updating information. The accelerator-side controls system is not configured to deploy this firmware. Therefore, an IQPC module that has been previously on the photon controls system must be factory reset and fully reconfigured before being used elsewhere.

The primary configuration change required for the module is setting party mode and step scaling for 14 bits per 2*pi radians. Party mode can be configured by connecting to the module via an RS-422 adapter or via the Digi Portserver TS MEI ("Digi") used to communicate with the controller. More information can be found at : FAQ for IMS and MForce 
If connecting via a Digi, the Digi configuration should be as follows:

Baud Rate: 9600
Data Bits: 8
Parity: NONE
Stop Bits: 1
Flow Control: NONE
Set for EIA-422/EIA-485 comminication
Pin Out; Un-terminated and 4-wire
Enable alternate pin-out for 4-wire mode
Transmission Control: Always keep transmitter enabled
Telnet to Telnet TCP Port (21xx - where xx is digi serial port numner)

When starting with a virgin IQPC, or with one of unknown origin, the configuration should be cleared and re-loaded using the following command sequence:

Enter these commands one-by-one into your terminal window:

1. FD<Enter> or 1FD<Ctrl-J> if the controller is in party mode, to factory reset it.
2. S7=49,0<Enter> to enable step and direction output (this also sets S8 to 49,0)
3. CM=1<Enter> to enable clock mode out
4. CW=0<Enter> to minimize clock pulse width
5. DN="1"<Enter> to set the device name to "1"
6. EM=2<Enter> to disable local echo and the prompt
7. PY=1<Enter> to enable party mode
8. 1S<Ctrl-J> to save all settings to NVRAM

The controller should be power-cycled after this sequence and all settings checked for consistency before deployment.

While telnet'ed to the controller, PR AL <Enter> will print out the complete configuration for the controller. A specific parameter can be substituted for AL. If the device is in party mode, the equivalent command is 1PR AL<Ctrl-J>.





Connect front panel connections

AIN0 <- From Diode

AIN1 <- From RF Reference

AOUT0 -> Piezo Amplifier

AOUT1 -> Diode Power RB

AOUT2 -> RF Pwr RB

AOUT3 -> Phase Error RB

DIN0 -> Direction

DIN1 -> Step




C -> Step (connect to DITM DIN1)

D -> Direction (connect to DITM DIN0)




Typically, attenuation should be added to the RF Reference and Diode inputs to the digital module. This has tended to be between 6 and 10 dB for both channels, depending on the signal amplitude.

Power on SIM900 mainframe. Front panel LEDs on the digital module should indicate either sufficient or out of range signals for the reference and diode RF. If low levels are indicated, or the control system readbacks read <2V or >4V, adjust attenuation to bring the levels within this range.

In the case the signal levels supplied are outside the range of the module, the readbacks are programmed to read -1 V (confirm this).




Verify locking functionality
Verify phase control functionality
Startup
Shutdown
Usage

The front panel LEDs will not indicate sufficient signal levels unless both Reference and Diode signals are present.




Settings for Operation
Cabling and Pinouts
Absolute Maximum Ratings
Electrical Characteristics
Typical Performance Characteristics
Software
List of Software

Firmware Version Numbers - These numbers are reported on status register 8.

Description	Major Version Byte	Minor Version Byte	Firmware Type
Files from ssmith afs: LaserLocker_00000006.mcs, LaserLocker_00000006.bit (dated 8/26/2015)	
	
	


	
	
	


	
	
	


	
	
	


	
	
	


	
	
	


	
	
	





Description of Software
Implementation Details
Revisions
Electrical
Schematics
Fabrication
Loading Instructions
Mechanical
Fabrication
Troubleshooting
Resources
Web Links
Documents
Testing and Production
V&V Traveler
Production Record
Software
Software Documentation