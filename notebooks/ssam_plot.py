import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import xarray as xr
import geopandas as gpd
import matplotlib.cm as cm
from ssam_groups import cohorts
from ssam_groups import bacteria
from PIL import Image
import glob
from IPython.display import Image as img
from mpl_toolkits.axes_grid1 import make_axes_locatable

label_size = 11
font_size = 12
line_width = 2


def plot_bacteria(scenario, control, time, start, end, event_start, y_min=None, y_max=None):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Bacteria groups in Salish Sea Atlantis', fontsize = font_size)

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,0:6], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,0:6,], np.nan)
            b_oiled = bact_oiled.sum(axis=2)
            b_control = bact_control.sum(axis=2)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,6], np.nan)
        
        ratio = b_oiled.sum(axis=1) / b_control.sum(axis=1) 
        control_ratio = b_control.sum(axis=1) / b_control.sum(axis=1)
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bacteria, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [ratio.min(), ratio.max()], 'r',alpha=0.1)

def plot_sediment(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Sediment groups in Salish Sea Atlantis', fontsize = font_size)

    for species in bio_group:
        sed_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        sed_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,6], np.nan)
        s_oiled = sed_oiled.sum(axis=1)
        s_control = sed_control.sum(axis=1)
        ratio = s_oiled / s_control
        control_ratio = s_control / s_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bio_group, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [ratio.min(), ratio.max()], 'r',alpha=0.1)

def plot_benthic_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): # benthos, shellfish

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Benthic groups in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        benthic_oiled = scenario.variables[bio_group[species] + '_N'][start:end,box_number] # tonnes
        benthic_control = control.variables[bio_group[species] + '_N'][start:end,box_number]
        ratio = benthic_oiled / benthic_control
        control_ratio = benthic_control / benthic_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bio_group, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim(y_min, y_max)
    #ax.plot([spill_end, spill_end], [min, max], 'r',alpha=0.1)

def plot_bacteria_box(scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in bacteria relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,0:6], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan)
        
        ratio = b_oiled / b_control
        control_ratio = b_control / b_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bacteria, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_pelagic_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton
    
    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in pelagic groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled / p_control
        control_ratio = p_control / p_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bio_group, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_surface_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton
    
    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in surface groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled / p_control
        control_ratio = p_control / p_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bio_group, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_sediment_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #mostly for sediment_feeders

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in sediment groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        s_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        s_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,6], np.nan)
        ratio = s_oiled / s_control
        control_ratio = s_control / s_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(bio_group, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_cohorts(bio_group, scenario, control, time, start, end, event_start):

    for species in bio_group:

        fig, ax = plt.subplots(3,1, figsize = (14,9), sharex='all')
        ax[0].plot(event_start, 0, 'ok')
        ax[1].plot(event_start,0, 'ok')
        ax[2].plot(event_start, 0, 'ok')

        numCohorts = cohorts[bio_group[species]]

        for cohort in range (1, numCohorts+1):

            new_species = bio_group[species] + str(cohort)
        
            o_numbers = np.ma.filled(scenario.variables[new_species + '_Nums'][start:end,:,:], np.nan)
            o_structuralN = np.ma.filled(scenario.variables[new_species +'_StructN'][start:end,:,:], np.nan)
            o_reservedN = np.ma.filled(scenario.variables[new_species +'_ResN'][start:end,:,:], np.nan)

            c_numbers = np.ma.filled(control.variables[new_species + '_Nums'][start:end,:,:], np.nan)
            c_structuralN = np.ma.filled(control.variables[new_species +'_StructN'][start:end,:,:], np.nan)
            c_reservedN = np.ma.filled(control.variables[new_species +'_ResN'][start:end,:,:], np.nan)

            o_numbers = o_numbers.sum(axis=2)
            o_structuralN = o_structuralN.sum(axis=2)
            o_reservedN = o_reservedN.sum(axis=2)

            c_numbers = c_numbers.sum(axis=2)
            c_structuralN = c_structuralN.sum(axis=2)
            c_reservedN = c_reservedN.sum(axis=2)

            numbers = (o_numbers.sum(axis=1) / c_numbers.sum(axis=1)-1)*100
            structuralN = (o_structuralN.sum(axis=1) / c_structuralN.sum(axis=1)-1)*100
            reservedN =(o_reservedN.sum(axis=1) / c_reservedN.sum(axis=1)-1)*100

            ax[0].plot(time[start:end], numbers, linewidth = line_width)
            ax[1].plot(time[start:end], structuralN,linewidth = line_width)
            ax[2].plot(time[start:end], reservedN,linewidth = line_width)
    
        ax[0].set_title('Numbers of ' + str(bio_group[species]), fontsize = font_size)
        ax[0].tick_params(labelsize=label_size)
        ax[0].legend(['event start','cohort 1','cohort 2','cohort 3','cohort 4','cohort 5','cohort 6','cohort 7','cohort 8','cohort 9','cohort 10',]) #loc='center left'
        
        ax[1].set_title('Structural Nitrogen (bone size)', fontsize = font_size)
        ax[1].set_ylabel('Percent (%) Change Relative to Control', fontsize = font_size)
        ax[1].tick_params(labelsize=label_size);
        
        ax[2].set_title('Reserve Nitrogen (fatty tissue)', fontsize = font_size)
        ax[2].tick_params(labelsize=label_size);
        

def plot_pelagic_biomass(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None):

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1]) 

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N m$^{-3}$') 
        ax.set_title(str(bio_group[species]), fontsize = font_size)
        ax.plot(time[start:end], p_oiled, label='scenario', linewidth = 2)
        ax.plot(time[start:end], p_control, 'k', label='control',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', label='event start', alpha=0.5)
        ax.set_ylim([y_min, y_max])
        #ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)  # to place the legend outside
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_benthic_biomass(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1]) 

    for species in bio_group:

        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N m$^{-3}$')
        ax.set_title(str(bio_group[species]), fontsize = font_size)
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
        ax.set_ylim([y_min, y_max])
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_bacteria_biomass(scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    bio_group = bacteria
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1]) 

    for species in bacteria:
    
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,0:6], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,0:6], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
            b_oiled = b_oiled.sum(axis=1)
            b_control = b_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,6], np.nan)
            b_oiled = b_oiled.sum(axis=1)
            b_control = b_control.sum(axis=1)
        
        p_max = b_oiled.max()
        p_min = b_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(bio_group[species]), fontsize = font_size)
        ax.plot(time[start:end], b_oiled, linewidth = 2)
        ax.plot(time[start:end], b_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
        ax.set_ylim([y_min, y_max])
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);        

def plot_surface_biomass(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): # benthos, shellfish
    
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
       
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(bio_group[species]), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_sediment_biomass(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(bio_group[species]), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_pelagic_biomass_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None):

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$') 
        ax.set_title(str(bio_group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_benthic_biomass_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 
    
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])
   
    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(bio_group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_bacteria_biomass_box(scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    bio_group = bacteria
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bacteria:
        
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,0:6], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan)
        
        p_max = b_oiled.max()
        p_min = b_oiled.min()
        
        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(bio_group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], b_oiled, linewidth = 2)
        ax.plot(time[start:end], b_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_surface_biomass_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Surface Biomass of ' + str(bio_group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_sediment_biomass_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,6], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        
        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(bio_group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_pelagic_diff_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Pelagic Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_benthic_diff_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Benthic Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_sediment_diff_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Sediment Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,6], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_surface_diff_box(bio_group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference Surface Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    
    for species in bio_group:

        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,box_number,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,box_number,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_bacteria_diff_box(scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Bacteria Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,0:6], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan)
        
        diff = b_oiled - b_control
        ax.plot(time[start:end], diff,linewidth = 2)
    
    c_diff = b_control - b_control
    ax.legend(bacteria, loc='center left')
    ax.plot(time[start:end], c_diff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_bacteria_diff(scenario, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Bacteria Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,0:6], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,0:6], np.nan)
            b_oiled = bact_oiled.sum(axis=2)
            b_control = bact_control.sum(axis=2)
            b_oiled = b_oiled.sum(axis=1)
            b_control = b_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,6], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        
        diff = b_oiled - b_control
        ax.plot(time[start:end], diff,linewidth = 2)
    
    c_diff = b_control - b_control
    ax.legend(bacteria, loc='center left')
    ax.plot(time[start:end], c_diff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_pelagic_diff(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Pelagic Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_benthic_diff(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Benthic Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_sediment_diff(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Sediment Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in bio_group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max]);

def plot_surface_diff(bio_group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference Surface Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in bio_group:

        pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,:,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,:,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(bio_group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max]);

def compare_pah(pah, scenarios, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.plot(event_start, 0, 'ro', alpha=0.5)

    for scenario in scenarios:
        Phe = np.ma.filled(scenario.variables[pah][start:end,:], np.nan)
        Phe = Phe.sum(axis=2)
        Phe = Phe.sum(axis=1)
        ax.plot(time[start:end], Phe) 
    
    ax.set_title('Concentration of ' + pah + ' in Salish Sea Atlantis', fontsize = font_size)
    ax.set_ylabel('mg PAH m$^{-3}$')
    ax.legend(['Release start','scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'], loc='best');

def compare_pelagic_pah_in_bio(bio_group, scenarios, pah, time, start, end, event_start):

    for species in bio_group:

        fig = plt.figure(figsize=(18, 18), facecolor='white')
        gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1], fig=fig)

        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])

        for scenario in scenarios:
            pelagic_oiled = scenario.variables[bio_group[species] + '_' + pah][start:end,:,:]
            p_oiled = pelagic_oiled.sum(axis=2)
            p_oiled = pelagic_oiled.sum(axis=1)
            ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.set_title(pah + ' inside ' + species)
        ax.set_ylabel('mgPAH')
        ax.plot(event_start, 0, 'ro', alpha=0.5)
        ax.legend(['scenario 1', 'scenario 2', 'scenario 3', 'scenario 4']);

def compare_pelagic_pah_in_bio_box(bio_group, scenarios, box_number, pah, time, start, end, event_start):

    for species in bio_group:
        fig, ax = plt.subplots(figsize = (14,3))
        for scenario in scenarios:
            pelagic_oiled = scenario.variables[bio_group[species] + '_' + pah][start:end,box_number,:]
            p_oiled = pelagic_oiled.sum(axis=1)
            ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.set_title(species)
        ax.set_ylabel('mgPAH')
        ax.plot(event_start, 0, 'ro', alpha=0.5)
        ax.legend(['scenario 1', 'scenario 2', 'scenario 3', 'scenario 4']);

def boxplot_pelagic(bio_group, scenario, control, start, boxes, days, data_labels, x_lim=None, bio_colours=['#063764','#0b5394','#3d85c6','#6fa8dc','#9fc5e8']): #bacteria, plankton
    
    df = pd.DataFrame(data_labels)
    spp = []
    
    for species in bio_group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:day,boxes,0:6], np.nan) # tonnes, take only water column layers
            p_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:day,boxes,0:6], np.nan)
            p_oiled = p_oiled.sum(axis=0)
            p_oiled = p_oiled.sum(axis=0)
            p_oiled = p_oiled.sum(axis=0)
            p_control = p_control.sum(axis=0)
            p_control = p_control.sum(axis=0)
            p_control = p_control.sum(axis=0)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(bio_group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')

    df1.plot(kind="barh", subplots=True, layout=(1,len(days)), figsize=(15,4), sharey=True, sharex=True, color=bio_colours, legend=None,
         xlabel='Pelagic Groups', ylabel=None, title='Percent (%) Change Relative to Control for Select Pelagic Groups', xlim=x_lim); 

def boxplot_pelagic_all(bio_group, scenarios, control, boxes, days, data_labels, x_lim=None): #bacteria, plankton
    
    for item in scenarios:
        boxplot_pelagic(bio_group, item, control, boxes, days, data_labels, x_lim=None)
    

def boxplot_benthic(bio_group, scenario, control, start, boxes, days, data_labels, x_lim=None, bio_colours=['#783f04','#b45f06','#e69138','#f6b26b','#f9cb9c']): 

    df = pd.DataFrame(data_labels)
    spp = []

    for species in bio_group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:day,boxes], np.nan) # tonnes, take only water column layers
            p_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:day,boxes], np.nan)
            p_oiled = p_oiled.sum(axis=0)
            p_oiled = p_oiled.sum(axis=0)
            p_control = p_control.sum(axis=0)
            p_control = p_control.sum(axis=0)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(bio_group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')

    df1.plot(kind="barh", subplots=True, layout=(1,len(days)), figsize=(15,6), sharey=True, sharex=True, color=bio_colours, legend=None,
         xlabel='Benthic Groups', ylabel=None, title='Percent (%) Change Relative to Control for Select Benthic Groups', xlim=x_lim);

def boxplot_benthic_all(bio_group, scenarios, control, boxes, days, data_labels, x_lim=None): #bacteria, plankton
    
    for item in scenarios:
        boxplot_benthic(bio_group, item, control, boxes, days, data_labels, x_lim=None)

def boxplot_sediment(bio_group, scenario, control, boxes, days, data_labels, x_lim=None, bio_colours=['#783f04','#b45f06','#e69138','#f6b26b','#f9cb9c']):
    
    df = pd.DataFrame(data_labels)
    spp = []
    
    for species in bio_group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][day,boxes,6], np.nan) # tonnes, only sediment layers
            p_control = np.ma.filled(control.variables[bio_group[species] + '_N'][day,boxes,6], np.nan)
            p_oiled = p_oiled.sum(axis=0)
            p_control = p_control.sum(axis=0)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(bio_group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')

    df1.plot(kind="barh", subplots=True, layout=(1,len(days)), figsize=(15,4), sharey=True, sharex=True, color=bio_colours, legend=None,
         xlabel='Pelagic Groups', ylabel=None, title='Percent (%) Change Relative to Control for Select Sedimentary Groups', xlim=x_lim); 

def boxplot_sediment_all(bio_group, scenarios, control, boxes, days, data_labels, x_lim=None):
    
    for item in scenarios:
        boxplot_sediment(bio_group, item, control, boxes, days, data_labels, x_lim=None)

def compare_scenarios_benthic_N(bio_group, scenarios, control, time, start, end, boxes, y_min=None, y_max=None): # benthos, shellfish

    # Plot variables
    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        
        benthic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,boxes], np.nan)
        benthic_control = benthic_control.sum(axis=1)
        control_ratio = (benthic_control / benthic_control-1)*100
        ax.plot(time[start:end], control_ratio, 'k', linewidth = 2)

        for scenario in scenarios:
            benthic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,boxes], np.nan) # tonnes
            ratio = (benthic_oiled.sum(axis=1) / benthic_control-1)*100 
            ax.plot(time[start:end], ratio, linewidth = 2)
        
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(species)
        ax.set_ylim([y_min, y_max]);

def compare_scenarios_pelagic_N(bio_group, scenario_paths, control, time, start, end, boxes, y_min=None, y_max=None): #bacteria, plankton, sharks, birds, mammals, named_fish, salmon, fish, benth_feeders

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        
        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])

        pelagic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,boxes,0:6], np.nan)
        pelagic_control = pelagic_control.sum(axis=2)
        pelagic_control = pelagic_control.sum(axis=1)
        control_ratio = (pelagic_control / pelagic_control-1)*100
        ax.plot(time[start:end], control_ratio, 'k', linewidth = 2)
    
        for path in scenario_paths:
            scenario = xr.open_dataset(str(path), decode_cf=True)
            pelagic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,boxes,0:6], np.nan) # tonnes
            pelagic_oiled = pelagic_oiled.sum(axis=2) 
            pelagic_oiled = pelagic_oiled.sum(axis=1) 
            ratio = (pelagic_oiled / pelagic_control-1)*100
            ax.plot(time[start:end], ratio, linewidth = 2)
       
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(species)
        ax.set_ylim([y_min, y_max]);

def compare_scenarios_pelagic_parameter(parameter_group, scenarios, control, time, start, end, boxes, y_min=None, y_max=None): # for use with any parameter that does not require _N

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for parameter in parameter_group:
        
        bio_index = (list(parameter_group).index(parameter))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])

        pelagic_control = np.ma.filled(control.variables[parameter_group[parameter]][start:end,boxes,0:6], np.nan)
        pelagic_control = pelagic_control.sum(axis=2)
        pelagic_control = pelagic_control.sum(axis=1)
        control_ratio = (pelagic_control / pelagic_control-1)*100
        ax.plot(time[start:end], control_ratio, 'k', linewidth = 2)
    
        for scenario in scenarios:
            pelagic_oiled = np.ma.filled(scenario.variables[parameter_group[parameter]][start:end, boxes,0:6], np.nan) # tonnes
            pelagic_oiled = pelagic_oiled.sum(axis=2) 
            pelagic_oiled = pelagic_oiled.sum(axis=1) 
            ratio = (pelagic_oiled / pelagic_control-1)*100
            ax.plot(time[start:end], ratio, linewidth = 2)
       
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(parameter)
        ax.set_ylim([y_min, y_max]);

def compare_scenarios_sediment_parameter(parameter_group, scenarios, control, time, start, end, boxes, y_min=None, y_max=None): # for use with any parameter that does not require _N

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for parameter in parameter_group:
        
        bio_index = (list(parameter_group).index(parameter))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])

        sediment_control = np.ma.filled(control.variables[parameter_group[parameter]][start:end,boxes,6], np.nan)
        sediment_control = sediment_control.sum(axis=1)
        control_ratio = (sediment_control / sediment_control-1)*100
        ax.plot(time[start:end], control_ratio, 'k', linewidth = 2)
    
        for scenario in scenarios:
            sediment_oiled = np.ma.filled(scenario.variables[parameter_group[parameter]][start:end,boxes,6], np.nan) # tonnes
            sediment_oiled = sediment_oiled.sum(axis=1) 
            ratio = (sediment_oiled / sediment_control-1)*100
            ax.plot(time[start:end], ratio, linewidth = 2)
       
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(parameter)
        ax.set_ylim([y_min, y_max]);

def compare_scenarios_sediment_N(bio_group, scenarios, control, time, start, end, boxes, y_min=None, y_max=None): # benthos, shellfish

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in bio_group:
        bio_index = (list(bio_group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])

        benthic_control = np.ma.filled(control.variables[bio_group[species] + '_N'][start:end,boxes,6], np.nan)
        benthic_control = benthic_control.sum(axis=1)
        control_ratio = (benthic_control  / benthic_control-1)*100
        ax.plot(time[start:end], control_ratio, 'k', linewidth = 2)

        for scenario in scenarios:
            benthic_oiled = np.ma.filled(scenario.variables[bio_group[species] + '_N'][start:end,boxes,6], np.nan) # tonnes
            ratio = (benthic_oiled.sum(axis=1) / benthic_control-1)*100 
            ax.plot(time[start:end], ratio, linewidth = 2)
       
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3'])
        ax.set_title(species)
        ax.set_ylim([y_min, y_max]);

def map_variable_aggregate_time(variable_name, scenarios, v_max=None, v_min=None, _cmap=cm.Purples):
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    land_df = map_df.loc[land_boxes]

    _cmap = cm.Purples
    
    # map of single variable ratio across the whole simulation

    # Pull variables for all scenarios
    fig = plt.figure(figsize=(29, 8), facecolor='white') #figsize=(9, 12)
    gs = plt.GridSpec(1, len(scenarios), wspace=0.5, hspace=0.2, height_ratios=[1],)

    position = 0

    for scenario in scenarios:
        dVar_s = scenario.variables[variable_name]
        dVar_s = dVar_s.sum(axis=2)
        pah = dVar_s.sum(axis=0)

        # Add scenario data to Atlantis spatial data
        map_df['pah'] = pah
        map_df.loc[land_boxes, 'pah'] = 0

        ax = fig.add_subplot(gs[0, position])
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=-0.5) 
        ax = map_df.plot(column = 'pah', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max, cax=cax,
            legend=True, #legend_kwds={'label': variable_name + ' % difference from control'},
            )
        ax.set_title('Scenario '+ str(position+1), fontsize = font_size)
        map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
        land_df.plot(ax=ax, color='white');
        position = position+1

def map_pelagic_aggregate_time(variable_name, scenarios, control, v_max=100, v_min=-100):
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    land_df = map_df.loc[land_boxes]

    _cmap = cm.bwr # cm.ocean_r
    
    # map of single variable ratio across the whole simulation

    # Pull variables for all scenarios
    dVar_control = control.variables[variable_name]
    dVar_control = dVar_control.sum(axis=2)
    dVar_control = dVar_control.sum(axis=0)

    fig = plt.figure(figsize=(29, 8), facecolor='white') #figsize=(9, 12)
    gs = plt.GridSpec(1, len(scenarios), wspace=0.5, hspace=0.2, height_ratios=[1],)

    position = 0

    for scenario in scenarios:
        dVar_s = scenario.variables[variable_name]
        dVar_s = dVar_s.sum(axis=2)
        dVar_s = dVar_s.sum(axis=0)
        percent_oil = (dVar_s / dVar_control-1)*100 

        # Add scenario data to Atlantis spatial data
        map_df['percent'] = percent_oil
        map_df.loc[land_boxes, 'percent'] = 0

        ax = fig.add_subplot(gs[0, position])
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=-0.5) 
        ax = map_df.plot(column = 'percent', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max, cax=cax,
            legend=True, #legend_kwds={'label': variable_name + ' % difference from control'},
            )
        ax.set_title('Scenario '+ str(position+1), fontsize = font_size)
        map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
        land_df.plot(ax=ax, color='white');
        position = position+1

    return

def map_pelagic_single_time(variable_name, scenarios, control, time, time_index, start, end, event_start, v_max=100, v_min=-100):
    # map of single variable ratio at a specific time index
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    land_df = map_df.loc[land_boxes]

    _cmap = cm.coolwarm # RdGy_r #cm.PuOr_r cm.bwr cm.ocean_r 

    ts_date = np.array(time[time_index])

    dVar_control = control.variables[variable_name]
    dVar_control = dVar_control.sum(axis=2)
    box_sum_control = dVar_control.sum(axis=1)
    control_ratio = (box_sum_control / box_sum_control-1)*100

    fig = plt.figure(figsize=(18, 12), facecolor='white')
    gs = plt.GridSpec(2, len(scenarios), height_ratios=[1, 3])
    ax_ts = fig.add_subplot(gs[0,:])
    ax_ts.plot(event_start, 0, 'ro', alpha=0.4)
    ax_ts.plot([ts_date, ts_date], [-10, 10], 'k--')
    ax_ts.plot(time[start:end], control_ratio[start:end], 'k', linewidth = line_width)
    ax_ts.set_title('Percent (%) Change in '+ variable_name, fontsize = font_size)

    position = 0
   
    for scenario in scenarios:
        dVar_s = scenario.variables[variable_name]
        dVar_s = dVar_s.sum(axis=2)
        box_sum_scenario = dVar_s.sum(axis=1) 
        scenario_ratio = (box_sum_scenario / box_sum_control-1)*100

        ## Select specific time period
        tVar_control = dVar_control[time_index,:]
        tVar_s = dVar_s[time_index,:]
        oil_ratio = (tVar_s / tVar_control -1)*100

        # Add scenario data to Atlantis spatial data
        map_df['scen'] = oil_ratio
        map_df.loc[land_boxes, 'scen'] = 0
        
        ax_ts.plot(time[start:end], scenario_ratio[start:end], linewidth = line_width)

        ax = fig.add_subplot(gs[1,position])
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=-0.5) 
        ax = map_df.plot(column = 'scen', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max, cax=cax,
            legend=True,
            #legend_kwds={'label': variable_name + ' percent (%) change'},
            )
        ax.set_title('Scenario '+ str(position+1), fontsize = font_size)
        map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
        land_df.plot(ax=ax, color='white')
        position = position+1
    # sm = plt.cm.ScalarMappable(cmap=_cmap, norm=plt.Normalize(vmin=v_min, vmax=v_max))
    # sm._A = []
    # fig.colorbar(sm)

    #ax= map_df.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);
    ax_ts.set_ylabel('Percent (%) Change', fontsize = font_size)
    ax_ts.legend(['event start','track date','control','scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'], loc='lower left')
    ax_ts.tick_params(labelsize=label_size)

    return

def animate_map_pelagic(variable_name, scenarios, control, time, start, end, event_start, v_max=100, v_min=-100):
    # animation of map of single variable ratio over time

    file_names = []

    for time_index in range(start, end):
    
        map_pelagic_single_time(variable_name, scenarios, control, time, time_index, start, end, event_start)
        
        plot_name = variable_name + '_' + str(time_index).zfill(3) + '.png'
        plt.savefig(plot_name)
        file_names.append(plot_name)
        plt.close()

    frames = []
    imgs = glob.glob("*.png")
    imgs.sort() 
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    # Save frames into a loop
    anim_name = variable_name + '.gif'
    frames[0].save(anim_name, format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300, loop=0)

    file_name_str = ' '.join(file_names)
    os.system('rm ' + file_name_str)

    # Display the figure
    with open(anim_name,'rb') as anim:
        display(img(anim.read()))
    
    return

def map_benthic_single_time(variable_name, scenarios, control, time, time_index, start, end, event_start, v_max=100, v_min=-100):
    # map of single variable ratio at a specific time index
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    land_df = map_df.loc[land_boxes]

    _cmap = cm.coolwarm # RdGy_r #cm.PuOr_r cm.bwr cm.ocean_r 

    ts_date = np.array(time[time_index])

    dVar_control = control.variables[variable_name]
    box_sum_control = dVar_control.sum(axis=1)
    control_ratio = (box_sum_control / box_sum_control-1)*100

    fig = plt.figure(figsize=(18, 12), facecolor='white')
    gs = plt.GridSpec(2, len(scenarios), height_ratios=[1, 3])
    ax_ts = fig.add_subplot(gs[0,:])
    ax_ts.plot(event_start, 0, 'ro', alpha=0.4)
    ax_ts.plot([ts_date, ts_date], [-10, 10], 'k--')
    ax_ts.plot(time[start:end], control_ratio[start:end], 'k', linewidth = line_width)
    ax_ts.set_title('Percent (%) Change in '+ variable_name, fontsize = font_size)

    position = 0
   
    for scenario in scenarios:
        dVar_s = scenario.variables[variable_name]
        box_sum_scenario = dVar_s.sum(axis=1) 
        scenario_ratio = (box_sum_scenario / box_sum_control-1)*100

        ## Select specific time period
        tVar_control = dVar_control[time_index,:]
        tVar_s = dVar_s[time_index,:]
        oil_ratio = (tVar_s / tVar_control -1)*100

        # Add scenario data to Atlantis spatial data
        map_df['scen'] = oil_ratio
        map_df.loc[land_boxes, 'scen'] = 0
        
        ax_ts.plot(time[start:end], scenario_ratio[start:end], linewidth = line_width)

        ax = fig.add_subplot(gs[1,position])
        divider = make_axes_locatable(ax)
        cax = divider.append_axes("right", size="5%", pad=-0.5) 
        ax = map_df.plot(column = 'scen', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max, cax=cax,
            legend=True,
            #legend_kwds={'label': variable_name + ' percent (%) change'},
            )
        ax.set_title('Scenario '+ str(position+1), fontsize = font_size)
        map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
        land_df.plot(ax=ax, color='white')
        position = position+1
    ax_ts.set_ylabel('Percent (%) Change', fontsize = font_size)
    ax_ts.legend(['event start','track date','control','scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'], loc='lower left')
    ax_ts.tick_params(labelsize=label_size)

    return

def animate_map_benthic(variable_name, scenarios, control, time, start, end, event_start, v_max=100, v_min=-100):
    # animation of single variable ratio over time

    file_names = []

    for time_index in range(start, end):
    
        map_benthic_single_time(variable_name, scenarios, control, time, time_index, start, end, event_start)
        
        plot_name = variable_name + '_' + str(time_index).zfill(3) + '.png'
        plt.savefig(plot_name)
        file_names.append(plot_name)
        plt.close()

    frames = []
    imgs = glob.glob("*.png")
    imgs.sort() 
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)

    # Save frames into a loop
    anim_name = variable_name + '.gif'
    frames[0].save(anim_name, format='GIF',
                append_images=frames[1:],
                save_all=True,
                duration=300, loop=0)

    file_name_str = ' '.join(file_names)
    os.system('rm ' + file_name_str)

    # Display the figure
    with open(anim_name,'rb') as anim:
        display(img(anim.read()))
    
    return