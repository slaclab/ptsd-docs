# ptsd-docs
Documentation repository for the Precision Timing Systems groups.

This repository collects material covering the following systems:
* Laser Locking Systems
* Stabilized Coax Reference RF System
* RF-over-Fiber
* Undulator Phase Cavity System

Additional systems will be incorporated as needed. Documents can be found in one of two primary formats, either flat files written using the Pandoc Markdown format or in an extensible json format appropriate for use in templating engines.

In addition, attachments and resources appropriate for documentation generation will be included in supporting directory structures. Large or variable formats (particularly binary formats) should not be included in this repository. Of particular note, certain source documents might be compiled into documentation, at build, from the design file master directories. For additional information about this structure see #todo:ref.

Unlike the previous incarnation of the precision timing system documentation, release and pre-release material is maintained using git branches, and obsolete versions of documentation can be found in the revision history of the repository.

Moreover, this is a generative repository, used for producing source documentation. The intent here is not to distribute user-facing documentation. It is not the intended way to distribute material to end-users and collaborators.

