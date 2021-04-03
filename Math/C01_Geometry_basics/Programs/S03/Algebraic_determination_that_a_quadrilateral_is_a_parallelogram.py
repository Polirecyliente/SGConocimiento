#T# the following code shows how to do an algebraic determination that a quadrilateral is a parallelogram

#T# create the points of the quadrilateral
A = (0, 0)
B = (5, 0)
C = (8, 2.4)
D = (3, 2.4)

#T# calculate the slopes of the four sides
m_AB = (B[1] - A[1])/(B[0] - A[0]) # 0.0
m_BC = (C[1] - B[1])/(C[0] - B[0]) # 0.7999999999999999
m_CD = (D[1] - C[1])/(D[0] - C[0]) # -0.0
m_DA = (A[1] - D[1])/(A[0] - D[0]) # 0.7999999999999999

#T# check if the opposite sides have equal slopes, if they do, then the quadrilateral is a parallelogram
bool_AB_CD = m_AB == m_CD # True
bool_BC_DA = m_BC == m_DA # True