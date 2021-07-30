Test simulation of CaMKII-GluN2Bc system
Based on demonstatration 1: Single Molecule Example - DiBlock Copolymer
-------------------------------------------

- Video1: Spatial distribution of molecules

-- ./../lassi -k param_targ.key

-- vmd -e Make_Video_demo.vmd

-- ffmpeg -r 15 -i imgs_demo/snap.%04d.ppm -vcodec libx264 -pix_fmt yuv420p demo.mp4


- Video2: Time developement of molecular distribution

-- ./../lassi -k param_targ.key

-- vmd -e Make_Video_targ.vmd

-- ffmpeg -i imgs_targ/snap.%04d.ppm -vcodec libx264 -pix_fmt yuv420p -vf "drawtext=fontfile=Arial.ttf: text='Frame\: %{frame_num}': start_number=1: x=(w-tw)/2
: y=h-(2*lh): fontcolor=black: fontsize=25: box=1: boxcolor=white: boxborderw=5" video_targ.mp4



- Video3: Time developement of molecular distribution (control)

-- ./../lassi -k param_ctl.key

-- vmd -e Make_Video_ctl.vmd

-- ffmpeg -i imgs_ctl/snap.%04d.ppm -vcodec libx264 -pix_fmt yuv420p -vf "drawtext=fontfile=Arial.ttf: text='Frame\: %{frame_num}': start_number=1: x=(w-tw)/2
: y=h-(2*lh): fontcolor=black: fontsize=25: box=1: boxcolor=white: boxborderw=5" video_ctl.mp4



- References

-- Scripting in VMD

https://www.ks.uiuc.edu/Training/Tutorials/vmd/tutorial-html/node4.html


-- I put the following "remove_long_bonds" in $HOME/.vmdrc

https://www.ks.uiuc.edu/Research/vmd/mailing_list/vmd-l/23787.html

