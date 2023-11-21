# Generation 1.5 Documentation

The generation 1.5 Laser Locker refers to the version of the laser lockers incorporating the ATCA common platform but without a custom RTM (planned for future development). The full matched pair of RF card and RTM would be a "gen 2 locker". Variations of this locker hardware, firmware and different versions of software support are in operation at SLAC, including in sector 0 for the LCLS SC linac injector.


This document provides extended documentation for this system design.

# Setup and Low Level Operation

The firmware for the locker systems, including what is needed for connecting to and communicating with the IOC for the locker, is stored on the board. Upon power on, the carrier card will automatically initiate communication and the locker registers should start updating.