{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy.stats import linregress\n",
    "\n",
    "def draw_plot():\n",
    "    # Read data from file\n",
    "\n",
    "    df = pd.read_csv('epa-sea-level.csv')\n",
    "    y = df['CSIRO Adjusted Sea Level']\n",
    "    x = df['Year']\n",
    "\n",
    "\n",
    "    # Create scatter plot\n",
    "\n",
    "    fig, ax = plt.subplots()\n",
    "    plt.scatter(x, y)\n",
    "\n",
    "\n",
    "    # Create first line of best fit\n",
    "\n",
    "    res = linregress(x, y)\n",
    "    x_pred = pd.Series([i for i in range(1880, 2051)])\n",
    "    y_pred = res.slope*x_pred + res.intercept\n",
    "    plt.plot(x_pred, y_pred, 'r')\n",
    "\n",
    "\n",
    "    # Create second line of best fit\n",
    "\n",
    "    new_df = df[df['Year'] >= 2000]\n",
    "    new_y = new_df['CSIRO Adjusted Sea Level']\n",
    "    new_x = new_df['Year']\n",
    "    res_2 = linregress(new_x, new_y)\n",
    "    x_pred_2 = pd.Series([i for i in range(2000, 2051)])\n",
    "    y_pred_2 = res_2.slope*x_pred_2 + res_2.intercept\n",
    "    plt.plot(x_pred_2, y_pred_2, 'green')\n",
    "\n",
    "\n",
    "    # Add labels and title\n",
    "\n",
    "    ax.set_xlabel('Year')\n",
    "    ax.set_ylabel('Sea Level (inches)')\n",
    "    ax.set_title('Rise in Sea Level')\n",
    "\n",
    "\n",
    "    # Save plot and return data for testing (DO NOT MODIFY)\n",
    "    plt.savefig('sea_level_plot.png')\n",
    "    return plt.gca()"
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
