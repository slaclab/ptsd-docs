# Generation 1 Laser Locker  
## Simple Commissioning Instructions  

**Author:** J. May  
**Initial Date:** 2021-06-02  
**Version:** 1.0   
____
# FQMT

The frequency multiplier expects 0dBm input, nominally at 476 MHz. The 3808
output will be nominally 0 dBm as well. The other outputs are typically +/- 2
dBm, but their harmonic content is non-optimal, and should not generally be used
in installations. Best phase noise performance will be with the other
inputs/outputs terminated into 50 Ohm.

# RECV

The front end down converter generates LO internally from the 10 MHz reference
provided to the SIM900. Therefore, the crate should have a high-quality RF
reference provided to it, typically via the SRS Rb frequency standard installed
in the crate, with an output connecting that module's outputs to the input on
the crate. The DIP switches need to also be set appropriately to distribute the
reference to the slots.

The input levels are something like -40 dBm to the reference input and -50 dBm
to the laser (diode) input. This is with the gain of the opamp stages set to
minimum (set via trim pots accessed through two holes in the front panel of the
module). The scale of the diode input is determined by the nominal operating
point of the ET-4000 photodiode with the Vitara oscillator. It is best to set
and maintain this level via diode alignment, once proper external attenuation is
added to set the appropriate inputs to the RECV. Do not use the op amp gain
except in cases where the diode alignment is optimized and you need to adjust
the signal levels finer than the 1dB afforded by external fixed attenuators.

Note, when setting these levels, it will feel like you're putting a ton of
attenuation in line, but don't worry too much about it.

To verify the levels are correct, you can look at three signals. First, look at
the monitor outputs on the RECV, or the actual outputs. The monitor outputs can
be put directly on a scope, whereas the main outputs will need to be terminated
in either a 50 Ohm pass-through or scope impedance. These signals will be a sine
wave that is a few dB below saturation (which will be clear on a scope trace by
the sinewave clipping). When set correctly and connected to the inputs on the
DITM module (see following), the readback levels of the DITM should indicate
something between 3.2 and 3.6 Volts.

# DITM

The DITM module has six inputs, and four outputs. See figure for a visual
description of the various connections.

The Enable/Disable and feedback input gain scaling connections are accessed via
the back panel db9 connector. In general the gain scaling should be connected to
ground (the firmware is designed for the vitara oscillator and piezodrive
amplifier response). The enable/disable is 0V:enable, 5V:disable.

The front panel inputs will be crossed in two places, a result of how the
designs and board layouts were done. I point this out here, because if it
doesn't look weird, you probably haven't set it up correctly.

The phase control, incorporating the IQPC module (described below) takes step
and direction inputs to rotate through the internal phase parameter space.
Output C from the IQPC should go to DIn1, and D should go to DIn0.

The downconverted diode signal from the RECV should be connected to Ain0, and
the downconverted reference RF should be connected to Ain1. The output signals
in order from AOut0 and increasing, are the piezo amplifier control signal, the
diode average rms, rf reference average rms, and phase error. These last three,
along with the piezo amplifier monitor output, should be connected to the
control system via ADCs.

To summarize:

Front panel connections (DITM)

AIN0 <- From Diode

AIN1 <- From RF Reference

AOUT0 -> Piezo Amplifier

AOUT1 -> Diode Power RB

AOUT2 -> RF Pwr RB

AOUT3 -> Phase Error RB

DIN0 -> Direction

DIN1 -> Step
Front panel connections (IQPC)

C -> Step (connect to DITM DIN1)

D -> Direction (connect to DITM DIN0)

# IQPC

The IQPC incorporates a modified version of the IMS Smart Motor, to provide a
simple motor controller interface to the control system, allowing the phase
control to easily benefit from speed ramp controls without having to implement
them ourselves. The module is communicated with via the RS-422 connection on the
front panel. This will require connection to a serial port server with the
proper cabling. More information can be found in the extended documentation for
the timing system.

# LSIT

The laser interface module combines a number of functions in one module. For
current generations, though, there are must two primary inputs, the second of
two resync triggers from the TGRS module, described below, and the output of the
regenerative amplifier photodiode (typically another ET-4000). The resync
trigger resets the fast flip-flop triggered by the very fast regen diode signal,
such that the Laser Interface module has a clean square wave of rise time
comparable to the laser pulse, and dwell time long enough for the time interval
counter set up time.

The regen diode signal can be difficult to set up correctly. The observed peak
voltage will depend on the reactance of the input impedance on a scope looking
at the diode signal. On a typical 500 Mhz bandwidth scope, you'll be looking for
a peak voltage of around 10 mV. At 2 GHz, likely around 70-80 mV.

To confirm the diode level is appropriate, look at the output of the LSIT via
the complementary output. If the level is too high, you'll see the flip-flop
retriggering close to the original pulse, zoom in, otherwise you might think
that it isn't doing anything. And on the other side, if the signal is too low,
the comparators won't fire so there will be no output from the flip-flop. Once
the optical alignment is set, adjust the signal level via an ND filter wheel
installed in front of the regen diode.

The output of the LSIT should be a pulse with a -400 mV baseline, to 0 V. This
should be connected to the A input of the Time Interval Counter.

# TGRS

The Trigger resync expects a typical EVR input, and an RF reference at nominally
0 dBm from the RFFO module. The + input should look like a positive going
trigger pulse with a -400 mV offset. The complementary output should be 0 V to
-400 mV.

The -400 to 0 output should be connected to channel B of the Time Interval
Counter.

# TIC

The time interval counter should always have trigger levels set to -200 mV. In
the case of goose trigger operation, the gate input should be configured
appropriately for this mode of operation. More information on this can be found
on Confluence.