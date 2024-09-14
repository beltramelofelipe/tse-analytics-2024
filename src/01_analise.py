
# %%
import pandas as pd
import sqlalchemy

import matplotlib.pyplot as plt
import seaborn as sns
from adjustText import adjust_text
# %%
with open("partidos.sql", "r") as open_file:
    query = open_file.read()

engine = sqlalchemy.create_engine("sqlite:///../data/database.db")

df = pd.read_sql(query, engine)

df.head()

# %%

txGenFeminino = df['totalGenFeminino'].sum() / df['totalCandidaturas'].sum()
txRacaPreta = df['totalCorRacaPreta'].sum() / df['totalCandidaturas'].sum()
txRacaNaoBranca = df['totalCorRacaNaoBranca'].sum() / df['totalCandidaturas'].sum()
txRacaPretaParda = df['totalCorRacaPretaParda'].sum() / df['totalCandidaturas'].sum()


# %% 
plt.figure(dpi=500)

sns.scatterplot(df, 
                x='txGenFemininoBR', 
                y='txCorRacaPretaBR')

texts= []
for i in df['SG_PARTIDO']:
    data = df[df["SG_PARTIDO"] == i]  
    x = data['txGenFemininoBR'].values[0]
    y= data['txCorRacaPretaBR'].values[0]
    texts.append(plt.text(x, y, i, fontsize=9))

adjust_text(texts, 
            only_move={'points': 'y', 'texts': 'xy'}, 
            arrowprops=dict(arrowstyle='->', lw=1.5))

plt.grid(True)
plt.title("Partidos: Cor x Genero")
plt.xlabel("Taxa de Mulheres")
plt.ylabel("Taxa de Pessoas Pretas")
# plt.show()
plt.hlines(y=txRacaPreta, xmin=0.3, xmax=0.55, colors='black', alpha=0.6, linestyle='--', label=f"Pessoas Pretas Geral: {100*txRacaPreta:.0f}%")
plt.vlines(x=txGenFeminino, ymin=0.05, ymax=0.35,colors='tomato', alpha=0.6, linestyle='--', label=f"Mulheres Geral: {100*txGenFeminino:.0f}%")


plt.legend()

plt.savefig('../img/partidos_cor_raca_genero.png')
# %%
