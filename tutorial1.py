from qutip import *

# #creating and inspecting quantum objects
# #to do so we use the QObj class
# q = Qobj([[1], [0]])
# #print(q) output looks like this:
# '''
# [[ 1.]
#  [ 0.]]
# '''
# # this is a metrix representation of a quantum object
# #printing dimesions of the object:
# print(q.dims)
# # output: 
# '''[[2], [1]]'''
# print(q.shape)
# # output:
# '''(2, 1)'''
# print(q.data) #printing sparse matrix object
# # output:
# '''(0, 0)	(1+0j)'''
# print(q.full()) # the dense matrix representation
# # output:
# '''[[ 1.+0.j]
#     [ 0.+0.j]]'''
# print(q.isherm, q.type) # 'some additional properties' (isherm= is hermetian)
# #output:
# '''(False, 'ket')'''

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

# generalized pauli matrices in Quantum mechanics
	# these refer to families of matrices which generalize the (linear algerbraic) properties
	# of the Pauli matrices. 
	# Pauli matrices:	
		# a set of three 2x2 complex matrices which are 'hermetian' and 'unitary'
		# In quantu,, they occur in the Pauli equation, which takes into account the 
			# interaction of the spin of a particle with an external electromagnetic field
# a sigma-z Pauli operator
sz = Qobj([[1,0], [0,-1]])
print(sz)
# output:
'''
Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
Qobj data =
[[ 1.  0.]
 [ 0. -1.]]
'''

# some arithmetic with quantum objects 
H = 1.0 * sz + 0.1 * sy
print("Qubit Hamiltonian = {}\n".format(H))
# output:
'''
Qubit Hamiltonian = Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
Qobj data =
[[ 1.+0.j   0.-0.1j]
 [ 0.+0.1j -1.+0.j ]]
'''

#Example of modifying quantum objects using the Qobj methods:
