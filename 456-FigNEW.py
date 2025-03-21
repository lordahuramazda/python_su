import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii


fig=plt.figure(figsize=(8.75,8))
nc_h=[73,73,55,53,29,59]
nc_cr=[89,89,64,67,43,68]
fs=9




plt.subplot(311)
datac3 = ascii.read('C3.txt')
lxc3=datac3['col1'];pc3=datac3['col2'];
datah3 = ascii.read('H3.txt')
lxh3=datah3['col1'];ph3=datah3['col2'];
plt.xlim(31.8,34.2)
plt.ylim(0.0,1.0)
plt.plot(lxh3,(1-ph3),'k',linestyle='dashed',linewidth=1, label='%s normal / non-collapsed GC' % nc_h[2])
plt.plot(lxc3,(1-pc3),'k',linestyle='solid',linewidth=1, label='%s normal / non-collapsed GC' % nc_cr[2])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(31.9, 0.1, '(d)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)


plt.subplot(312)
datac4 = ascii.read('C4.txt')
lxc4=datac4['col1'];pc4=datac4['col2'];
datah4 = ascii.read('H4.txt')
lxh4=datah4['col1'];ph4=datah4['col2'];
plt.xlim(31.5,34.0)
plt.ylim(0.0,1.0)
plt.plot(lxh4,(1-ph4),'k',linestyle='dashed',linewidth=1, label='%s \'in situ\' GC' % nc_h[3])
plt.plot(lxc4,(1-pc4),'k',linestyle='solid',linewidth=1, label='%s \'in situ\' GC' % nc_cr[3])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(31.6, 0.1, '(e)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)


plt.subplot(313)
datac5 = ascii.read('C5.txt')
lxc5=datac5['col1'];pc5=datac5['col2'];
datah5 = ascii.read('H5.txt')
lxh5=datah5['col1'];ph5=datah5['col2'];
plt.xlim(31.6,34.2)
plt.ylim(0.0,1.0)
plt.plot(lxh5,(1-ph5),'k',linestyle='dashed',linewidth=1, label='%s ordinary GC' % nc_h[4])
plt.plot(lxc5,(1-pc5),'k',linestyle='solid',linewidth=1, label='%s ordinary GC' % nc_cr[4])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(31.7, 0.1, '(f)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)





plt.tight_layout()
#fig.savefig('FigNEW_Harris+Cruz_Reyes.pdf')
plt.show()
plt.close(fig)

