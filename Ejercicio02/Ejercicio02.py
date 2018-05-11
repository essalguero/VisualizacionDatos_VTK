import vtk
from vtk import *

#Create a camera
camera = vtkCamera()
camera.SetPosition(0, 0, 4)

#Create a renderer
renderer = vtk.vtkRenderer()
renderer.SetActiveCamera(camera)
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


# create a transform with the rotation info of the cone
transform = vtk.vtkTransform()
transform.RotateX(30)

transformFilter = vtk.vtkTransformPolyDataFilter()
transformFilter.SetTransform(transform)
transformFilter.SetInputConnection(cylinder.GetOutputPort())
transformFilter.Update()

# mapper for original cone
cylinder_mapper = vtk.vtkPolyDataMapper()
cylinder_mapper.SetInputConnection(transformFilter.GetOutputPort())

# actor for original cone
cylinder_actor = vtk.vtkActor()
cylinder_actor.SetMapper(cylinder_mapper)

#Set the color
cylinder_actor.GetProperty().SetDiffuseColor(1.0, 0, 0)
cylinder_actor.GetProperty().SetSpecular(0.5) 	
cylinder_actor.GetProperty().SetLighting(True)

# assign actor to the renderer
renderer.AddActor(cylinder_actor)

# enable user interface interactor
interactor.Initialize()
renderer_window.Render()
interactor.Start()