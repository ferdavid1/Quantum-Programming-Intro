from qutip import *

# # #creating and inspecting quantum objects
# # #to do so we use the QObj class
# # q = Qobj([[1], [0]])
# # #print(q) output looks like this:
# # '''
# # [[ 1.]
# #  [ 0.]]
# # '''
# # # this is a metrix representation of a quantum object
# # #printing dimesions of the object:
# # print(q.dims)
# # # output: 
# # '''[[2], [1]]'''
# # print(q.shape)
# # # output:
# # '''(2, 1)'''
# # print(q.data) #printing sparse matrix object
# # # output:
# # '''(0, 0)	(1+0j)'''
# # print(q.full()) # the dense matrix representation
# # # output:
# # '''[[ 1.+0.j]
# #     [ 0.+0.j]]'''
# # print(q.isherm, q.type) # 'some additional properties' (isherm= is hermetian)
# # #output:
# # '''(False, 'ket')'''

# #Using Qobj instances for calculations
# sy = Qobj([[0, -1j], [1j, 0]])
# print(sy)
# #output:
# '''
# Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
# Qobj data =
# [[ 0.  -1.j]
#  [ +1.j  0.]]
# '''

# # generalized pauli matrices in Quantum mechanics
# 	# these refer to families of matrices which generalize the (linear algerbraic) properties
# 	# of the Pauli matrices. 
# 	# Pauli matrices:	
# 		# a set of three 2x2 complex matrices which are 'hermetian' and 'unitary'
# 		# In quantu,, they occur in the Pauli equation, which takes into account the 
# 			# interaction of the spin of a particle with an external electromagnetic field
# # a sigma-z Pauli operator
# sz = Qobj([[1,0], [0,-1]])
# print(sz)
# # output:
# '''
# Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
# Qobj data =
# [[ 1.  0.]
#  [ 0. -1.]]
# '''

# # some arithmetic with quantum objects 
# H = 1.0 * sz + 0.1 * sy
# print("Qubit Hamiltonian = {}\n".format(H))
# # output:
# '''
# Qubit Hamiltonian = Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
# Qobj data =
# [[ 1.+0.j   0.-0.1j]
#  [ 0.+0.1j -1.+0.j ]]
# '''

# #Examples of modifying quantum objects using the Qobj methods:

# # the Hermetian conjugate 
# print(sy.dag())
# #output:
# '''
# Quantum object: dims = [[2], [2]], shape = (2, 2), type = oper, isherm = True
# Qobj data =
# [[ 0.+0.j  0.-1.j]
#  [ 0.+1.j  0.+0.j]]
# '''

# # the trace
# print(H.tr())
# #output:
# '''0.0'''

# # the Eigen energies
# print(H.eigenenergies())
# #output:
# '''[-1.00498756  1.00498756]'''

# # States and operators
# #State Vectors

# # Fundamental basis states (Fock states of oscillator modes)
# N = 2
# n = 1
# print(basis(N, n))
# #output:
# '''
# Quantum object: dims = [[2], [1]], shape = (2, 1), type = ket
# Qobj data =
# [[ 0.]
#  [ 1.]]
# '''
# print(fock(4,2))
# #output:
# '''Quantum object: dims = [[4], [1]], shape = (4, 1), type = ket
# Qobj data =
# [[ 0.]
#  [ 0.]
#  [ 1.]
#  [ 0.]]
# '''
# a coherent state
print(coherent(N=10, alpha=1.0))
#output:
'''
Quantum object: dims = [[10], [1]], shape = (10, 1), type = ket
Qobj data =
[[ 0.60653066]
 [ 0.60653066]
 [ 0.42888194]
 [ 0.24761511]
 [ 0.12380753]
 [ 0.0553686 ]
 [ 0.02260303]
 [ 0.00854887]
 [ 0.00299672]
 [ 0.00110007]]
'''
