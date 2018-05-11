from vtk import *

coneSource = vtkConeSource()
coneSource.SetResolution(20)

mapper = vtkPolyDataMapper()
mapper.SetInputConnection(coneSource.GetOutputPort())

actor = vtkActor()
actor.SetMapper(mapper)
actor.GetProperty().SetDiffuseColor(1.0, 0, 0)

actor.RotateX(45)
actor.RotateY(-30)


#Rotar el Cono


renderer = vtkRenderer()
renderer.AddActor(actor)
renderer.SetBackground(0,0,0.5)

renderer.ResetCamera()
renderer.GetActiveCamera().Zoom(1.5)

renderWindow = vtkRenderWindow()
renderWindow.AddRenderer(renderer)
renderWindow.SetSize(640, 480)

renderWindowInteractor  = vtkRenderWindowInteractor()
renderWindowInteractor.SetRenderWindow(renderWindow)
renderWindowInteractor.Start()