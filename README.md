# distortion_hotmap
## Utility
To visulize the lattice distortion after the geometric optimization or along a dynamic trajectory. 
Structure file in `vasp` format.

## Flow chart
1. Data of two corresponding `POSCAR`s
2. Calculate the `displacement matrix`
3. Calculate the `displacement scalar`
4. Plot atomic stick-ball figure
5. Add the hotmap based on `displacement matrix` and `displacement scalars`

## Example
![local distortion](local.jpg)
![delocal distortion](delocal.jpg)

## Bugs
