from subsystems import driveCommands, relays
import board

drive = driveCommands.analogDrive()
r1 = relays.Standard(board.D6)
r2 = relays.Standard(board.D13)
r3 = relays.Standard(board.D19)
r4 = relays.Standard(board.D26)

drive.tank(0)
