{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1 2 3 4 5 6 7 8 9]\n",
      "{'mean': [[np.float64(4.0), np.float64(5.0), np.float64(6.0)], [np.float64(2.0), np.float64(5.0), np.float64(8.0)], np.float64(5.0)], 'variance': [[np.float64(6.0), np.float64(6.0), np.float64(6.0)], [np.float64(0.6666666666666666), np.float64(0.6666666666666666), np.float64(0.6666666666666666)], np.float64(6.666666666666667)], 'standard deviation': [[np.float64(2.449489742783178), np.float64(2.449489742783178), np.float64(2.449489742783178)], [np.float64(0.816496580927726), np.float64(0.816496580927726), np.float64(0.816496580927726)], np.float64(2.581988897471611)], 'max': [[np.int64(7), np.int64(8), np.int64(9)], [np.int64(3), np.int64(6), np.int64(9)], np.int64(9)], 'min': [[np.int64(1), np.int64(2), np.int64(3)], [np.int64(1), np.int64(4), np.int64(7)], np.int64(1)], 'sum': [[np.int64(12), np.int64(15), np.int64(18)], [np.int64(6), np.int64(15), np.int64(24)], np.int64(45)]}\n"
     ]
    }
   ],
   "source": [
    "import numpy as np\n",
    "\n",
    "def calculate(lst):\n",
    "        ls = np.array(lst)  \n",
    "        print(ls)\n",
    "\n",
    "        \n",
    "        mean_rows = [ls[[0, 1, 2]].mean(), ls[[3, 4, 5]].mean(), ls[[6, 7, 8]].mean()]\n",
    "        mean_columns = [ls[[0, 3, 6]].mean(), ls[[1, 4, 7]].mean(), ls[[2, 5, 8]].mean()]\n",
    "\n",
    "        \n",
    "        var_rows = [ls[[0, 1, 2]].var(), ls[[3, 4, 5]].var(), ls[[6, 7, 8]].var()]\n",
    "        var_columns = [ls[[0, 3, 6]].var(), ls[[1, 4, 7]].var(), ls[[2, 5, 8]].var()]\n",
    "\n",
    "        \n",
    "        std_rows = [ls[[0, 1, 2]].std(), ls[[3, 4, 5]].std(), ls[[6, 7, 8]].std()]\n",
    "        std_columns = [ls[[0, 3, 6]].std(), ls[[1, 4, 7]].std(), ls[[2, 5, 8]].std()]\n",
    "\n",
    "        \n",
    "        max_rows = [ls[[0, 1, 2]].max(), ls[[3, 4, 5]].max(), ls[[6, 7, 8]].max()]\n",
    "        max_columns = [ls[[0, 3, 6]].max(), ls[[1, 4, 7]].max(), ls[[2, 5, 8]].max()]\n",
    "\n",
    "        \n",
    "        min_rows = [ls[[0, 1, 2]].min(), ls[[3, 4, 5]].min(), ls[[6, 7, 8]].min()]\n",
    "        min_columns = [ls[[0, 3, 6]].min(), ls[[1, 4, 7]].min(), ls[[2, 5, 8]].min()]\n",
    "\n",
    "        \n",
    "        sum_rows = [ls[[0, 1, 2]].sum(), ls[[3, 4, 5]].sum(), ls[[6, 7, 8]].sum()]\n",
    "        sum_columns = [ls[[0, 3, 6]].sum(), ls[[1, 4, 7]].sum(), ls[[2, 5, 8]].sum()]\n",
    "\n",
    "        return {\n",
    "            'mean': [mean_columns, mean_rows, ls.mean()],\n",
    "            'variance': [var_columns, var_rows, ls.var()],\n",
    "            'standard deviation': [std_columns, std_rows, ls.std()],\n",
    "            'max': [max_columns, max_rows, ls.max()],\n",
    "            'min': [min_columns, min_rows, ls.min()],\n",
    "            'sum': [sum_columns, sum_rows, ls.sum()],\n",
    "        }\n",
    "\n",
    "    \n",
    "result = calculate([1, 2, 3, 4, 5, 6, 7, 8, 9])\n",
    "print(result)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
