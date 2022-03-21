cmake_minimum_required(VERSION 3.1.3)
project(mesh_rviz)

find_package(catkin REQUIRED)

catkin_package()
catkin_python_setup()

catkin_install_python(PROGRAMS
  scripts/publish_mesh
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
