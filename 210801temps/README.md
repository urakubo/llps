Test simulation of CaMKII-GluN2Bc system
Based on demonstatration 1: Single Molecule Example - DiBlock Copolymer
-------------------------------------------

- Temparature dependence

-- python3 prep_files.py

-- python3 run_files_openPBS.py (run on open PBS)

-- python3 run_files_sequential.py (run on single core sequentially)

-- python3 run_files_parallel..py (run using multiple processes on a single computer)

-- vmd -e Make_final_images.vmd (Molecular color problem is unsolved).

-- You will see the snapshots in the directory imgs


- References

-- Scripting in VMD

https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/node4.html


-- I put the following "remove_long_bonds" in $HOME/.vmdrc

https://www.ks.uiuc.edu/Research/vmd/mailing_list/vmd-l/23787.html

