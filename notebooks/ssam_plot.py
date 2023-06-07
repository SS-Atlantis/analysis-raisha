import os
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import geopandas as gpd
import matplotlib.cm as cm
from ssam_groups import cohorts
from ssam_groups import bacteria
from PIL import Image
import glob
from IPython.display import Image as img

label_size = 11
font_size = 12
line_width = 2

def plot_benthic(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None) : # benthos, shellfish

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of benthic groups in Salish Sea Atlantis', fontsize = font_size)

    for species in group:
        benthic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        benthic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        ratio = benthic_oiled.sum(axis=1) / benthic_control.sum(axis=1) 
        control_ratio = benthic_control.sum(axis=1)  / benthic_control.sum(axis=1) 
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim(y_min, y_max)
    #ax.plot([spill_end, spill_end], [ratio.min(), ratio.max()], 'r',alpha=0.1)

def plot_pelagic(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of pelagic groups in Salish Sea Atlantis', fontsize = font_size)
 
    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes, take only water column layers
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled.sum(axis=1) / p_control.sum(axis=1) 
        control_ratio = p_control.sum(axis=1) / p_control.sum(axis=1)
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [rato.min(), rato.max()], 'r',alpha=0.1)

def plot_surface(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of groups in the surface of Salish Sea Atlantis', fontsize = font_size)

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,4:6], np.nan) # tonnes, take only water column layers
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled.sum(axis=1) / p_control.sum(axis=1) 
        control_ratio = p_control.sum(axis=1) / p_control.sum(axis=1)
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [ratio.min(), ratio.max()], 'r',alpha=0.1)

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

def plot_sediment(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Sediment groups in Salish Sea Atlantis', fontsize = font_size)

    for species in group:
        sed_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        sed_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        s_oiled = sed_oiled.sum(axis=1)
        s_control = sed_control.sum(axis=1)
        ratio = s_oiled / s_control
        control_ratio = s_control / s_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [ratio.min(), ratio.max()], 'r',alpha=0.1)

def plot_benthic_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): # benthos, shellfish

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Benthic groups in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        benthic_oiled = scenario.variables[group[species] + '_N'][start:end,box_number] # tonnes
        benthic_control = control.variables[group[species] + '_N'][start:end,box_number]
        ratio = benthic_oiled / benthic_control
        control_ratio = benthic_control / benthic_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
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

def plot_pelagic_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton
    
    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in pelagic groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled / p_control
        control_ratio = p_control / p_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_surface_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #bacteria, plankton
    
    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in surface groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled / p_control
        control_ratio = p_control / p_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_sediment_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): #mostly for sediment_feeders

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in sediment groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        s_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        s_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,6], np.nan)
        ratio = s_oiled / s_control
        control_ratio = s_control / s_control
        ax.plot(time[start:end], ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time[start:end], control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_cohorts(group, scenario, control, time, start, end, event_start):

    for species in group:

        numCohorts = cohorts[group[species]]

        o1_numbers = np.ma.zeros((scenario.variables[group[species] + '1_Nums'][start:end,:,:].shape),dtype = np.int32)
        o1_structuralN = np.ma.zeros((scenario.variables[group[species] + '1_StructN'][start:end,:,:].shape),dtype = np.int32)
        o1_reservedN = np.ma.zeros((scenario.variables[group[species] + '1_ResN'][start:end,:,:].shape),dtype = np.int32)

        c1_numbers = np.ma.zeros((control.variables[group[species] + '1_Nums'][start:end,:,:].shape),dtype = np.int32)
        c1_structuralN = np.ma.zeros((control.variables[group[species] + '1_StructN'][start:end,:,:].shape),dtype = np.int32)
        c1_reservedN = np.ma.zeros((control.variables[group[species] + '1_ResN'][start:end,:,:].shape),dtype = np.int32)    

        for cohort in range (1, numCohorts+1):

            new_species = group[species] + str(cohort)
        
            o1_numbers = o1_numbers + np.ma.filled(scenario.variables[new_species + '_Nums'][start:end,:,:], np.nan)
            o1_structuralN = o1_structuralN + np.ma.filled(scenario.variables[new_species +'_StructN'][start:end,:,:], np.nan)
            o1_reservedN = o1_reservedN + np.ma.filled(scenario.variables[new_species +'_ResN'][start:end,:,:], np.nan)

            c1_numbers = c1_numbers + np.ma.filled(control.variables[new_species + '_Nums'][start:end,:,:], np.nan)
            c1_structuralN = c1_structuralN + np.ma.filled(control.variables[new_species +'_StructN'][start:end,:,:], np.nan)
            c1_reservedN = c1_reservedN + np.ma.filled(control.variables[new_species +'_ResN'][start:end,:,:], np.nan)

        o2_numbers = o1_numbers.sum(axis=2)
        o2_structuralN = o1_structuralN.sum(axis=2)
        o2_reservedN = o1_reservedN.sum(axis=2)

        c2_numbers = c1_numbers.sum(axis=2)
        c2_structuralN = c1_structuralN.sum(axis=2)
        c2_reservedN = c1_reservedN.sum(axis=2)

        numbers = o2_numbers.sum(axis=1) / c2_numbers.sum(axis=1)
        structuralN = o2_structuralN.sum(axis=1) / c2_structuralN.sum(axis=1)
        reservedN = o2_reservedN.sum(axis=1) / c2_reservedN.sum(axis=1)
    
        fig, ax = plt.subplots(3,1, figsize = (14,9), sharex='all')
        ax[0].set_title('Numbers', fontsize = font_size)
        ax[0].set_ylabel('scenario : control')
        ax[0].tick_params(labelsize=label_size)
        ax[0].plot(time[start:end], numbers, linewidth = line_width)
        #ax[0].legend(group, loc='center left')
        ax[0].plot([event_start, event_start], [numbers.min(), numbers.max()], 'r', alpha=0.1)

        ax[1].set_title('Structural Nitrogen (bone size)', fontsize = font_size)
        ax[1].set_ylabel('scenario : control')
        ax[1].tick_params(labelsize=label_size)
        ax[1].plot(time[start:end], structuralN,linewidth = line_width)
        ax[1].plot([event_start, event_start], [structuralN.min(), structuralN.max()], 'r', alpha=0.1)

        ax[2].set_title('Reserve Nitrogen (fatty tissue)', fontsize = font_size)
        ax[2].set_ylabel('scenario : control')
        ax[2].tick_params(labelsize=label_size)
        ax[2].plot(time[start:end], reservedN,linewidth = line_width)
        ax[2].plot([event_start, event_start], [reservedN.min(), reservedN.max()], 'r', alpha=0.1);

def plot_pelagic_biomass(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None):

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1]) 

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$') 
        ax.set_title(str(group[species]), fontsize = font_size)
        ax.plot(time[start:end], p_oiled, label='scenario', linewidth = 2)
        ax.plot(time[start:end], p_control, 'k', label='control',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', label='event start', alpha=0.5)
        ax.set_ylim([y_min, y_max])
        #ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)  # to place the legend outside
    ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_benthic_biomass(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1]) 

    for species in group:

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]), fontsize = font_size)
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
        ax.set_ylim([y_min, y_max])
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_bacteria_biomass(scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    group = bacteria
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

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]), fontsize = font_size)
        ax.plot(time[start:end], b_oiled, linewidth = 2)
        ax.plot(time[start:end], b_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
        ax.set_ylim([y_min, y_max])
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);        

def plot_surface_biomass(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): # benthos, shellfish
    
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
       
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_sediment_biomass(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_pelagic_biomass_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None):

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$') 
        ax.set_title(str(group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_benthic_biomass_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 
    
    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])
   
    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_bacteria_biomass_box(scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    group = bacteria
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
        
        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], b_oiled, linewidth = 2)
        ax.plot(time[start:end], b_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_surface_biomass_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Surface Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_sediment_biomass_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig = plt.figure(figsize=(18, 14), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,6], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        
        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title(str(group[species]) + ' in Atlantis box ' + str(box_number), fontsize = font_size)
        ax.set_ylim([y_min, y_max])
        ax.plot(time[start:end], p_oiled, linewidth = 2)
        ax.plot(time[start:end], p_control, 'k',linewidth = 1)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
    ax.legend(['scenario', 'control', 'event start'], bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12);

def plot_pelagic_diff_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Pelagic Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_benthic_diff_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Benthic Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_sediment_diff_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Sediment Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,6], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_surface_diff_box(group, scenario, box_number, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference Surface Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    
    for species in group:

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
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

def plot_pelagic_diff(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Pelagic Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_benthic_diff(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Benthic Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max])

def plot_sediment_diff(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Sediment Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff, linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max]);

def plot_surface_diff(group, scenario, control, time, start, end, event_start, y_min=None, y_max=None): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference Surface Biomass in Salish Sea Atlantis', fontsize = font_size)

    for species in group:

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,4:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,4:6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time[start:end], diff,linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time[start:end], cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylim([y_min, y_max]);

def compare_pah(pah, scenario1, scenario2, scenario3, scenario4, time, start, end, event_start): 

    Phe1 = np.ma.filled(scenario1.variables[pah], np.nan)
    Phe2 = np.ma.filled(scenario2.variables[pah], np.nan)
    Phe3 = np.ma.filled(scenario3.variables[pah], np.nan)
    Phe4 = np.ma.filled(scenario4.variables[pah], np.nan)
    Phe1 = Phe1.sum(axis=2)
    Phe1 = Phe1.sum(axis=1)
    Phe2 = Phe2.sum(axis=2)
    Phe2 = Phe2.sum(axis=1)
    Phe3 = Phe3.sum(axis=2)
    Phe3 = Phe3.sum(axis=1)
    Phe4 = Phe4.sum(axis=2)
    Phe4 = Phe4.sum(axis=1)

    fig, ax = plt.subplots(figsize = (14,3))
    ax.plot(time[start:end], Phe1[start:end], time[start:end], Phe2[start:end], time[start:end], Phe3[start:end], time[start:end], Phe4[start:end])
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_title('Concentration of ' + pah + ' in Salish Sea Atlantis', fontsize = font_size)
    ax.set_ylabel('mg PAH m$^{-3}$')
    ax.legend(['scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'], loc='best');

def compare_pelagic_pah_in_bio(group, scenario1, scenario2, scenario3, scenario4, pah, time, start, end, event_start):

    for species in group:
        pelagic_oiled1 = scenario1.variables[group[species] + '_' + pah][start:end,:,:]
        pelagic_oiled2 = scenario2.variables[group[species] + '_' + pah][start:end,:,:]
        pelagic_oiled3 = scenario3.variables[group[species] + '_' + pah][start:end,:,:]
        pelagic_oiled4 = scenario4.variables[group[species] + '_' + pah][start:end,:,:]
        # sum over depth
        p_oiled1 = pelagic_oiled1.sum(axis=2)
        p_oiled2 = pelagic_oiled2.sum(axis=2)
        p_oiled3 = pelagic_oiled3.sum(axis=2)
        p_oiled4 = pelagic_oiled4.sum(axis=2)
        # sum over boxes
        p_oiled1 = pelagic_oiled1.sum(axis=1)
        p_oiled2 = pelagic_oiled2.sum(axis=1)
        p_oiled3 = pelagic_oiled3.sum(axis=1)
        p_oiled4 = pelagic_oiled4.sum(axis=1)
        fig, ax = plt.subplots(figsize = (14,3))
        ax.plot(time[start:end], p_oiled1, time[start:end], p_oiled2, time[start:end], p_oiled3, time[start:end], p_oiled4, linewidth = 2)
        ax.set_title(pah + ' inside ' + species)
        ax.set_ylabel('mgPAH')
        ax.plot(event_start, 0, 'ro', alpha=0.5)
        ax.legend(['scenario 1', 'scenario 2', 'scenario 3', 'scenario 4']);

def compare_pelagic_pah_in_bio_box(group, scenario1, scenario2, scenario3, scenario4, box_number, pah, time, start, end, event_start):

    for species in group:
        pelagic_oiled1 = scenario1.variables[group[species] + '_' + pah][start:end,box_number,:]
        pelagic_oiled2 = scenario2.variables[group[species] + '_' + pah][start:end,box_number,:]
        pelagic_oiled3 = scenario3.variables[group[species] + '_' + pah][start:end,box_number,:]
        pelagic_oiled4 = scenario4.variables[group[species] + '_' + pah][start:end,box_number,:]
        p_oiled1 = pelagic_oiled1.sum(axis=1)
        p_oiled2 = pelagic_oiled2.sum(axis=1)
        p_oiled3 = pelagic_oiled3.sum(axis=1)
        p_oiled4 = pelagic_oiled4.sum(axis=1)
        fig, ax = plt.subplots(figsize = (14,3))
        ax.plot(time[start:end], p_oiled1, time[start:end], p_oiled2, time[start:end], p_oiled3, time[start:end], p_oiled4, linewidth = 2)
        ax.set_title(species)
        ax.set_ylabel('mgPAH')
        ax.plot(event_start, 0, 'ro', alpha=0.5)
        ax.legend(['scenario 1', 'scenario 2', 'scenario 3', 'scenario 4']);

def boxplot_pelagic(group, scenario, control, days, data_labels, x_lim=None, bio_colours=['#063764','#0b5394','#3d85c6','#6fa8dc','#9fc5e8']): #bacteria, plankton
    
    df = pd.DataFrame(data_labels)
    spp = []
    
    for species in group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][day,:,0:6], np.nan) # tonnes, take only water column layers
            p_control = np.ma.filled(control.variables[group[species] + '_N'][day,:,0:6], np.nan)
            p_oiled = p_oiled.sum(axis=1)
            p_oiled = p_oiled.sum(axis=0)
            p_control = p_control.sum(axis=1)
            p_control = p_control.sum(axis=0)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')

    df1.plot(kind="barh", subplots=True, layout=(1,len(days)), figsize=(15,4), sharey=True, sharex=True, color=bio_colours, legend=None,
         xlabel='Pelagic Groups', ylabel=None, title='Percent (%) Change Relative to Control for Select Pelagic Groups', xlim=x_lim); 

def boxplot_pelagic_all(group, scenarios, control, days, data_labels, x_lim=None): #bacteria, plankton
    
    for item in scenarios:
        boxplot_pelagic(group, item, control, days, data_labels, x_lim=None)
    

def boxplot_benthic(group, scenario, control, days, data_labels, x_lim=None, bio_colours=['#783f04','#b45f06','#e69138','#f6b26b','#f9cb9c']): 

    df = pd.DataFrame(data_labels)
    spp = []

    for species in group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][day,:], np.nan) # tonnes, take only water column layers
            p_control = np.ma.filled(control.variables[group[species] + '_N'][day,:], np.nan)
            p_oiled = p_oiled.sum(axis=0)
            p_control = p_control.sum(axis=0)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')

    df1.plot(kind="barh", subplots=True, layout=(1,len(days)), figsize=(15,6), sharey=True, sharex=True, color=bio_colours, legend=None,
         xlabel='Benthic Groups', ylabel=None, title='Percent (%) Change Relative to Control for Select Benthic Groups', xlim=x_lim);

def boxplot_benthic_all(group, scenarios, control, days, data_labels, x_lim=None): #bacteria, plankton
    
    for item in scenarios:
        boxplot_benthic(group, item, control, days, data_labels, x_lim=None)

def boxplot_sediment(group, scenario, control, days, data_labels, x_lim=None, bio_colours=['#783f04','#b45f06','#e69138','#f6b26b','#f9cb9c']):
    
    df = pd.DataFrame(data_labels)
    spp = []
    
    for species in group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][day,:,6], np.nan) # tonnes, only sediment layers
            p_control = np.ma.filled(control.variables[group[species] + '_N'][day,:,6], np.nan)
            p_oiled = p_oiled.sum(axis=0)
            p_control = p_control.sum(axis=0)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')

    df1.plot(kind="barh", subplots=True, layout=(1,len(days)), figsize=(15,4), sharey=True, sharex=True, color=bio_colours, legend=None,
         xlabel='Pelagic Groups', ylabel=None, title='Percent (%) Change Relative to Control for Select Sedimentary Groups', xlim=x_lim); 

def boxplot_sediment_all(group, scenarios, control, days, data_labels, x_lim=None):
    
    for item in scenarios:
        boxplot_sediment(group, item, control, days, data_labels, x_lim=None)

def benthic_compare_scenarios(group, scenario1, scenario2, scenario3, scenario4, control, time, start, end, y_min=None, y_max=None): # benthos, shellfish

    # Plot variables
    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        benthic_oiled1 = np.ma.filled(scenario1.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        benthic_oiled2 = np.ma.filled(scenario2.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        benthic_oiled3 = np.ma.filled(scenario3.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        benthic_oiled4 = np.ma.filled(scenario4.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        benthic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        ratio1 = (benthic_oiled1.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio2 = (benthic_oiled2.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio3 = (benthic_oiled3.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio4 = (benthic_oiled4.sum(axis=1) / benthic_control.sum(axis=1)-1)*100
        control_ratio = (benthic_control.sum(axis=1)  / benthic_control.sum(axis=1)-1)*100
        
        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        
        ax.plot(time[start:end], control_ratio, 'k', time[start:end], ratio1, time[start:end], ratio2, time[start:end], ratio3, time[start:end], ratio4, linewidth = 2)
        ax.set_ylim([y_min, y_max])
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(species);

def pelagic_compare_scenarios(group, scenario1, scenario2, scenario3, scenario4, control, time, start, end, y_min=None, y_max=None): #bacteria, plankton, sharks, birds, mammals, named_fish, salmon, fish, benth_feeders

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        pelagic_oiled1 = np.ma.filled(scenario1.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_oiled2 = np.ma.filled(scenario2.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_oiled3 = np.ma.filled(scenario3.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_oiled4 = np.ma.filled(scenario4.variables[group[species] + '_N'][start:end,:,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:6], np.nan)
        # sum across depth
        pelagic_oiled1 = pelagic_oiled1.sum(axis=2) 
        pelagic_oiled2 = pelagic_oiled2.sum(axis=2) 
        pelagic_oiled3 = pelagic_oiled3.sum(axis=2) 
        pelagic_oiled4 = pelagic_oiled4.sum(axis=2) 
        pelagic_control = pelagic_control.sum(axis=2)
        # sum across boxes
        ratio1 = (pelagic_oiled1.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100
        ratio2 = (pelagic_oiled2.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100 
        ratio3 = (pelagic_oiled3.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100
        ratio4 = (pelagic_oiled4.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100
        control_ratio = (pelagic_control.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.plot(time[start:end], control_ratio, 'k', time[start:end], ratio1, time[start:end], ratio2, time[start:end], ratio3, time[start:end], ratio4,linewidth = 2)
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(species)
        ax.set_ylim([y_min, y_max]);

def sediment_compare_scenarios(group, scenario1, scenario2, scenario3, scenario4, control, time, start, end, y_min=None, y_max=None): # benthos, shellfish

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        benthic_oiled1 = np.ma.filled(scenario1.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        benthic_oiled2 = np.ma.filled(scenario2.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        benthic_oiled3 = np.ma.filled(scenario3.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        benthic_oiled4 = np.ma.filled(scenario4.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        benthic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        ratio1 = (benthic_oiled1.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio2 = (benthic_oiled2.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio3 = (benthic_oiled3.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio4 = (benthic_oiled4.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        control_ratio = (benthic_control.sum(axis=1)  / benthic_control.sum(axis=1)-1)*100
        
        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        
        ax.plot(time[start:end], control_ratio, 'k', time[start:end], ratio1, time[start:end], ratio2, time[start:end], ratio3, time[start:end], ratio4, linewidth = 2)
        ax.set_ylim([y_min, y_max])
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3'])
        ax.set_title(species);

def pelagic_compare_nutrients(group, scenario1, scenario2, scenario3, scenario4, control, time, start, end, y_min=None, y_max=None): #bacteria, plankton, sharks, birds, mammals, named_fish, salmon, fish, benth_feeders

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        pelagic_oiled1 = np.ma.filled(scenario1.variables[group[species]][start:end,:,0:6], np.nan) # tonnes
        pelagic_oiled2 = np.ma.filled(scenario2.variables[group[species]][start:end,:,0:6], np.nan) # tonnes
        pelagic_oiled3 = np.ma.filled(scenario3.variables[group[species]][start:end,:,0:6], np.nan) # tonnes
        pelagic_oiled4 = np.ma.filled(scenario4.variables[group[species]][start:end,:,0:6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species]][start:end,:,0:6], np.nan)
        # sum across depth
        pelagic_oiled1 = pelagic_oiled1.sum(axis=2) 
        pelagic_oiled2 = pelagic_oiled2.sum(axis=2) 
        pelagic_oiled3 = pelagic_oiled3.sum(axis=2) 
        pelagic_oiled4 = pelagic_oiled4.sum(axis=2) 
        pelagic_control = pelagic_control.sum(axis=2)
        # sum across boxes
        ratio1 = (pelagic_oiled1.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100
        ratio2 = (pelagic_oiled2.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100 
        ratio3 = (pelagic_oiled3.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100
        ratio4 = (pelagic_oiled4.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100
        control_ratio = (pelagic_control.sum(axis=1) / pelagic_control.sum(axis=1)-1)*100

        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        ax.plot(time[start:end], control_ratio, 'k', time[start:end], ratio1, time[start:end], ratio2, time[start:end], ratio3, time[start:end], ratio4,linewidth = 2)
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3', 'scenario 4'])
        ax.set_title(species)
        ax.set_ylim([y_min, y_max]);

def sediment_compare_nutrients(group, scenario1, scenario2, scenario3, scenario4, control, time, start, end, y_min=None, y_max=None): # benthos, shellfish

    fig = plt.figure(figsize=(18, 18), facecolor='white')
    gs = plt.GridSpec(3, 3, wspace=0.2, hspace=0.2, width_ratios=[1, 1, 1], height_ratios=[1, 1, 1])

    for species in group:
        benthic_oiled1 = np.ma.filled(scenario1.variables[group[species]][start:end,:,6], np.nan) # tonnes
        benthic_oiled2 = np.ma.filled(scenario2.variables[group[species]][start:end,:,6], np.nan) # tonnes
        benthic_oiled3 = np.ma.filled(scenario3.variables[group[species]][start:end,:,6], np.nan) # tonnes
        benthic_oiled4 = np.ma.filled(scenario4.variables[group[species]][start:end,:,6], np.nan) # tonnes
        benthic_control = np.ma.filled(control.variables[group[species]][start:end,:,6], np.nan)
        ratio1 = (benthic_oiled1.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio2 = (benthic_oiled2.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio3 = (benthic_oiled3.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        ratio4 = (benthic_oiled4.sum(axis=1) / benthic_control.sum(axis=1)-1)*100 
        control_ratio = (benthic_control.sum(axis=1)  / benthic_control.sum(axis=1)-1)*100
        
        bio_index = (list(group).index(species))

        if bio_index < 3:
            position = 0, bio_index
        elif bio_index > 5: 
            position = 2, bio_index-6
        else :
            position = 1, bio_index-3

        ax = fig.add_subplot(gs[position])
        
        ax.plot(time[start:end], control_ratio, 'k', time[start:end], ratio1, time[start:end], ratio2, time[start:end], ratio3, time[start:end], ratio4, linewidth = 2)
        ax.set_ylim([y_min, y_max])
        plt.ylabel('Percent (%) change', fontsize=12)
        ax.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3'])
        ax.set_title(species);

def map_pelagic_aggregate_time4(variable_name, scenario1, scenario2, scenario3, scenario4, control, v_max=100, v_min=-100):
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    
    # map of single variable ratio across the whole simulation

    # Pull variables for all scenarios
    dVar_control = control.variables[variable_name]
    dVar_s1 = scenario1.variables[variable_name]
    dVar_s2 = scenario2.variables[variable_name]
    dVar_s3 = scenario3.variables[variable_name]
    dVar_s4 = scenario4.variables[variable_name]

    # Aggregate across depths
    dVar_control = dVar_control.sum(axis=2)
    dVar_s1 = dVar_s1.sum(axis=2)
    dVar_s2 = dVar_s2.sum(axis=2)
    dVar_s3 = dVar_s3.sum(axis=2)
    dVar_s4 = dVar_s4.sum(axis=2)

    _cmap = cm.bwr # cm.ocean_r
    land_df = map_df.loc[land_boxes]

    ## Aggregate across time
    dVar_control = dVar_control.sum(axis=0)
    dVar_s1 = dVar_s1.sum(axis=0)
    dVar_s2 = dVar_s2.sum(axis=0)
    dVar_s3 = dVar_s3.sum(axis=0)
    dVar_s4 = dVar_s4.sum(axis=0)
    
    s1_oil = (dVar_s1 / dVar_control-1)*100 
    s2_oil = (dVar_s2 / dVar_control-1)*100  
    s3_oil = (dVar_s3 / dVar_control-1)*100  
    s4_oil = (dVar_s4 / dVar_control-1)*100  

    # Add scenario data to Atlantis spatial data
    map_df['scen_1'] = s1_oil
    map_df['scen_2'] = s2_oil
    map_df['scen_3'] = s3_oil
    map_df['scen_4'] = s4_oil
    map_df.loc[land_boxes, 'scen_1'] = 0
    map_df.loc[land_boxes, 'scen_2'] = 0
    map_df.loc[land_boxes, 'scen_3'] = 0
    map_df.loc[land_boxes, 'scen_4'] = 0

    fig = plt.figure(figsize=(29, 8), facecolor='white') #figsize=(9, 12)
    gs = plt.GridSpec(1, 4, wspace=0.5, hspace=0.2, width_ratios=[1, 1, 1, 1], height_ratios=[1],)

    ax = fig.add_subplot(gs[0, 0])    
    ax = map_df.plot(column = 'scen_1', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax,
        legend=True, legend_kwds={'label': 'Scenario 1: ' + variable_name
        },)
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white')

    ax = fig.add_subplot(gs[0, 1])
    ax = map_df.plot(column = 'scen_2', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax,
        legend=True, legend_kwds={'label': 'Scenario 2: ' + variable_name
        },)
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white') 

    ax = fig.add_subplot(gs[0, 2])
    ax = map_df.plot(column = 'scen_3', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax,
        legend=True, legend_kwds={'label': 'Scenario 3: ' + variable_name
        },)
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white');

    ax = fig.add_subplot(gs[0, 3])
    ax = map_df.plot(column = 'scen_4', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax,
        legend=True, legend_kwds={'label': 'Scenario 4: ' + variable_name
        },)
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white');
    
    return

def map_pelagic_aggregate_time(variable_name, scenario, control, v_max=100, v_min=-100):
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    
    # map of single variable ratio across the whole simulation

    # Pull variables for all scenarios
    dVar_control = control.variables[variable_name]
    dVar_s = scenario.variables[variable_name]

    # Aggregate across depths
    dVar_control = dVar_control.sum(axis=2)
    dVar_s = dVar_s.sum(axis=2)

    _cmap = cm.bwr # cm.ocean_r
    land_df = map_df.loc[land_boxes]

    ## Aggregate across time
    dVar_control = dVar_control.sum(axis=0)
    dVar_s = dVar_s.sum(axis=0)

    percent_oil = (dVar_s / dVar_control-1)*100 

    # Add scenario data to Atlantis spatial data
    map_df['percent'] = percent_oil
    map_df.loc[land_boxes, 'percent'] = 0

    fig = plt.figure(figsize=(9, 12))

    ax = fig.add_subplot()
    ax = map_df.plot(column = 'percent', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max,
        legend=True, legend_kwds={'label': variable_name + ' % difference from control'
        },)
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white');
    
    return

def map_pelagic_single_time(variable_name, scenario1, scenario2, scenario3, control, time, time_index, start, end, event_start, v_max=100, v_min=-100):
    # map of single variable ratio at a specific time index
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])

    ts_date = np.array(time[time_index])

    # Pull variables for all scenarios
    dVar_control = control.variables[variable_name]
    dVar_s1 = scenario1.variables[variable_name]
    dVar_s2 = scenario2.variables[variable_name]
    dVar_s3 = scenario3.variables[variable_name]

    # Aggregate across depths
    dVar_control = dVar_control.sum(axis=2)
    dVar_s1 = dVar_s1.sum(axis=2)
    dVar_s2 = dVar_s2.sum(axis=2)
    dVar_s3 = dVar_s3.sum(axis=2)

    # Aggregate across boxes and take ratio, for summary main graph
    bVar_control = dVar_control.sum(axis=1)
    bVar_s1 = (dVar_s1.sum(axis=1) / bVar_control-1)*100
    bVar_s2 = (dVar_s2.sum(axis=1) / bVar_control-1)*100
    bVar_s3 = (dVar_s3.sum(axis=1) / bVar_control-1)*100
    bVar_control = (bVar_control / bVar_control-1)*100

    ## Select specific time period
    tVar_control = dVar_control[time_index,:]
    tVar_s1 = dVar_s1[time_index,:]
    tVar_s2 = dVar_s2[time_index,:]
    tVar_s3 = dVar_s3[time_index,:]

    s1_oil = (tVar_s1 / tVar_control -1)*100
    s2_oil = (tVar_s2 / tVar_control -1)*100
    s3_oil = (tVar_s3 / tVar_control -1)*100

    # Add scenario data to Atlantis spatial data
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    _cmap = cm.bwr # cm.ocean_r cm.PuOr_r
    land_df = map_df.loc[land_boxes]
    map_df['scen_1'] = s1_oil
    map_df['scen_2'] = s2_oil
    map_df['scen_3'] = s3_oil
    map_df.loc[land_boxes, 'scen_1'] = 0
    map_df.loc[land_boxes, 'scen_2'] = 0
    map_df.loc[land_boxes, 'scen_3'] = 0

    fig = plt.figure(figsize=(18, 13), facecolor='white')
    gs = plt.GridSpec(2, 3, width_ratios=[1, 1, 1.2], height_ratios=[1, 3])

    ax_ts = fig.add_subplot(gs[0, :])
    ax_ts.plot(time[start:end], bVar_control[start:end], 'k', time[start:end], bVar_s1[start:end], time[start:end], bVar_s2[start:end], time[start:end], bVar_s3[start:end], linewidth = line_width)
    ax_ts.plot([ts_date, ts_date], [v_min, v_max], 'k--')
    ax_ts.plot(event_start, 1, 'ro', alpha=0.4)
    ax_ts.set_ylabel('Percent (%) Change', fontsize = label_size)
    ax_ts.set_ylim([v_min, v_max])
    ax_ts.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3']) #, loc='center right'
    ax_ts.tick_params(labelsize=label_size)

    ax = fig.add_subplot(gs[1, 0])
    ax = map_df.plot(column = 'scen_1', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max,
         legend=False, 
        # legend_kwds={'label': variable_name + scenario1_name },
        )
    ax.set_title('Scenario 1: ' + variable_name, fontsize = 12, color = '#2e7fb8')
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white')

    ax = fig.add_subplot(gs[1, 1])
    ax = map_df.plot(column = 'scen_2', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max, 
         legend=False, 
        # legend_kwds={'label': variable_name + scenario2_name },
        )
    ax.set_title('Scenario 2: ' + variable_name, fontsize = 12, color = '#ff7f0e')
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white') 

    ax = fig.add_subplot(gs[1, 2])
    # divider = make_axes_locatable(ax)
    # _cax = divider.append_axes('right',size='5%', pad=0.1)
    ax = map_df.plot(column = 'scen_3', cmap=_cmap, ax=ax, vmin=v_min, vmax=v_max, #cax=_cax, 
        legend=True, legend_kwds={'label': 'Percent (%) Change'
        },)
    ax.set_title('Scenario 3: ' + variable_name, fontsize = 12, color = '#399f2c')
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white');
    ax = fig.suptitle('Percent Change in ' + variable_name + ' at ' + str(ts_date), fontsize=12)
    #ax.legend(cmap=_cmap) 

    return

def animate_map_pelagic(variable_name, scenario1, scenario2, scenario3, control, time, start, end, event_start, v_max=100, v_min=-100):
    # animation of map of single variable ratio over time

    file_names = []

    for time_index in range(start, end):
    
        map_pelagic_single_time(variable_name, scenario1, scenario2, scenario3, control, time, time_index, start, end, event_start)
        
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

def map_benthic_single_time(variable_name, scenario1, scenario2, scenario3, control, time, time_index, start, end, event_start, v_max=100, v_min=-100):
    # map of single variable ratio at a specific time index
    
    shapefile_name = "/ocean/rlovindeer/Atlantis/ssam_oceanparcels/SalishSea/SalishSea_July172019_2/SalishSea_July172019.shp"
    map_df = gpd.read_file(shapefile_name)
    map_df = map_df.sort_values(by=['BOX_ID'])

    ts_date = np.array(time[time_index])

    # Pull variables for all scenarios
    dVar_control = control.variables[variable_name]
    dVar_s1 = scenario1.variables[variable_name]
    dVar_s2 = scenario2.variables[variable_name]
    dVar_s3 = scenario3.variables[variable_name]

    _cmap = cm.bwr # cm.ocean_r cm.PuOr_r

    # Aggregate across boxes and take ratio, for summary main graph
    bVar_control = dVar_control.sum(axis=1)
    bVar_s1 = (dVar_s1.sum(axis=1) / bVar_control-1)*100
    bVar_s2 = (dVar_s2.sum(axis=1) / bVar_control-1)*100
    bVar_s3 = (dVar_s3.sum(axis=1) / bVar_control-1)*100
    bVar_control = (bVar_control / bVar_control-1)*100
    f_min = bVar_s3.min()
    f_max = bVar_s3.max()

    ## Select specific time period
    dVar_control = dVar_control[time_index,:]
    dVar_s1 = dVar_s1[time_index,:]
    dVar_s2 = dVar_s2[time_index,:]
    dVar_s3 = dVar_s3[time_index,:]

    s1_oil = (dVar_s1 / dVar_control -1)*100
    s2_oil = (dVar_s2 / dVar_control -1)*100
    s3_oil = (dVar_s3 / dVar_control -1)*100

    # Add scenario data to Atlantis spatial data
    box_depth = map_df['BOTZ']
    land_boxes = box_depth==0
    land_boxes = map_df.index[land_boxes]
    land_df = map_df.loc[land_boxes]
    map_df['scen_1'] = s1_oil
    map_df['scen_2'] = s2_oil
    map_df['scen_3'] = s3_oil
    map_df.loc[land_boxes, 'scen_1'] = 0
    map_df.loc[land_boxes, 'scen_2'] = 0
    map_df.loc[land_boxes, 'scen_3'] = 0

    fig = plt.figure(figsize=(18, 13), facecolor='white')
    gs = plt.GridSpec(2, 3, width_ratios=[1, 1, 1.2], height_ratios=[1, 3])

    ax_ts = fig.add_subplot(gs[0, :])
    ax_ts.plot(time[start:end], bVar_control[start:end], 'k', time[start:end], bVar_s1[start:end], time[start:end], bVar_s2[start:end], time[start:end], bVar_s3[start:end], linewidth = line_width)
    ax_ts.plot([ts_date, ts_date], [f_min, f_max], 'k--')
    ax_ts.plot(event_start, 1, 'ro', alpha=0.4)
    ax_ts.set_ylabel('ratio to control', fontsize = label_size)
    ax_ts.set_ylim([v_min, v_max])
    ax_ts.legend(['control', 'scenario 1', 'scenario 2', 'scenario 3']) #, loc='center right'
    ax_ts.tick_params(labelsize=label_size)

    ax = fig.add_subplot(gs[1, 0])
    ax = map_df.plot(column = 'scen_1', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax,
         legend=False, 
        # legend_kwds={'label': variable_name + scenario1_name },
        )
    ax.set_title('Scenario 1: ' + variable_name, fontsize = 12, color = 'blue')
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white')

    ax = fig.add_subplot(gs[1, 1])
    ax = map_df.plot(column = 'scen_2', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax,
         legend=False, 
        # legend_kwds={'label': variable_name + scenario2_name },
        )
    ax.set_title('Scenario 2: ' + variable_name, fontsize = 12,  color = 'orange')
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white') 

    ax = fig.add_subplot(gs[1, 2])
    # divider = make_axes_locatable(ax)
    # _cax = divider.append_axes('right',size='5%', pad=0.1)
    ax = map_df.plot(column = 'scen_3', cmap=_cmap, vmin=v_min, vmax=v_max, ax=ax, #cax=_cax,
        legend=True, legend_kwds={'label': 'scenario : control'
        },)
    ax.set_title('Scenario 3: ' + variable_name, fontsize = 12,  color = 'green')
    map_df.boundary.plot(ax=ax, color='grey', linewidths=0.7)
    land_df.plot(ax=ax, color='white');
    ax = fig.suptitle('Ratio of Control to Scenario at time ' + str(ts_date), fontsize=12)
    #ax.legend(cmap=_cmap) 

    return

def animate_map_benthic(variable_name, scenario1, scenario2, scenario3, control, time, start, end, event_start, v_max=100, v_min=-100):
    # animation of single variable ratio over time

    file_names = []

    for time_index in range(start, end):
    
        map_benthic_single_time(variable_name, scenario1, scenario2, scenario3, control, time, time_index, start, end, event_start)
        
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