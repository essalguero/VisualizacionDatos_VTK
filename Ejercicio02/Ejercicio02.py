import vtk
from vtk import *


#Create a renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0,0,0.3)

#Create a window
renderer_window = vtk.vtkRenderWindow()
renderer_window.SetWindowName("Ejercicio 02")
renderer_window.SetSize (800, 600)
renderer_window.AddRenderer(renderer)

# create a renderwindowinteractor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderer_window)

# create cylinder
cylinder = vtk.vtkCylinderSource()
cylinder.SetResolution(20)
#cylinder.SetCenter(0, -1.5, -2.5)


# mapper for original cone
cylinder_mapper = vtk.vtkPolyDataMapper()
cylinder_mapper.SetInputConnection(cylinder.GetOutputPort())

# actor for original cone
cylinder_actor = vtk.vtkActor()
cylinder_actor.SetMapper(cylinder_mapper)
cylinder_actor.RotateX(30)

properties = cylinder_actor.GetProperty()
properties.SetDiffuse(0.7)
properties.SetSpecular(1)
properties.SetSpecularPower(7)
#Set the color
#cylinder_actor.SetProperty(properties)
cylinder_actor.GetProperty().SetDiffuseColor(1.0, 0, 0)

# assign actor to the renderer
renderer.AddActor(cylinder_actor)

renderer.ResetCamera()

# enable user interface interactor
interactor.Initialize()
renderer_window.Render()
interactor.Start()