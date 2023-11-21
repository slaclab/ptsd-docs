% ReadMe - Documentation Management for Precision Timing
% Justin May
% 2020-06-11 18:04:20

----
| Metadata | Value |
|----|----|
|Tags|documentation, jinja, pandoc|
|Usage|Internal Use, Guidance for Developing Equivalent Approaches|
|ROU|2021-06-1|
|Reviews| This document is not a controlled document, and has no review procedure that involves signatories|
|Versions| 1.0 - Initial Version|

Documentation at SLAC represents a perpetual challenge. The composition, collection and management of effective documentation for the vast assortment of systems at SLAC represents a massive amount of work, and at the same time is difficult to do well. It is not a project that has an end point. It instead relies on the training and habits of employees to efficiently maintain documentation of their work both while it is in progress and while the resulting work is still in service at the laboratory. At the same time, it is often the critical piece that is missing when a system goes down; if you want to make a system long-term supportable in a way that minimizes hidden expense in terms of science and lost time, good documentation is a big part of achieving that.

Good, persistent, accessible documentation is not a challenge unique to SLAC. Every industry and business practice to some extent faces the same challenges. Software development, in particular, inherits a great deal of subsystems that get incorporated into projects, often very quickly, such that documentation while in development can quickly be lost unless rigorous practices are applied. The transfer of design information in a mechanical engineering project can quickly distance the project from the design choices leading it, unless good practices are employed.

In the precision timing group at SLAC, we've faced both these conventional challenges in software, electronic, mechanical and system engineering, but we have the additional challenge of having unique sets of information that are difficult to convey well with existing tools. One example is the description of timing events. We deal with picosecond to attosecond effects for which we still need to describe temporal relationships out to the microsecond or slower. This means we often need adaptive plots and diagrams that are not very easy to manage by hand.

To address the needs of the precision timing program, we've defined a set of systems and protocols to assume for documentation that are intended to mitigate the management overhead of creating documentation (typically long after a system is complete and operational), while providing tools that reduce the amount of duplicate work that is needed to get this information in the right places.

# Documentation Types

Documentation types fall into two primary categories so far. These are:
1. Flat File Documentation
2. Compiled Documentation

## Flat File Documentation

Flat file documentation is written in Markdown with a delivery target of Pandoc. The Pandoc library is generally consistent, and in general, no additional libraries or processors are needed for Markdown that is appropriate for documentation.

To aid in writing, a snippets file for VSCode has been compiled for Markdown that will provide basic formatting for the core ReadMe file. The default ReadMe that is included in the provided template folder is based off of this snippet set (but will not have tab insertion points enabled like a snippet initially would).

## Compiled Documentation

Compiled documentation is built in the sense of compiling code, but does not use code-centric build tools. We've settled on using the Jinja templating engine for building dynamic documentation sets that can then be processed using Pandoc as needed. After documentation is updated to the managed repositories, a process will convert the provided files in each directory that has had changes made to it, after which the updated documentation sources are pushed to specifically defined destinations. This output is also available to be pulled into other client systems as needed.

When working with an assembled document, you are not required to use a specific template and data format. The default folder template includes both, but a given project will often need to support slightly different formatting, headers, cell types, etc.

Approaches used here are similar to the process one would use to build documentation from a Jupyter notebook. If used, we'd suggest implementing a similar style of management.

In general, flat file documentation should be sufficient for most applications. The case where a templated production process makes sense is when you are already working with a system that will provide easy production of the json files you will be populating the template from. Examples of this soft of system would be a python analysis using Pandas dataframes, crawling CAPTAR data for cable plants, generating test sets from criteria in spreadsheets, etc.

# Managing Documentation

## Documentation Lifecycle

Every source document generated should include a ROU (Retire or Update) date that represents a date when the documentation should be reviewed by the point of contact (author or inheritor) for up-to-date content and applicability. If the system involved is no longer active, then the documentation should be pruned from existing distributions and archived appropriately.

## Version Control

Documentation is intended to be version controlled (currently in git). Therefore, large resources should not be included directly in the resources subdirectory. A standard git ignore file is included that will ignore common video formats and other large file types.

If a documentation source is managed in a repository, if the documentation is determined to be a candidate for retirement, then the repository ReadMe should be modified to show that it is no longer active, though the repo can be left in place for archiving purposes.

## Metadata

All documentation should include metadata (in the case of a templated file) or pseudo-metadata in the form of defined markdown-formatted introductions to documentation.

# References

Pandoc and the markdown formatting it supports can be found here:

[Pandoc](https://pandoc.org)  
[Pandoc and Markdown](https://pandoc.org/MANUAL.html#pandocs-markdown)  

Jinja, including information on the installation and use of it and the Jinja templating language can be found here:

[Jinja](https://jinja.palletsprojects.com)  
