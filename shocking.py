#Basic shock calculator.
import numpy as np

print('Is it an oblique shockwave (O), normal shockwave (N), or expansion fan (E)?')
mod = input()
check = 0
while True:
    if mod == 'O' or mod == 'N' or mod == 'E':
        break
    else:
        print('Please input either O, N, or E.')
        mod = input()

#Change below to 1 if you want to be asked for a specific heat ratio.
gacheck = 1
if gacheck == 0:
    ga = 1.4
else:
    print('What is specific heat?')
    while True:
        try:
            ga = float(input())
        except:
            print('Please insert a number.')
        else:
            break

print('What is your mach number?')
while True:
    try:
        mach = float(input())
    except:
        print('Please insert a number.')
    else:
        if mach > 1:
            break
        else:
            print('Please insert a mach number greater than one.')
            
if mod == 'O':
    print('What is shock angle (degrees)?')
    while True:
        try:
            ang = float(input())
        except:
            print('Please insert a number.')
        else:
            break
    angle = np.deg2rad(ang)
    data = oblique(mach,ga,angle)
elif mod == 'N':
    data = normal(mach,ga)
else:
    print('Haven\'t gotten around to coding expansion fan yet, sorry.')

def normal(m,g):
    p1 = (2*g*m**2-(g-1))/(g+1)
    pt1 = ((g+1)*m**2/((g-1)*m**2+2))**(g/(g-1))*((g+1)/(2*g*m**2-(g-1)))**(1/(g-1))
    t1 = ((2*g*m**2-(g-1))*((g-1)*m**2+2))/((g+1)**2*m**2)
    rho1 = ((g+1)*m**2)/((g-1)*m**2+2)
    m1 = (((g+1)*m**2+2)/(2*g*m**2-(g-1)))**0.5
    data = [p1,pt1,t1,rho1,m1]
    return data

def oblique(m,g,a):
    #nixing the idea of wvs and a choice for now, but could be an
    #interesting problem to return to. iteration? angles in radians.
    s = np.pi/2 - np.arctan(np.tan(a)*(((g+1)*m**2)/(2*(m**2*(np.sin(a))**2+2))-1)) 
    p1 = (2*g*m**2*np.sin(s)**2-(g-1))/(g+1)
    #Another way I could streamline in future is by paring the
    #g + 1 and m**2*np.sin etc phrases down. 
    t1 = (2*g*m**2*np.sin(s)**2-(g-1))*((g-1)*m**2*np.sin(s)**2+2)/((g+1)**2*m**2*np.sin(s)**2)
    #a and b are just labels for splitting into two parts
    pta = (((g+1)*m**2*np.sin(s)**2)/((g-1)*m**2*np.sin(s)**2+2))**(g/(g-1))
    ptb = ((g+1)/(2*g*m**2*np.sin(s)**2-(g-1)))**(1/(g-1))
    pt1 = pta*ptb
    rho1 = ((g+1)*m**2*np.sin(s)**2)/((g-1)*m**2*np.sin(s)**2+2)
    #I'd say divisor for m1 looks ugly but they're all ugly actually.
    mdiv = np.sin(s-a)**2*(2*g*m**2*np.sin(s)**2-(g-1))
    m1 = (((g-1)*m**2*np.sin(s)**2+2)/mdiv)**0.5
    data = [p1,pt1,t1,rho1,m1]
    return data

#def expansion():