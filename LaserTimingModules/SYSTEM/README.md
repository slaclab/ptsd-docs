This version of the LTMS system documentation applies to a typically configured LTMS installation at SLAC. Specific installations may have slight variations in components or operation, typically due to the nature of the specific requirements of the site, or the equipment specific to the site that require slight modifications to the standard system.

This document applies to the following module version numbers and design variants:

| Module | Version Numbers               | Variants |
|:-------|:------------------------------|:---------|
| FQMT   | 261-201-15-C02                | A,B      |
| IQPC   | 261-201-19                    |          |
| IQPS   | 261-201-17                    |          |
| LSIT   | 261-100-50-C02                | A        |
| PHDT   | 261-201-10                    |          |
| PLLM   | 261-201-20                    |          |
| PWSU   | 261-201-27-C00                |          |
| RECV   | 261-100-46-C02/261-100-48-C01 | A,B      |
| RFFO   | 261-201-04-C02                |          |
| TGRS   | 261-201-03-C05                | A        |
| DITM   | 261-100-53-C00                |          |
| RDIV   |                               |          |


While this document attempts to be comprehensive in its coverage of the installation, operation and maintenance of the LTMS systems, it is likely that certain topics might be unintentionally overlooked or under represented. In the event that you are not able to find an answer to a question regarding the LTMS, feel free to contact the parties currently managing the LTMS system and installations.

Legal considerations: _Per SLAC regulations regarding the outside release of design information, this document should be considered confidential and for internal use only unless approved by SLAC management. Further, requests for documentation will be considered on a per-request basis, and receipt of this document or any of the module manuals does not convey copyright to reproduce this document in part or in whole._

#### Introduction
The Laser Timing Module System was developed as part of the Timing System Taskforce convened at SLAC in late 2011. Originally tasked with creating a replacement system for the existing laser timing system deployed as part of LCLS-I on the hutch laser systems. The system performed well and was deployed throughout the site on various laser systems, including all LCLS-I hutch laser systems, the LCLS-I Injector Laser systems (x2), FACET’s experiment laser, and the ASTA UED laser system.

The system is composed of a number of core modules based on the Stanford Research Systems Small Instrumentation Module framework. We decided to separate specific functions into separate modules to increase re-usability and supportability. While components on their own can and have been used for a wide variety of applications, a full installation of these modules configured as a laser timing system performs the following functional processes:

1. Produce RF signals from an accelerator reference and a laser oscillator at roughly equivalent harmonic frequencies
2. Downmix and phase compare these two signals with a two stage, heterodyne receiver/phase detector combination
3. Modulate the laser oscillator cavity length to phase lock the oscillator to the accelerator reference
4. Control arbitrary phase shift in the oscillator, along with accelerator timing to provide absolute timing shift control

Additional components of the system have been created to either support this function, such as high speed timing discriminator and trigger re-synchronization systems to RF and DC power supply distribution systems.

Further, a key component of the operation of these systems is the software that drives them, and determines how timing is actually controlled. Therefore, a description of the LTMS system is not complete without describing the control system software that is required to successfully operate and integrate the system.

This component of the LTMS documentation will describe the general features of the system, how it is assembled, installed and operated, and provide information about cost, production time, production and testing structures, development issues, and more.

#### Description and features

The Laser Timing Module System is composed of components that perform specific sub functions. In some are more generally applicable than others. For example, the RF Fanout (RFFO) is a broad band module that generates 8 copies of an input RF signal in a shielded, ruggedized 1U rack mount unit. This can be used in a variety of settings. Conversely, the Event Synchronizer (Trigger Re-Sync, or TGRS) is designed specifically to work with SLAC and VME EVR modules, and the SLAC 476 MHz Accelerator Reference RF.

Separate from these "single" function modules, the LTMS also includes the Digital Interface Module (DITM). There is more information in the specific documentation for this module, but in brief, this module is an FPGA with ADCs and DACs, plus communication channels, that is intended to be used within an algorithm development workflow, incorporating Matlab/Simulink and System Generator. This makes the module have significant adaptability and reusability.

The modules are divided into two form factors. The majority of the modules are designed around the Stanford Research Systems SIM (Small Instrumentation Modules) form factor, and are used in an SRS SIM900 mainframe. The other modules are individually rack-mountable in standard 19” instrumentation racks.
