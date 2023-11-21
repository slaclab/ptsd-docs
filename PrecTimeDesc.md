% Precision Timing : Capability Reference
% Justin May
% 2020-06-11 18:04:20
 

## INTRODUCTION  

The scope of the systems described here fall along the lines of the precision timing program. Precision timing represents the integrated monitoring and control of systems that are required to interact beneficially with the core accelerator driver for LCLS but which have independent control relative to the accelerator and FEL photons. Separately, precision timing represents those systems which function at timescales shorter than the framework event system for accelerator facilities. In addition, this terminology is extended to other facilities at SLAC that rely on these systems though without the level of temporal stability or control required of LCLS experiments.

Note, this is an internal definition and the terminology used external to the precision timing groups at SLAC, and beyond the laboratory, vary.

>This document concerns itself primarily with the systems beginning with the Phase Cavities in the Undulator hall through to the experiment hutches, including the fiber timing lab, the reconfigured NEH laser lab and the server instructure installations in the NEH and FEH.

----

The disposition of timing and related systems in the experimental and support areas in the reconfigured NEH and FEH is designed to support the following:
- Reference LLRF signals for use in existing or planned systems (one run of low loss, larger diameter coax for 476 MHz that can be switched if needed to run an LCLS2 rf reference at various frequencies). This provides:
  - Modest provision for possible future capability
- Installation of sufficient fiber for dedicated precision timing systems including:
    - RF-Over-Fiber installations for basic drift-stabilized rf references
      - This implies running additional fiber length such that RFOF fibers can be directly fusion-spliced if performance requirements dictate
    - Timing control signals
    - Sufficient fiber installations for high rate fiber-based systems (alternately referred to as the L2SI Experiment Timing Systems)
- Reference timing signals
  - Provision is made for supplying user/diagnostic timing signals (events from EVRs/TPRs based on system)
- Provision for one reference cable between key areas that is sufficient for impromptu debugging including configurations that require low drift rf signals
- Data processing of timing related data acquisition systems (though not managed through the precision timing program)
- Wave8 data links (Two fibers)

| System                         | Description                                                                                                                                               | Sub-Systems                       | Function                                                                                                                                                  |
|--------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| Phase Cavities                 | Arrival Time Monitor for DAQ and Drift Correction Measurement for NEH/FEH Reference RF                                                                    | --                                | Measure arrival time of electrons by processing the ringdown signal from a resonant cavity pickup                                                         |
| XTCAV                          | Transverse Cavity to Image Electron Temporal Characteristics                                                                                              | --                                | Key diagnostics for accelerator operations for configuring and maintaining the bunch characteristics that lead to the desired FEL output for experiments  |
| NEH Reference RF Distribution  | Drift-Stabilized Low Noise Reference RF                                                                                                                   | Stabilized Coax Reference System  | Baseline system for distributing the rf reference to experiments                                                                                          |
|                                |                                                                                                                                                           | RF-over-Fiber System              | Upgraded system for distributing the rf reference to experiments                                                                                          |
| FEH Reference RF Distribution  | Drift-Stabilized Low Noise Reference RF                                                                                                                   | Stabilized Coax Reference System  | Baseline system for distributing the rf reference to experiments                                                                                          |
|                                |                                                                                                                                                           | RF-over-Fiber System              | Upgraded system for distributing the rf reference to experiments                                                                                          |
| Experiment Timing              |                                                                                                                                                           | Fiber Oven                        | Compensates for thermal drift in the long connecting link between the phase cavities and the experiment areas                                             |
|                                |                                                                                                                                                           | First Generation Laser Locker     | Baseline Locking System for Ti:Sapphire Lasers; utilizes SLAC-designed LTMS Modules                                                                       |
|                                |                                                                                                                                                           | Second Generation Laser Locker    | Upgraded Laser Locking System, appropriate for Ti:Sapphire and High Rate Lasers; utilizes ATCA Common Platform                                            |
|                                |                                                                                                                                                           | X-Ray Optical Cross Correlators   | High Precision measurement of the relative arrival time of FEL and laser pulses in experiments                                                            |
| LCLS2 Master Oscillator        | Reference RF Generator; among many other systems, provides the reference for synchronizing and controlling the timing of the various experiement systems  | RF-over-Fiber System              | This system transmits the reference rf to the initial starting point for rf distribution to the experiments and other functional areas                    |


## How This Is Determined

The determination of what type of signal provision is needed for the scientific output of a facility is determined by the hutch scientists in discussion with the precision timing group. This sort of consideration is captured in diagram and table format in internal documents, but is not reviewed explicitly within a review procedure that includes both precision timing and the hutch teams.

Compared to end-user focused systems like those determined with the hutch teams, the configuration of the precision timing infrastructure that is included is determined from:
1. Determining the elements from the original hutch and beamline configuration that are needed for continuing operation in the reconfigured systems
2. Reference to designs for new timing systems that are part of the LCLS2 and L2S-I Projects
3. Evaluation of the necessary infrastructure that is implied by the combination of the above items


# Notable Examples of New Infrastructure

The precision timing systems going forward heavily leverage the SLAC ATCA-based Common Platform components. Therefore a large amount of ATCA hardware is added to racks in hutches and support facilities in the NEH and FEH. Related to this, we are working to eliminate the dependence on serial interfaces that we used in the first generation hardware, therefore diagrams and tables will see a reduction in the number of serial port servers necessary. At the same time, a standard configuration for the ATCA systems add a number of monitor and interface channels for the crates and servers, so this element will see an increase in the number of necessary communication channels in an installation.

New elements like the Wave8 digitizers used in the new laser systems have signals going to multiple locations, and therefore multiple cable plants.

Systems dependent on fiber installation include both traditional communication channels and dedicated systems that may or may not at some point be fusion spliced. The installation of these systems described here in part dovetail with existing/planned DAQ and controls systems, and count of fibers in particular needs to be considered within the context of fiber trunk runs and total used/used+spares counts. The diagrams and tables defining this work should take this into account.

The systems described include the tiered operation of laser systems as described in previous reviews and documentation. In brief, a full installation as planned includes an RFoF link to an experiment, a laser-based interferometrically stabilized system that operates with narrower bandwidth but improved performance over the RFoF system, and a direct cross-correlation locking system that operates only at high rate but with our best projected performance.

### References

### Notes

- [ ] Todo: Matt has a comment in Stefan's diagram about the relocation of the XPP DAQ farm to the FEH Mezzanine, and whether that still supports our needs for the fiber based systems
- [ ] Describe the laser systems if possible, pull from other documents where able.

- This document does not include power, grounding and network connectivity infrastructure.