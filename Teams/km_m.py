km  = int(input("km input: "))
m = km*1000

print("ans in meters is ", m)

m_i = int(input("m input: "))
km_c = m_i//1000
m_c = m_i - (km_c*1000)

print("the answer is: ", km_c, " km and ", m_c, " m")