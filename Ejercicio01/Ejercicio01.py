import vtk
from vtk import *

#Create a renderer
renderer = vtk.vtkRenderer()
renderer.SetBackground(0,0,0.5)

#Create a window
renderer_window = vtk.vtkRenderWindow()
renderer_window.SetWindowName("Ejercicio 01")
renderer_window.SetSize (800, 600)
renderer_window.AddRenderer(renderer)

# create a renderwindowinteractor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderer_window)

# create cone
cone = vtk.vtkConeSource()
cone.SetResolution(20)

# mapper for original cone
cone_mapper = vtk.vtkPolyDataMapper()
cone_mapper.SetInputConnection(cone.GetOutputPort())

# actor for original cone
cone_actor = vtk.vtkActor()
cone_actor.SetMapper(cone_mapper)
cone_actor.RotateX(45)
cone_actor.RotateY(-30)

#Set the color
cone_actor.GetProperty().SetDiffuseColor(1.0, 0, 0)

# assign actor to the renderer
renderer.AddActor(cone_actor)

renderer.ResetCamera()
renderer.GetActiveCamera().Zoom(1.5)

# enable user interface interactor
interactor.Initialize()
renderer_window.Render()
interactor.Start()