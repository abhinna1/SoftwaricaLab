'''You live 4 miles from university. The bus drives at 25mph but spends 2 minutes at each of the 10 stops on the way.
How long will the bus journey take? Alternatively, you could run to university. You jog the first mile at 7mph; then
run the next two at 15mph; before  jogging the last at 7mph again. Will this be quicker or slower than the bus?'''


distanceFromUni=4#m

busSpeed=25#mph
busPerStop = 2/60#hours

#when in bus
busTimeInStops = busPerStop*10
finalTimeInBus = (distanceFromUni/busSpeed)+busTimeInStops
print('time taken to reach university in bus is ',finalTimeInBus)


#when jogging
speedFirstMile=7
speedSecondMile=15
speedThirdMile=15
speedFouthMile=7
joggingSpeed=speedFirstMile+speedSecondMile+speedThirdMile+speedFouthMile
joggingTime = distanceFromUni/joggingSpeed

#output generating
print('you take ',finalTimeInBus,'hours in bus')
print('you take ',joggingTime,'hours jogging')
if finalTimeInBus>joggingTime:
    print('You reach faster in bus')
else:
    print('You reach faster jogging')