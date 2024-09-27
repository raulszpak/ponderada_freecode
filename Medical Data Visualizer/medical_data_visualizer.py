{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "\n",
    "# 1\n",
    "df = pd.read_csv('medical_examination.csv')\n",
    "\n",
    "\n",
    "df['overweight'] = (df['weight'] / ((df['height'] / 100) **2 )). apply(lambda x : 1 if x >5 else 0)\n",
    "df['cholesterol'] = df['cholesterol']. apply(lambda x : 0 if x == 1 else 1)\n",
    "df['gluc'] = df['gluc']. apply(lambda x : 0 if x == 1 else 1)\n",
    "\n",
    "def fraw_cat_plot():\n",
    "  df_cat = pd.melt(df, id_vars = ['cardio'], value_vars = ['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])\n",
    "\n",
    "  df_cat['total'] = 1\n",
    "  df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index = False).count()\n",
    "\n",
    "  fig = sns.catplot(x = 'variable', y = 'total', hue = 'value', col = 'cardio', data = df_cat, kind = 'bar').fig\n",
    "  fig.savefig('catplot.png')\n",
    "  return fig\n",
    "\n",
    "  def draw_heat_map():\n",
    "   df_heat = df[\n",
    "  (df['ap_lo'] <= df['ap_hi']) &\n",
    "  (df['height'] >= df['height'].quantile(0.025)) &\n",
    "  (df['height'] <= df['height'].quantile(0.975)) &\n",
    "  (df['weight'] >= df['weight'].quantile(0.025)) &\n",
    "  (df['weight'] <= df['weight'].quantile(0.975))]\n",
    "\n",
    "  corr = df_heat.corr(method='pearson')\n",
    "\n",
    "  mask = np.triu(corr)\n",
    "\n",
    "  fig, ax = plt.subplots(figsize=(12, 12))\n",
    "\n",
    "  sns.heatmap(cprr, linewidths=1, annot = True, mask = mask, fmt ='.lf', center =0.09,cbar_kws = {'shrink':0.5})\n",
    "  fig.savefig('heatmap.png')\n",
    "  return fig\n"
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
