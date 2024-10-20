
def left_rotate(self, x):
    y=x.right
    z=y.left
    p=x.parent

    #link x and z
    x.right=z
    if z != self.NIL:
        z.parent=x
    
    # link y and p
    y.parent=p
    if p==None:
        y = self.root
    #check p's child
    elif p.left==x:
        p.left=y
    else:
        p.right=y
    
    # link x and y
    x.parent=y
    y.left=x


