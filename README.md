# distortion_hotmap
## Utility
To visulize the lattice distortion after the geometric optimization or along a dynamic trajectory. \\
Input structure file in `vasp` format, output `CHGCAR` like files which can be visualized by `VESTA`.

## Flow chart
1. Data of two corresponding `POSCAR`s
2. Calculate the `displacement matrix`
3. Calculate the `displacement scalar`
4. Grid lattice cell and interpolate displacement value.
5. format data as `CHGCAR`.

## Example
![local distortion](local.jpg)
After geo-opt, only bonds around one Ti expanded, forming a small polaron.
![delocal distortion](delocal.jpg)
A group of Ti atoms expanded their centered octahedrons.

## Bugs
