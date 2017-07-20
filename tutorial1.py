from qutip import *

#creating and inspecting quantum objects
#to do so we use the QObj class
q = Qobj([[1], [0]])
#print(q) output looks like this:
'''
[[ 1.]
 [ 0.]]
'''
# this is a metrix representation of a quantum object
#printing dimesions of the object:
print(q.dims)
# output: 
'''[[2], [1]]'''
print(q.shape)
# output:
'''(2, 1)'''
print(q.data) #printing sparse matrix object
# output:
'''(0, 0)	(1+0j)'''
print(q.full()) # the dense matrix representation
# output:
'''[[ 1.+0.j]
    [ 0.+0.j]]'''
print(q.isherm, q.type) # 'some additional properties'
#output:
'''(False, 'ket')'''

#Using Qobj instances for calculations
sy = Qobj([[0, -1j], [1j, 0]])
print(sy)
#output:
'''
Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
Qobj data =
[[ 0.  -1.j]
 [ +1.j  0.]]
'''

