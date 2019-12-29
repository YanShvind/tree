import mcpi.minecraft as minecraft
import time
mc = minecraft.Minecraft.create()
import mcpi.block as block



mc.setBlocks(109, 65, 201, 105, 65, 197, 133)
mc.setBlocks(108, 67, 200, 106, 67, 196, 133)
mc.setBlocks(107, 70, 197, 108, 70, 199, 133)
mc.setBlocks(107, 63, 199, 107, 70, 199, 17)
mc.setBlocks(108, 66, 201, 105, 66, 196, 133)
mc.setBlocks(109, 69, 201, 105, 69, 197, 133)



while True:
    mc.setBlock(108, 68, 196, 152)
    time.sleep(0.5)
    mc.setBlock(108, 68, 196, 133)
    time.sleep(0.5)
   
