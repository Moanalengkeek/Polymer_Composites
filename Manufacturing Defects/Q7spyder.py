# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 17:13:26 2024

@author: coenh

When infusing a part with resin, it is important to understand the difference between the capillary forces and the viscous forces driving the resin through the fibres. The capillary number is defined as the ration between the viscous forces and the capillary forces, i.e.

$$Ca = \frac{v\eta}{\gamma_a}$$

where $v$ is the resin flow velocity, $\nu$ is the viscosity of the resin and $\gamma_a$ is the surface tension of the resin. If the capillary number is <<1, the viscous forces are dominated by the capillary forces within the resin, thus mostly capillary flow will take place in the infusion. These forces are most present within the fibre tows, and way less within the "empty" channels in between the tows. Thus the resin flow front will advance more easily along the fibre tows, and lag behind in the channels. This can create voids within the channels as air can get trapped as the capillary flow surrounds the channel before it has properly infused itself. 

In case of a higher capillary number, the opposite is hapenning, namely that the viscous forces dominate within the resin, and thus it flows much easier along the channels within the fabric, and lags behind along the tows, where it is mainly dependent on capillary force. Voids are easier formed within the tows. 

In terms of flow properties, one wants to balance the viscous and capillary forces on the resin front, in order to have a balanced flow front in terms of speed of the resin along the tows/fibres and within the channels between tows. As shown in figure 7 above, there is an optimum capillary number at which the balance between capillary and viscous forces result in a minimum void content. As explained earlier, a capillary flow dominated infusion might lead to intra-tow void, i.e. in the channels, and a viscous dominated flow can result in poor tow infusion. 

As one wants to minimise void content within the part in order to ensure the final part reaches it's optimum mechanical properties, there is not one type of flow that is preferred over the other, but rather a carefull balance between capillary flow and viscous flow in order to minimise void formation.

"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


plt.close('all')

# Sample dimensions
Area1 = 322.58 #mm^2

file = pd.ExcelFile('weld1.xls')
sample1 = pd.read_excel(file,'sample1').to_numpy()
strain1 = sample1[2:,0]
force1  = sample1[2:,1]
stress1 = force1/Area1

sample2 = pd.read_excel(file,'sample2').to_numpy()
strain2 = sample2[2:,0]
force2  = sample2[2:,1]
stress2 = force2/Area1

sample4 = pd.read_excel(file,'sample4').to_numpy()
strain4 = sample4[2:,0]
force4  = sample4[2:,1]
stress4 = force4/Area1

sample5 = pd.read_excel(file,'sample5').to_numpy()
strain5 = sample5[2:,0]
force5  = sample5[2:,1]
stress5 = force5/Area1

sample6 = pd.read_excel(file,'sample6').to_numpy()
strain6 = sample6[2:,0]
force6  = sample6[2:,1]
stress6 = force6/Area1

plt.figure()
plt.plot(strain1,stress1,'b',label='Dataset 1')
plt.plot(strain2,stress2,'b')
plt.plot(strain4,stress4,'b')
plt.plot(strain5,stress5,'b')
plt.plot(strain6,stress6,'b')

file = pd.ExcelFile('weld2.xls')
sample1 = pd.read_excel(file,'sample1').to_numpy()
strain1 = sample1[2:,0]
force1  = sample1[2:,1]
stress1 = force1/Area1

sample2 = pd.read_excel(file,'sample2').to_numpy()
strain2 = sample2[2:,0]
force2  = sample2[2:,1]
stress2 = force2/Area1

sample4 = pd.read_excel(file,'sample4').to_numpy()
strain4 = sample4[2:,0]
force4  = sample4[2:,1]
stress4 = force4/Area1

sample5 = pd.read_excel(file,'sample5').to_numpy()
strain5 = sample5[2:,0]
force5  = sample5[2:,1]
stress5 = force5/Area1

sample6 = pd.read_excel(file,'sample6').to_numpy()
strain6 = sample6[2:,0]
force6  = sample6[2:,1]
stress6 = force6/Area1


plt.plot(strain1,stress1,'r',label='Dataset 2')
plt.plot(strain2,stress2,'r')
plt.plot(strain4,stress4,'r')
plt.plot(strain5,stress5,'r')
plt.plot(strain6,stress6,'r')

plt.xlabel(r"Strain in %")
plt.ylabel(r"Stress in MPa")
plt.legend()
plt.grid()
plt.title('Dataset 1')
plt.show()