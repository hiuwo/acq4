from OpenGL.GL import *
from .. GLGraphicsItem import GLGraphicsItem
from pyqtgraph import QtGui
import numpy as np

__all__ = ['GLScatterPlotItem']

class GLScatterPlotItem(GLGraphicsItem):
    """Draws points at a list of 3D positions."""
    
    def __init__(self, data=None):
        GLGraphicsItem.__init__(self)
        self.data = []
        if data is not None:
            self.setData(data)
    
    def setData(self, data):
        """
        Data may be either a list of dicts (one dict per point) or a numpy record array.
        
        ====================  ==================================================
        Allowed fields are:
        ------------------------------------------------------------------------
        pos                   (x,y,z) tuple of coordinate values or QVector3D
        color                 (r,g,b,a) tuple of floats (0.0-1.0) or QColor
        size                  (float) diameter of spot in pixels
        ====================  ==================================================
        """
        
        
        self.data = data
        self.update()

        
    def initializeGL(self):
        def fn(x,y):
            r = ((x-15)**2 + (y-15)**2) ** 0.5
            return 255 * (1.0-(np.clip(r, 13., 14.) - 13.))
        pData = np.empty((30, 30, 4), dtype=np.ubyte)
        pData[:] = 255
        pData[:,:,3] = np.fromfunction(fn, (30, 30), dtype=np.ubyte)
        
        self.pointTexture = glGenTextures(1)
        glActiveTexture(GL_TEXTURE0)
        glEnable(GL_TEXTURE_2D)
        glBindTexture(GL_TEXTURE_2D, self.pointTexture)
        glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, 20, 20, 0, GL_RGBA, GL_UNSIGNED_BYTE, pData)
        glEnable(GL_POINT_SPRITE)
        glTexEnvi(GL_POINT_SPRITE, GL_COORD_REPLACE, GL_TRUE)
        glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP_TO_EDGE)
        glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP_TO_EDGE)
        
    def paint(self):
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
        glEnable( GL_BLEND )
        glEnable( GL_ALPHA_TEST )
        glEnable( GL_POINT_SMOOTH )
        #glDisable( GL_DEPTH_TEST )
        #glEnable(GL_VERTEX_PROGRAM_POINT_SIZE)
        
        glEnable( GL_POINT_SPRITE )
        glHint(GL_POINT_SMOOTH_HINT, GL_NICEST)
        glPointParameterfv(GL_POINT_DISTANCE_ATTENUATION, (1.0, -0.2, 0.0))
        
        glActiveTexture(GL_TEXTURE0)
        glEnable( GL_TEXTURE_2D )
        #glTexEnv(GL_POINT_SPRITE, GL_COORD_REPLACE, GL_TRUE)
        #glTexEnv(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_REPLACE)
        glBindTexture(GL_TEXTURE_2D, self.pointTexture)
    
    
        for pt in self.data:
            pos = pt['pos']
            try:
                color = pt['color']
            except KeyError:
                color = (1,1,1,1)
            try:
                size = pt['size']
            except KeyError:
                size = 10
                
            if isinstance(color, QtGui.QColor):
                color = fn.glColor(color)
                
            glPointSize(size)
            glBegin( GL_POINTS )
            glColor4f(*color)  # x is blue
            #glNormal3f(size, 0, 0)
            glVertex3f(*pos)
            glEnd()

        
        
        
        