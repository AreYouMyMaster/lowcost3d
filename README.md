# Fast Generation 3D Model with Deep Learning
Generation of 3d model has been the bottleneck of modern 3A game production. 
This project is a collection of experiments on applying various techniques, heavily focus on deep leanring, to achieve fast, customizable 3d model/scene generation.

## Set-up and Unit test

Simply build the Docker image with: `docker build -t lowcost3d .`
If you have access on our private server `city7`, it's already built there.

Assuming the Objaverse data is in the `/rawdata3` directory, execute the command at project root to run all unit tests:
`docker run -it -v \`pwd\`:/workspace -v /rawdata3:/rawdata3 lowcost3d pytest`

## Technical Issue

### Headless Rendering
In order to view the point cloud generated on a remote server, we decide to use jupyter Open3D + notebook for visualization.

Relevant Open3d documentation:
[web_visualizer](https://www.open3d.org/docs/release/tutorial/visualization/web_visualizer.html)
[docker support, espeically read the `Headless rendering` section](https://www.open3d.org/docs/release/docker.html)

Addtional reading:
[EGL introduction from Nvidia](https://developer.nvidia.com/blog/egl-eye-opengl-visualization-without-x-server/)
[EGL introduction on KHRONOS site](https://www.khronos.org/egl)
