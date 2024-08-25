# -*- coding: utf-8 -*-
"""
Created on Thu May 19 11:25:08 2022

@author: Maryam
"""
import pandas as pd
m_list =[-0.002,-0.001]
sim_type='D_wind_check_price_1e-9'
#print(sim_type)
for m in m_list:
 for n in [0,1,2,3,4,5,6,7,8]:
    load_factor = pd.read_csv("inputs/vre_obs_pv_wind.csv", index_col=[0, 1], header=None)
    load_factor = load_factor.squeeze().copy()

    load_factor_onshore = load_factor['onshore'].copy()
    load_factor_onshore_sorted = load_factor_onshore.sort_values().copy()
    load_factor_onshore_sorted = load_factor_onshore_sorted.reset_index().copy()
    load_factor_onshore_sorted.loc[(n)*8760:(n+1)*8760, 2] = (load_factor_onshore_sorted.loc[(n)*8760:(n+1)*8760, 2]+m).copy()
    load_factor_onshore_back_to_original1 = load_factor_onshore_sorted.sort_values(by=[1]).copy()
    load_factor_onshore_back_to_original2 = load_factor_onshore_back_to_original1.set_index(1).copy()

    load_factor.loc['onshore', :] = (load_factor_onshore_back_to_original2[2].values).copy()

    print(sim_type, n,m)

    exec(open('EOLES_pert cf.py').read())




