# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 21:51:48 2017

@author: subha
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 06 15:00:40 2017

@author: subha
"""

from Drone_Final.road import Road
from Drone_Final.parser import Parser
import numpy as np
import copy
#from djikstar import short_path
from DjikstraFinal import shortestPath

import os
#import math

def distance(v,t,startNode):
    #if the drone is initially cw and final dest also cw
        src=float(v[1])
        dst=float(t[1])
#    if SR!=v[0] and ER!=t[0]:
        if v[0]==t[0] :
            (distance,action,angle,ang1,ang2,time)=ang2Dis(t[0],v[0],dst,src,t[2],v[2],startNode)
            
#            if(v[2]=='+' and t[2]=='+'):
#                angle=dst-src #dest angle - source angle
#                if angle<0:
#                    angle=360+angle
#                distance=(p.getRoadById(v[0]).getRadius())*(angle)*0.017   #dis=(angle*radius*2*pi)/360
#            elif (v[2]=='+' and t[2]=='-'):
#                angle=src-dst #source angle - destination angle for aw
#                if angle<0:
#                    angle=360+angle
#                distance=(p.getRoadById(v[0]).getRadius())*(angle)*0.017+0.069*0.3*(p.getRoadById(v[0]).getRadius())#dis=(angle*radius*2*pi)/360 + distance during .3 seconds(4/360*2*pi*r*0.3 : 4m/s because that is the maximum speed that can be obtained)
#
#            elif (v[2]=='-' and t[2]=='-'):
#                angle=src-dst #source angle - destination angle for aw
#                if angle<0:
#                    angle=360+angle
#                distance=(p.getRoadById(v[0]).getRadius())*(angle)*0.017+0.069*0.3*(p.getRoadById(v[0]).getRadius())
#
#            else:
#
#                angle=dst-src #dest angle - source angle
#                if angle<0:
#                    angle=360+angle
#                distance=(p.getRoadById(v[0]).getRadius())*(angle)*0.017 +0.069*0.3*(p.getRoadById(v[0]).getRadius())

        else: # At intersections
            if(v[2]==t[2]):
                distance=0.1 #transfer without direction change
                action='TRANSFER'
                angle='0'
                ang1=v[0]
                ang2=t[0]
                time=0.1
            else:
                distance=10000000000# you assign a high cost because you do not want it to change direction before transfer
                         # as the direction change will cause high cost
                action='REVERSE-TRANSFER'
                angle='null'
                ang1='null'
                ang2='null'
                time=10000000000
        return (time,distance,action,angle,ang1,ang2)
def ang2Dis(road2,road1,ang2,ang1,dir2,dir1,startNode):

    distance=0
    if dir1=='+' and dir2=='+':
                angle=ang2-ang1 #dest angle - source angle
                if angle<0:
                    angle=360+angle
#                print "angle{0}".format(p.getRoadById(road1).getRadius())
                distance=(p.getRoadById(road1).getRadius())*(angle)*0.01744444 #dis=(angle*radius*2*pi)/360
                if startNode:
                  time=(distance-8)/4 + 4
                else:
                    time=distance/4
                action='GO'
#                print(angle)
    elif dir1=='+' and dir2=='-':
         angle=ang1-ang2 #source angle - destination angle for aw
         if angle<0:
            angle=360+angle
         distance=(p.getRoadById(road1).getRadius())*(angle)*0.01744444
         if not startNode:
                
                
                time = distance/4+4+0.3#dis=(angle*radius*2*pi)/360 + distance during .3 seconds(4/360*2*pi*r*0.3 : 4m/s because that is the maximum speed that can be obtained)
                action='STOP-REVERSE-GO'
         else:
              time=(distance-8)/4 + 4 + 0.3
              action='REVERSE-GO'
            
    elif dir1=='-' and dir2=='-':
                angle=ang1-ang2 #source angle - destination angle for aw
                if angle<0:
                    angle=360+angle
                distance=(p.getRoadById(road1).getRadius())*(angle)*0.01744444  #dis=(angle*radius*2*pi)/360
                if startNode:
                  time=(distance-8)/4 + 4
                else:
                    time=distance/4
                action='GO'
    else:

                angle=ang2-ang1 #dest angle - source angle
                if angle<0:
                    angle=360+angle
                distance=(p.getRoadById(road1).getRadius())*(angle)*0.01744444
                if not startNode:
                    time = distance/4+4+4+0.3#dis=(angle*radius*2*pi)/360 + distance during .3 seconds(4/360*2*pi*r*0.3 : 4m/s because that is the maximum speed that can be obtained)
                    action='STOP-REVERSE-GO'
                else:
                    time=(distance-8)/4 + 4 + 0.3
                    action='REVERSE-GO'
    return (distance,action,angle,ang1,ang2,time)
#def timeCalc(actions,distances):
#  time = []
#  totalTime=0
#  for i in xrange(len(actions)):
##          print "action{0},dist{1}".format(actions[i],distances[i])
##      if (i==0):
#          # First time
#          if actions[i]=='REVERSE-GO':
#              if (i==0):
#                  time.append(((distances[i]-8)/4)+4+0.3)
#                  totalTime+=time[i]
#              else:
#                  
#                  time.append(((distances[i])/4)+4+4+0.3 )#first will deccelerate drone to stop for 4 seconds which will increase distance by 8, then accelerate
#                      #drone to 4m/s for 4 seconds which will compensate for increased 8 m
#              #SHOULD BE BROUGHT TO STOP AND THEN ACCELERATE
#                  
#          elif actions[i]=='GO':
##              print "test"
#              time.append(((distances[i]-8)/4)+4)
#              totalTime+=time[i]
#          elif actions[i]=='TRANSFER':
#              time.append(0.1)
#              totalTime+=time[i]
                 
#  print "time{0},tot{1}".format(time,totalTime)
#  return (time,totalTime)            
                  
def calDistAct(path):
    actions=[]
    distances=[]
    time=[]
    
#    for a in pathGlobal:
#        a=a[::-1]
#    i=len(path)-1
    for i in xrange(len(path)-1):
            actions.append(graphTree[path[i]][path[i+1]][2])
            distances.append(graphTree[path[i]][path[i+1]][1])   
            time.append(graphTree[path[i]][path[i+1]][0])
#            print "time{0}".format(graphTree[path[i]][path[i+1]][2])
#            i-=1
    return (actions,distances,time)
#    for a in path:
#        for i in range(len(a)-1):
#            print(len(a))
#            print "path{0}".format(path)
#
#            ang1=float(''.join(filter(str.isdigit, a[i])))
#            ang2=float(''.join(filter(str.isdigit, a[i+1])))
##            print "ang1{0}".format(ang1)
##            print "ang2{0}".format(ang2)
#            road1=a[i][:1]
#            road2=a[i+1][:1]
#            dir1=a[i][-1:]
#            dir2=a[i+1][-1:]
#            dist=ang2Dis(road1,road2,ang1,ang2,dir1,dir2)
##            print "distance{0}".format(dist)
##            print(road1,road2,dir1,dir2,dist)
#            if(len(a)==2):# only 2 states
#              if dir1!=dir2:
#                  actions.append('REVERSE')
#                  # already in stop state so ne need of deccelerating
#                  time=time+0.3
#                  actions.append('GO')
#                  time+=((dist-8)/4)+4 # second term is the time to accelerate to 4m/s, first term is distance left after the distance covered during acceleration(Dacc=0.5*1*(4*4))
#              else:
#                  time+=((dist-8)/4)+4
#                  actions.append('GO')
#              actions.append('TRANSFER')
#              time+=0.1
#              actions.append('G0')
#            else:# more than two nodes
#                if i==0: #drone starting state
#                  if dir1!=dir2:
#                      actions.append('REVERSE')
#                      # already in stop state so ne need of deccelerating
#                      time=time+0.3
#                      actions.append('GO')
#                      time+=((dist-8)/4)+4 # second term is the time to accelerate to 4m/s, first term is distance left after the distance covered during acceleration(Dacc=0.5*1*(4*4))
#                  else:
#                      time+=((dist-8)/4)+4
#                      actions.append('GO')
#                      if road1!=road2:
#                          actions.append('TRANSFER')
#                          time+=0.1
#                else:#intermediate states
#                    if road1!=road2:
#                          actions.append('TRANSFER')
#                          time+=0.1
#                    elif dir1!=dir2:
#                      actions.append('REVERSE')
#                      # already in stop state so ne need of deccelerating
#                      time=time+0.3
#                      actions.append('GO')
#                      time+=((dist)/4)+4+4+0.3#since intermediate moves an additional distance of
#                      #first will deccelerate drone to stop for 4 seconds which will increase distance by 8, then accelerate
#                      #drone to 4m/s for 4 seconds which will compensate for increased 8 m
#                    else:
#                        actions.append('GO')
#                        time+=(dist/4)
#                    if road1!=road2:
#                          actions.append('TRANSFER')
#                          time+=0.1
#                    actions.append('GO')
#
#    return (actions,time)

if __name__ == "__main__":
    graph={}
    absFilePath = os.path.abspath("./input.txt")
    p = Parser(absFilePath)
    roadsAndDrone = p.parse()
    #roads, drone = roadsAndDrone['roads'], roadsAndDrone['drone']
    roads, drone = roadsAndDrone['roads'], roadsAndDrone['drone']
    startRoad=drone.getSource()
    endRoad=drone.getDestination()
    Nodes=[]
    nodeGraph={}
    newNodes=[]
    newNodes=Nodes
    for roadId in roads:
        #print "roadId{0}".format(roadId)
        temp=[]
        intersDict={}
        road = p.getRoadById(roadId)
        
#        print "{0}\t{1}\t{2}".format(road.getId(), road.getRadius(), road._intersections)
        for key,values in road._intersections.items():
#            print "values{0}\key{1}".format(values,key)
#            print "---------------------------"
            for i in ['+','-']:
#           
                node=(roadId,key,i)
                Nodes.append(node)
                new_vals=[]
                for tup in values:
                    for j in ['+','-']:
                        new_vals.append(tup+(j,))
#                print "\tup {0}\tnode{1}".format(new_vals,node)
#                print "---------------------------"
                nodeGraph[node]=new_vals
#    for roadId in roads:
#        road = p.getRoadById(roadId)
#        for key,values in road._intersections.items():
#            for i in ['+','-']:
                
            
        
    for n in Nodes:
        for n1 in Nodes:
            if n1[0]==n[0] and n1[1]!=n[1]:
                nodeGraph[n].append(n1)
                np.unique(nodeGraph[n])
#        print "n{0}: NodeGraph{1}".format(n,nodeGraph[n])
#        print "------------------------------------------------"
    

#    nodeGraph[(startRoad['road'].getId(),startRoad['pos'],startRoad['direction'])]=startInters
    SR=(startRoad['road'].getId(),startRoad['pos'],startRoad['direction'])
    ER1=(endRoad['road'].getId(),endRoad['pos'],'+')
    ER2=(endRoad['road'].getId(),endRoad['pos'],'-')
    ER=[]
    ER.append(ER1)
    ER.append(ER2)
#    endNodes=[]
#    for i in ['+','-']:
#        temp=(endRoad['road'].getId(),endRoad['pos'],i)
##        endNodes.append(temp)
#        if temp in Nodes:
#            nodeGraph[temp]=endInters

    if SR not in Nodes:
        startInters=[]
        
        for tuple in Nodes:
    #        print "tuple{0}".format(tuple)
    #        print "startRoad{0}".format(startRoad['road'])
                if tuple[0]==startRoad['road'].getId():
                    startInters.append(tuple)
                    nodeGraph[tuple].append(SR)
        nodeGraph[SR]=startInters
    if ER1 and ER2 not in Nodes:

        endInters=[]
#        if ER1 not in Nodes:
        for tuple in Nodes:
                if tuple[0]==endRoad['road'].getId():
                    endInters.append(tuple)
                    nodeGraph[tuple].append(ER1)
                    nodeGraph[tuple].append(ER2)
        
#        elif ER2 not in Nodes:
#             for tuple in Nodes:
#                if tuple[0]==endRoad['road'].getId():
#                    endInters.append(tuple)
        nodeGraph[ER1]=endInters
        nodeGraph[ER2]=endInters
        
    
    graphTree={}
#    print "nodegraph{0}".format(nodeGraph[('B','80','+')])
#    print "int{0}".format(Nodes)
#    for n in Nodes:
#        print "n{0}: NodeGraph{1}".format(n,nodeGraph[n])
#        print "------------------------------------------------"
#        
    for startKey,endValues in nodeGraph.items():
        intersDict={}
        if SR== startKey:
            startNode=1
        else:
            startNode=0
        for t in endValues:
            
            
          
            intersDict[''.join((t))]=distance(startKey,t,startNode)
    
        a=''.join(startKey)
        if intersDict.has_key(a):
            del intersDict[a]
        graphTree[a]=intersDict
    
#    print "gt{0}".format(graphTree)
#        del
#    print "FinalTreenow{0}".format(graphTree['B0+'])
#        print "---------------------------------"
    
    #Structure of Tree: where every node consists of the road it is on, the position angle and the orientation of the drone
    #FinalTree{'A355+': {'A180+': 0.1, 'C0+': 3060.0, 'C0-': 3080.7, 'A180-': 10000000000L, '
    #C180-': 0.1, 'B0-': 20.7, 'E180-': 13863.150000000001, 'E180+': 13863.150000000001, 'C180+': 10000000000L, 'A0+': 0.1, 'E0-': 93.14999999999999, 'E0+':
    startString=''.join((startRoad['road'].getId(),startRoad['pos'],startRoad['direction']))
    
    
    #since the direction of destination is known, the distance to both clockwise and anti-clockwise 
    # is calculated and the least is chosen
    endString=''.join((endRoad['road'].getId(),endRoad['pos'],'+'))
    endString1=''.join((endRoad['road'].getId(),endRoad['pos'],'+'))
    endString2=''.join((endRoad['road'].getId(),endRoad['pos'],'-'))
    path1=shortestPath(graphTree,startString,endString1)
#    print Nodes
    path2= shortestPath(graphTree,startString,endString2)
#    print path1
#    print path2
#    path1 = pathGlobal[0]
#    path2= pathGlobal[1]
#    print path1
#    print path2
#    pathGlobal=[]
    (actions1,distances1,times1)=calDistAct(path1)
###    for i in pathGlobal:
###        del i
##    print(actions1,distances1,times1)
###    dijkstra(graphTree,startString,endString2)
###    print pathGlobal
    (actions2,distances2,times2)=calDistAct(path2)
###    print pathGlobal
#    print (actions2,distances2,times2)
##    for i in distances1
    time1=sum(times1)
    time2=sum(times2)
#    print time1
#    print time2
    if time1<time2:
        time=time1
        distances=distances1
        actions=actions1
        times=times1
        print "The path followed was {0}:".format(path1)
    else:
        time=time2
        distances=distances2
        actions=actions2
        times=times2
        print "The path followed was :{0}".format(path2)
    
    
#    print(pathGlobal)
   
#    (time,totalTime)=timeCalc(actions,distances)       
##    print "finalActions{0},Distances{1}".format(actions,distances)
    print "TotalTime:{0}\n".format(time)
    for i in xrange(len(actions)):
        print "Action: {0} time :{1} ".format(actions[i],times[i])
   
    
