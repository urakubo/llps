Test simulation of CaMKII-GluN2Bc system

-------------------------------------------

- Concentration dependence

  -- python3 prep_files.py

  -- python3 run_files.py (run on open PBS)

  -- vmd -e Make_final_images.vmd (Molecular color problem is unsolved)

  -- You will see the snapshots in the directory imgs


- References

  -- Scripting in VMD

https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/node4.html


  -- I put the following "remove_long_bonds" in $HOME/.vmdrc

https://www.ks.uiuc.edu/Research/vmd/mailing_list/vmd-l/23787.html

  -- Based on demonstatration 1: Single Molecule Example - DiBlock Copolymer
