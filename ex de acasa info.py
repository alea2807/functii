x,y,z = int(input("numarul 1= ")), int(input("numarul 2= ")), int(input("numarul 3= "))
#a)`cel mai mare divizor comun`
div=[]
def div_maxim(a,b,c):
    n=0
    for i in range(1, min(a, b, c)+1):
        if a%i==b%i==c%i==0:
            n+=1
            div.append(i)
div_maxim(x,y,z)
print("cel mai mare divizor comun= ",div[-1])

#b) cel mai mic multiplu comun
listaMultiplelor=[]
def multiples(a,b,c):
    maxDin3 = max(a,b,c)
    for j in range(1, 500):
        multiplul=j*maxDin3
        if ((multiplul%a==0) and (multiplul%b==0) and (multiplul%c==0)):
           listaMultiplelor.append(multiplul)
    return listaMultiplelor

print('cel mai mic multiplu comun=',min(multiples(x,y,z)))

#c) Numarul minim
def minimul(a,b,c):
    if ((a<b) and (a<c)):
        min=a
    if ((b<a) and (b<c)):
        min=b
    if ((c<b) and (c<a)):
        min=c
    return min
print("minimul= ", minimul(x,y,z))

#d) Numarul maxim
def maximul(a,b,c):
    if ((a>b) and (a>c)):
        max=a
    if ((b>a) and (b>c)):
        max=b
    if ((c>b) and (c>a)):
        max=c
    return max
print("maximul= ",maximul(x,y,z))

#e) Toti divizorii comuni
divizori=[]
def totidivizorii(a, b, c):
    for i in range(1, min(a,b,c) + 1):
        if a%i==b%i==c%i== 0:
            divizori.append(i)
    return divizori 
print("toti divizorii comuni= ",totidivizorii(x,y,z))

#f) cei mai mici 3 multipli comuni
#am definit functia generala in punctul b
print('3 multipli comuni:',multiples(x,y,z)[0],',',multiples(x,y,z)[1],',',multiples(x,y,z)[2])

#g1) verif daca laturile pot forma triunghi + aria lui
def triunghi_aria(a,b,c):
    if (a+b)>c:
        s = (a + b +c)/2
        aria=((s*(s-a)*(s-b)*(s-c))**0.5)
    if (a+b)<=c:
        print('aceste laturi nu pot forma triunghi')
    return aria
print('aria triunghiului este= ', triunghi_aria(x,y,z))

#g2) verif daca laturile pot forma triunghi + perimetru
def triunghi_perim(a,b,c):
    if (a+b)>c:
        perimetru = (a + b + c)
    if (a+b)<=c:
        print('aceste laturi nu pot forma triunghi')
    return perimetru
print('perimetrul este= ', triunghi_perim(x,y,z))

#h) se va afisha sol reala a ec daca a,b,c sunt coeficientii ei
def ecuatie(a,b,c):
    d=((b**2)-(4*a*c))
    if d<0:
        print('a,b,c nu sunt coeficienti ai ecuatiei')
        solutie=()
    if d==0:
        k=((-1)*b)//(2*a)
        solutie=k
    if d>0:
        m=(((-1)*b)+(d**0.5))//2
        n=(((-1)*b)-(d**0.5))//2
        solutie=m,n
    return solutie
print('solutiile ecuatiilor sunt= ',ecuatie(x,y,z))