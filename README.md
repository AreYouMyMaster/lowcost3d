# Fast Generation 3D Model with Deep Learning
Generation of 3d model has been the bottleneck of modern 3A game production. 
This project is a collection of experiments on applying various techniques, heavily focus on deep leanring, to achieve fast, customizable 3d model/scene generation.

## Technical Issue

### Headless Rendering
In order to view the point cloud generated on a remote server, we decide to use jupyter Open3D + notebook for visualization.

Relevant Open3d documentation:
[web_visualizer](https://www.open3d.org/docs/release/tutorial/visualization/web_visualizer.html)
[docker support, espeically read the `Headless rendering` section](https://www.open3d.org/docs/release/docker.html)

Addtional reading:
[EGL introduction from Nvidia](https://developer.nvidia.com/blog/egl-eye-opengl-visualization-without-x-server/)
[EGL introduction on KHRONOS site](https://www.khronos.org/egl)
