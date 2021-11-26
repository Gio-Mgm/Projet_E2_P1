import pandas as pd


def get_df_uniques(df):
    attFeatures = []
    for col in df.columns:
        attFeatures.append(
            [col, df[col].dtype, df[col].nunique(),
             df[col].drop_duplicates().values]
        )
    return pd.DataFrame(attFeatures, columns=[
            'Features', 'Dtype', 'Uniques count', 'Values'
    ])


def get_corr_pairs_thresh(df, size, thresh):
    s = df.corr().abs().unstack().sort_values(ascending=False)
    s = s[s.values < 1]
    for i in range(size*2):
        if s[i] > thresh:
            if i % 2 == 0:
                print("{:.5f} {}".format(s[i], s.index[i]))


def manage_major_values(df, thresh, drop=False):
    s = pd.Series(dtype="float64")
    for col in df.columns:
        # Ajout dans la Series du pourcentage d'occurence
        # par rapport à la taille de la colonne pour chaque colonnes
        s.loc[col] = df[col].value_counts().iloc[0]/len(df[col])*100
    # Récupération des x colonnes avec le pourcentage le plus haut
    # return(s[s > thresh].sort_values(ascending=False))
    return df.drop(columns=s[s > thresh].index.tolist()) if drop else df
