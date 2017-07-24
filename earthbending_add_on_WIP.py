import mcpi.minecraft as minecraft
import time
itL = 20 #distance of shot
speed = 0.07#slowness of shot
global width
width = 2#width of shot explosion
mc = minecraft.Minecraft.create()
#zd = 1
#xd = 2
#yd = 3
xl = 0
yl = 0
zl = 0


def move(ifSideHit, blockID):
    global xl,yl,zl
    mc.setBlock(xl, yl, zl, 0)
    if sideHit == 4:
            xl = xl + 1
    elif sideHit == 5:
            xl = xl - 1
    elif sideHit == 0:
            yl = yl + 1
    elif sideHit == 1:
            yl = yl - 1
    elif sideHit == 3:
            zl = zl - 1
    elif sideHit == 2:
            zl = zl + 1
    mc.setBlock(xl, yl, zl, blockID)
    time.sleep(speed)

ahit = False
while True:
    #ahit = True#debug - take away # if you want to only do the block move Forward
    blockEvent = mc.events.pollBlockHits()
    for blockHit in blockEvent:
        if blockHit and ahit == False:
            xl = blockHit.pos.x
            yl = blockHit.pos.y
            zl = blockHit.pos.z
            hittedBlock = mc.getBlockWithData(xl, yl, zl)
            hitBlockID = hittedBlock.id
            mc.setBlock(xl, yl, zl, 0)
            yl = yl + 2
            mc.setBlock(xl, yl, zl, hitBlockID)
            ahit = True
        elif blockHit and ahit == True:
            sideHit = blockHit.face
            #mc.postToChat(sideHit)  #-For Debugging, remove first '#'to see the number corresponding to the side you just hit.
            tL = itL
            while tL > 0:
                move(sideHit, hitBlockID)
                tL = tL - 1
            X2 = xl + width
            Y2 = yl + width
            Z2 = zl + width
            X3 = xl - width
            Y3 = yl - width
            Z3 = zl - width
            mc.setBlocks(X2, Y2, Z2, X3, Y3, Z3, 0)# Add # in front to disable block explosion at the end.
            ahit = False
            
            
            
