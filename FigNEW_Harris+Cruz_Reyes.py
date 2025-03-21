import numpy as np
import matplotlib.pyplot as plt
from astropy.io import ascii


fig=plt.figure(figsize=(8.75,8))
nc_h=[73,73,55,53,29,59]
nc_cr=[89,89,64,67,43,68]
fs=9

plt.subplot(321)
datac1 = ascii.read('C1.txt')
lxc1=datac1['col1'];pc1=datac1['col2'];
datah1 = ascii.read('H1.txt')
lxh1=datah1['col1'];ph1=datah1['col2'];
plt.xlim(31.7,34.1)
plt.ylim(0.0,1.0)
plt.plot(lxh1, ph1,'c',linestyle='solid',linewidth=1, label='%s GC \n(Harris 2010)' % nc_h[0])
plt.plot(lxc1, (1-pc1),'r',linestyle='solid',linewidth=1, label='%s GC \n(Cruz Reyez 2024)' % nc_cr[0])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs, loc=1)
#adding text inside the plot
plt.text(31.8, 0.1, '(a)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)
#plt.text(31.8, 0.04, '73 GC (Harris 2010)', fontsize = 10, color = 'c', bbox = dict(facecolor = 'white', edgecolor='white', alpha = 1.0), zorder=2)
#plt.text(31.8, 0.16, '89 GC (Cruz-Reyez 2024)', fontsize = 10, color = 'r', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=3)


plt.subplot(322)
datac2 = ascii.read('C2.txt')
lxc2=datac2['col1'];pc2=datac2['col2'];
datah2 = ascii.read('H2.txt')
lxh2=datah2['col1'];ph2=datah2['col2'];
plt.xlim(31.3,34.4)
plt.ylim(0.0,1.0)
plt.plot(lxh2,(1-ph2),'c',linestyle='solid',linewidth=1, label='%s GC' % nc_h[1])
plt.plot(lxc2,(1-pc2),'r',linestyle='solid',linewidth=1, label='%s GC' % nc_cr[1])
plt.xlabel('log $L_{\mathrm{X}}$ ($M_{\mathrm{V}}$=-7 mag) [erg/s] (this work)')
plt.ylabel('probability')
plt.legend(fontsize=fs, loc=5)
#adding text inside the plot
plt.text(31.4, 0.1, '(b)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)


plt.subplot(323)
datac3 = ascii.read('C3.txt')
lxc3=datac3['col1'];pc3=datac3['col2'];
datah3 = ascii.read('H3.txt')
lxh3=datah3['col1'];ph3=datah3['col2'];
plt.xlim(31.8,34.2)
plt.ylim(0.0,1.0)
plt.plot(lxh3,(1-ph3),'c',linestyle='solid',linewidth=1, label='%s normal / non-collapsed GC' % nc_h[2])
plt.plot(lxc3,(1-pc3),'r',linestyle='solid',linewidth=1, label='%s normal / non-collapsed GC' % nc_cr[2])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(31.9, 0.1, '(c)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)


plt.subplot(324)
datac4 = ascii.read('C4.txt')
lxc4=datac4['col1'];pc4=datac4['col2'];
datah4 = ascii.read('H4.txt')
lxh4=datah4['col1'];ph4=datah4['col2'];
plt.xlim(31.5,34.0)
plt.ylim(0.0,1.0)
plt.plot(lxh4,(1-ph4),'c',linestyle='solid',linewidth=1, label='%s \'in situ\' GC' % nc_h[3])
plt.plot(lxc4,(1-pc4),'r',linestyle='solid',linewidth=1, label='%s \'in situ\' GC' % nc_cr[3])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(31.6, 0.1, '(d)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)


plt.subplot(325)
datac5 = ascii.read('C5.txt')
lxc5=datac5['col1'];pc5=datac5['col2'];
datah5 = ascii.read('H5.txt')
lxh5=datah5['col1'];ph5=datah5['col2'];
plt.xlim(31.6,34.2)
plt.ylim(0.0,1.0)
plt.plot(lxh5,(1-ph5),'c',linestyle='solid',linewidth=1, label='%s ordinary GC' % nc_h[4])
plt.plot(lxc5,(1-pc5),'r',linestyle='solid',linewidth=1, label='%s ordinary GC' % nc_cr[4])
plt.xlabel('log $L_{\mathrm{X}}}$ [erg/s] (Botev et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(31.7, 0.1, '(e)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)


plt.subplot(326)
datac6 = ascii.read('C6.txt')
lxc6=datac6['col1'];pc6=datac6['col2'];
datah6 = ascii.read('H6.txt')
lxh6=datah6['col1'];ph6=datah6['col2'];
plt.xlim(32.4,33.5)
plt.plot(lxh6,(1-ph6),'c',linestyle='solid',linewidth=1, label='%s GC' % nc_h[5])
plt.plot(lxc6,(1-pc6),'r',linestyle='solid',linewidth=1, label='%s GC' % nc_cr[5])
plt.xlabel('log $L_{\mathrm{X}}$ [erg/s] (Cheng et al. 2024)')
plt.ylabel('probability')
plt.legend(fontsize=fs)
#adding text inside the plot
plt.text(32.45, 0.1, '(f)', fontsize = 12, color = 'k', bbox = dict(facecolor = 'white',  edgecolor='white', alpha = 1.0), zorder=1)



plt.tight_layout()
#fig.savefig('FigNEW_Harris+Cruz_Reyes.pdf')
plt.show()
plt.close(fig)

