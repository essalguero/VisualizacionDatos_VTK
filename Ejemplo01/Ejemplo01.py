import vtk
from vtk import *

cone = vtk.vtkConeSource()

cone_mapper = vtk.vtkPolyDataMapper()
cone_mapper.SetInputConnection(cone.GetOutputPort())

cone_actor = vtk.vtkActor()
cone_actor.SetMapper(cone_mapper)

renderer = vtk.vtkRenderer()
renderer.AddActor(cone_actor)

renderer_window = vtk.vtkRenderWindow()
renderer_window.SetWindowName("Ejercicio 01")
renderer_window.SetSize (800, 600)
renderer_window.AddRenderer(renderer)

interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(renderer_window)
interactor.Initialize()
interactor.Start()