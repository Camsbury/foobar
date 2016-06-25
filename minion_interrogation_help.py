#Doing some testing for minion_interrogation
def timeit(Ta,Pa,Tb,Pb,Tc,Pc):
    
    return Ta*Pa+(1-Pa)*Pb*(Ta+Tb)+(1-Pa)*(1-Pb)*(Ta+Tb+Tc)