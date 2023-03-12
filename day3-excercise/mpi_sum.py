#################################################
#  File Name:mpi_sum.py
#  Author: Pengwei.Xing
#  Mail: xingwei421@qq.com,pengwei.xing@igp.uu.se,xpw1992@gmail.com
#  Created Time: Thu Mar  9 15:12:14 2023
#################################################


from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

data = np.random.random(1)
total = np.zeros(1)

comm.Reduce(data, total, op=MPI.SUM, root=0)

if rank == 0:
    print(f"The sum of data is: {total}")
