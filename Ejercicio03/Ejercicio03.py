import vtk

from vtk import *

import numpy as np



class MyInteractorStyle(vtk.vtkInteractorStyleTrackballCamera):

 

    def __init__(self,parent=None):
        self._parent = parent
        #print("Created parent")
        #print(self._parent)
        self.AddObserver("LeftButtonPressEvent",self.leftButtonPressEvent)


    def leftButtonPressEvent(self, obj, event):
        #print("Event generated")
        colorVector = np.random.rand(3,1)
        #print(colorVector)
        self._parent.GetProperty().SetDiffuseColor(colorVector[0], colorVector[1], colorVector[2])
        self.OnLeftButtonDown()
        return



np.random.seed()

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

#Set the color
#Set the color
cylinder_actor.GetProperty().SetDiffuseColor(1.0, 0, 0)
cylinder_actor.GetProperty().SetDiffuse(.7)
cylinder_actor.GetProperty().SetSpecular(0.2)
cylinder_actor.GetProperty().SetSpecularColor(1.0, 1.0, 1.0)
cylinder_actor.GetProperty().SetLighting(True)

# assign actor to the renderer
renderer.AddActor(cylinder_actor)
renderer.ResetCamera()


# enable user interface interactor
interactor.SetInteractorStyle(MyInteractorStyle(cylinder_actor))
interactor.Initialize()
renderer_window.Render()
interactor.Start()