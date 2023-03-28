
import matplotlib.pyplot as plt
import numpy as np
from ssam_groups.py import cohorts
from ssam_groups.py import bacteria

label_size = 11
font_size = 12
line_width = 2

def plot_benthic(group, scenario, control, time, start, end, event_start) : # benthos, shellfish

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of benthic groups in Salish Sea Atlantis', fontsize = font_size)
    ax.set_ylim(y_min, y_max)

    for species in group:
        benthic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        benthic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        ratio = benthic_oiled.sum(axis=1) / benthic_control.sum(axis=1) 
        control_ratio = benthic_control.sum(axis=1)  / benthic_control.sum(axis=1) 
        ax.plot(time, ratio, linewidth = 2)
    
    y_max = benthic_oiled.max()
    y_min = benthic_oiled.min()
    ax.legend(group) #, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_pelagic(group, scenario, control, time, start, end, event_start): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of pelagic groups in Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,0:5], np.nan) # tonnes, take only water column layers
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled.sum(axis=1) / p_control.sum(axis=1) 
        control_ratio = p_control.sum(axis=1) / p_control.sum(axis=1)
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_surface(group, scenario, control, time, start, end, event_start):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of groups in the surface of Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,4:5], np.nan) # tonnes, take only water column layers
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,4:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled.sum(axis=1) / p_control.sum(axis=1) 
        control_ratio = p_control.sum(axis=1) / p_control.sum(axis=1)
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_bacteria(scenario, control, time, start, end, event_start):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Bacteria groups in Salish Sea Atlantis', fontsize = font_size)
    # ax.set_ylim([y_min, y_max])

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,0:5], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,0:5,], np.nan)
            b_oiled = bact_oiled.sum(axis=2)
            b_control = bact_control.sum(axis=2)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,6], np.nan)
        
        ratio = b_oiled.sum(axis=1) / b_control.sum(axis=1) 
        control_ratio = b_control.sum(axis=1) / b_control.sum(axis=1)
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(bacteria, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_sediment(group, scenario, control, time, start, end, event_start): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Sediment groups in Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        sed_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        sed_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        s_oiled = sed_oiled.sum(axis=1)
        s_control = sed_control.sum(axis=1)
        ratio = s_oiled / s_control
        control_ratio = s_control / s_control
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_benthic_box(group, scenario, box_number, control, time, start, end, event_start): # benthos, shellfish

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change relative to control of Benthic groups in Salish Sea Atlantis', fontsize = font_size)
    # ax.set_ylim(y_min, y_max)

    for species in group:
        benthic_oiled = scenario.variables[group[species] + '_N'][start:end,box_number] # tonnes
        benthic_control = control.variables[group[species] + '_N'][start:end,box_number]
        ratio = benthic_oiled / benthic_control
        control_ratio = benthic_control / benthic_control
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_bacteria_box(scenario, box_number, control, time, start, end, event_start): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in bacteria relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    # ax.set_ylim([y_min, y_max])

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,0:5], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,0:5], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan)
        
        ratio = b_oiled / b_control
        control_ratio = b_control / b_control
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(bacteria, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_pelagic_box(group, scenario, box_number, control, time, start, end, event_start): #bacteria, plankton
    
    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in pelagic groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,0:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,0:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled / p_control
        control_ratio = p_control / p_control
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_surface_box(group, scenario, box_number, control, time, start, end, event_start): #bacteria, plankton
    
    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in surface groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,4:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,4:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        ratio = p_oiled / p_control
        control_ratio = p_control / p_control
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)
    #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_sediment_box(group, scenario, box_number, control, time, start, end, event_start): #mostly for sediment_feeders

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario:control')
    ax.set_title('Change in sediment groups relative to control in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        s_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        s_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,6], np.nan)
        ratio = s_oiled / s_control
        control_ratio = s_control / s_control
        ax.plot(time, ratio, linewidth = 2)
    
    ax.legend(group, loc='center left')
    ax.plot(time, control_ratio, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_cohorts(group, scenario, control, time, start, end, event_start):

    fig, ax = plt.subplots(3,1, figsize = (14,9), sharex='all')
    ax[0].set_title('Numbers - all cohorts', fontsize = font_size)
    ax[0].set_ylabel('scenario : control')
    ax[0].tick_params(labelsize=label_size)

    ax[1].set_title('Structural Nitrogen (bone size) - all cohorts', fontsize = font_size)
    ax[1].set_ylabel('scenario : control')
    ax[1].tick_params(labelsize=label_size)

    ax[2].set_title('Reserve Nitrogen (fatty tissue) - all cohorts', fontsize = font_size)
    ax[2].set_ylabel('scenario : control')
    ax[2].tick_params(labelsize=label_size)

    for species in group:

        numCohorts = cohorts[group[species]]

        o1_numbers = np.ma.zeros((scenario.variables[group[species] + '1_Nums'].shape),dtype = np.int32)
        o1_structuralN = np.ma.zeros((scenario.variables[group[species] + '1_StructN'].shape),dtype = np.int32)
        o1_reservedN = np.ma.zeros((scenario.variables[group[species] + '1_ResN'].shape),dtype = np.int32)

        c1_numbers = np.ma.zeros((control.variables[group[species] + '1_Nums'].shape),dtype = np.int32)
        c1_structuralN = np.ma.zeros((control.variables[group[species] + '1_StructN'].shape),dtype = np.int32)
        c1_reservedN = np.ma.zeros((control.variables[group[species] + '1_ResN'].shape),dtype = np.int32)    

        for cohort in range (1, numCohorts+1):

            new_species = group[species] + str(cohort)
        
            o1_numbers = o1_numbers + np.ma.filled(scenario.variables[new_species + '_Nums'][:,:,:], np.nan)
            o1_structuralN = o1_structuralN + np.ma.filled(scenario.variables[new_species +'_StructN'][:,:,:], np.nan)
            o1_reservedN = o1_reservedN + np.ma.filled(scenario.variables[new_species +'_ResN'][:,:,:], np.nan)

            c1_numbers = c1_numbers + np.ma.filled(control.variables[new_species + '_Nums'][:,:,:], np.nan)
            c1_structuralN = c1_structuralN + np.ma.filled(control.variables[new_species +'_StructN'][:,:,:], np.nan)
            c1_reservedN = c1_reservedN + np.ma.filled(control.variables[new_species +'_ResN'][:,:,:], np.nan)

        o2_numbers = o1_numbers.sum(axis=2)
        o2_structuralN = o1_structuralN.sum(axis=2)
        o2_reservedN = o1_reservedN.sum(axis=2)

        c2_numbers = c1_numbers.sum(axis=2)
        c2_structuralN = c1_structuralN.sum(axis=2)
        c2_reservedN = c1_reservedN.sum(axis=2)

        numbers = o2_numbers.sum(axis=1) / c2_numbers.sum(axis=1)
        structuralN = o2_structuralN.sum(axis=1) / c2_structuralN.sum(axis=1)
        reservedN = o2_reservedN.sum(axis=1) / c2_reservedN.sum(axis=1)
    
        ax[0].plot(time, numbers[start:end], linewidth = line_width)
        ax[0].legend(group, loc='center left')
        ax[0].plot([event_start, event_start], [numbers.min(), numbers.max()], 'r', alpha=0.1)
        #ax[0].plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)
   
        ax[1].plot(time, structuralN[start:end],linewidth = line_width)
        ax[1].plot([event_start, event_start], [structuralN.min(), structuralN.max()], 'r', alpha=0.1)
        #ax[1].plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

        ax[2].plot(time, reservedN[start:end],linewidth = line_width)
        ax[2].plot([event_start, event_start], [reservedN.min(), reservedN.max()], 'r', alpha=0.1)
        #ax[2].plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_pelagic_biomass(group, scenario, control, time, start, end, event_start):

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$') 
        ax.set_title('Pelagic Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis', fontsize = font_size)
        #ax.set_ylim([y_min, y_max])
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,0:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = p_oiled.sum(axis=1)
        p_control = p_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_benthic_biomass(group, scenario, control, time, start, end, event_start): 

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Benthic Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis', fontsize = font_size)
        #ax.set_ylim([y_min, y_max])
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_bacteria_biomass(scenario, control, time, start, end, event_start): 

    group = bacteria

    for species in bacteria:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis', fontsize = font_size)
        #ax.set_ylim([y_min, y_max])

        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,0:5], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,0:5], np.nan)
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
        ax.plot(time, b_oiled, linewidth = 2)
        ax.plot(time, b_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_surface_biomass(group, scenario, control, time, start, end, event_start): # benthos, shellfish

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Surface Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis', fontsize = font_size)
        #ax.set_ylim([y_min, y_max])

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,4:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,4:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
        #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_sediment_biomass(group, scenario, control, time, start, end, event_start): 

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Sediment Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis', fontsize = font_size)
        #ax.set_ylim([y_min, y_max])
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_pelagic_biomass_box(group, scenario, box_number, control, time, start, end, event_start):

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$') 
        ax.set_title('Pelagic Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        #ax.set_ylim([y_min, y_max])
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,0:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,0:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_benthic_biomass_box(group, scenario, box_number, control, time, start, end, event_start): 

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Benthic Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        #ax.set_ylim([y_min, y_max])
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_bacteria_biomass_box(scenario, box_number, control, time, start, end, event_start): 

    group = bacteria

    for species in bacteria:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        #ax.set_ylim([y_min, y_max])

        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,0:5], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,0:5], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan)
        
        p_max = b_oiled.max()
        p_min = b_oiled.min()
        ax.plot(time, b_oiled, linewidth = 2)
        ax.plot(time, b_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_surface_biomass_box(group, scenario, box_number, control, time, start, end, event_start): # benthos, shellfish

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Surface Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        #ax.set_ylim([y_min, y_max])

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,4:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,4:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)
        #ax.plot([spill_end, spill_end], [y_min, y_max], 'r',alpha=0.1)

def plot_sediment_biomass_box(group, scenario, box_number, control, time, start, end, event_start): 

    for species in group:
        fig, ax = plt.subplots(figsize = (14,3))
        ax.tick_params(labelsize=label_size)
        ax.set_ylabel('mg N$^{-3}$')
        ax.set_title('Sediment Biomass of ' + str(group[species]) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
        #ax.set_ylim([y_min, y_max])
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,6], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        p_max = p_oiled.max()
        p_min = p_oiled.min()
        ax.plot(time, p_oiled, linewidth = 2)
        ax.plot(time, p_control, 'k',linewidth = 2)
        ax.plot([event_start,event_start],[p_min, p_max], 'r', alpha=0.5)

def plot_pelagic_diff_box(group, scenario, box_number, control, time, start, end, event_start):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Pelagic Biomass of ' + str(group) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,0:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,0:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time, diff,linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_benthic_diff_box(group, scenario, box_number, control, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Benthic Biomass of ' + str(group) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        diff = p_oiled - p_control
        ax.plot(time, diff, linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_sediment_diff_box(group, scenario, box_number, control, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Sediment Biomass of ' + str(group) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,6], np.nan)
        p_oiled = pelagic_oiled
        p_control = pelagic_control
        diff = p_oiled - p_control
        ax.plot(time, diff, linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_surface_diff_box(group, scenario, box_number, control, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference Surface Biomass of ' + str(group) + ' in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,box_number,4:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,box_number,4:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time, diff,linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_bacteria_diff_box(scenario, box_number, control, time, start, end, event_start): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Bacteria Biomass in Salish Sea Atlantis box ' + str(box_number), fontsize = font_size)
    # ax.set_ylim([y_min, y_max])

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,0:5], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,0:5], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,box_number,6], np.nan)
        
        diff = b_oiled - b_control
        ax.plot(time, diff,linewidth = 2)
    
    c_diff = b_control - b_control
    ax.legend(bacteria, loc='center left')
    ax.plot(time, c_diff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_bacteria_diff(scenario, control, time, start, end, event_start): #bacteria, plankton

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Bacteria Biomass in Salish Sea Atlantis', fontsize = font_size)
    ax.set_ylim([-0.01, 0])

    for species in bacteria:
        if "pelagic" in species:
            bact_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,0:5], np.nan) # tonnes, take only water column layers
            bact_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,0:5], np.nan)
            b_oiled = bact_oiled.sum(axis=2)
            b_control = bact_control.sum(axis=2)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        else:
            b_oiled = np.ma.filled(scenario.variables[bacteria[species] + '_N'][start:end,:,6], np.nan) # tonnes, take only sediment layer
            b_control = np.ma.filled(control.variables[bacteria[species] + '_N'][start:end,:,6], np.nan)
            b_oiled = bact_oiled.sum(axis=1)
            b_control = bact_control.sum(axis=1)
        
        diff = b_oiled - b_control
        ax.plot(time, diff,linewidth = 2)
    
    c_diff = b_control - b_control
    ax.legend(bacteria, loc='center left')
    ax.plot(time, c_diff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_pelagic_diff(group, scenario, control, time, start, end, event_start):

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Pelagic Biomass of ' + str(group) + ' in Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,0:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,0:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time, diff,linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_benthic_diff(group, scenario, control, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Benthic Biomass of ' + str(group) + ' in Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time, diff, linewidth = 2)

    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_sediment_diff(group, scenario, control, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference in Sediment Biomass of ' + str(group) + ' in Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:
        
        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,6], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,6], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time, diff, linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5)

def plot_surface_diff(group, scenario, control, time, start, end, event_start): 

    fig, ax = plt.subplots(figsize = (14,3))
    ax.tick_params(labelsize=label_size)
    ax.set_ylabel('scenario - control (mg N$^{-3}$)')
    ax.set_title('Difference Surface Biomass of ' + str(group) + ' in Salish Sea Atlantis', fontsize = font_size)
    #ax.set_ylim([y_min, y_max])

    for species in group:

        pelagic_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][start:end,:,4:5], np.nan) # tonnes
        pelagic_control = np.ma.filled(control.variables[group[species] + '_N'][start:end,:,4:5], np.nan)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        p_oiled = pelagic_oiled.sum(axis=1)
        p_control = pelagic_control.sum(axis=1)
        diff = p_oiled - p_control
        ax.plot(time, diff,linewidth = 2)
    
    cdiff = p_control - p_control
    ax.legend(group, loc='center left')    
    ax.plot(time, cdiff, 'k',linewidth = 2)
    ax.plot(event_start, 1, 'ro', alpha=0.5);

def plot_pah(pah, scenario1, scenario2, scenario3, time, start, end, event_start): 

    Phe1 = np.ma.filled(scenario1.variables[pah], np.nan)
    Phe2 = np.ma.filled(scenario2.variables[pah], np.nan)
    Phe3 = np.ma.filled(scenario3.variables[pah], np.nan)
    Phe1 = Phe1.sum(axis=2)
    Phe1 = Phe1.sum(axis=1)
    Phe2 = Phe2.sum(axis=2)
    Phe2 = Phe2.sum(axis=1)
    Phe3 = Phe3.sum(axis=2)
    Phe3 = Phe3.sum(axis=1)

    fig, ax = plt.subplots(figsize = (14,3))
    ax.plot(time, Phe1[start:end], time, Phe2[start:end], time, Phe3[start:end])
    ax.plot(event_start, 0, 'ro', alpha=0.5)
    ax.set_ylabel('mg Phe m$^{-3}$')
    ax.legend(['scenario 1', 'scenario 2', 'scenario 3']);

def plot_pelagic_pah_in_bio(group, scenario1, scenario2, scenario3, pah, time, start, end, event_start):

    for species in group:
        pelagic_oiled1 = scenario1.variables[group[species] + '_' + pah][start:end,:,:]
        pelagic_oiled2 = scenario2.variables[group[species] + '_' + pah][start:end,:,:]
        pelagic_oiled3 = scenario3.variables[group[species] + '_' + pah][start:end,:,:]
        # sum over depth
        p_oiled1 = pelagic_oiled1.sum(axis=2)
        p_oiled2 = pelagic_oiled2.sum(axis=2)
        p_oiled3 = pelagic_oiled3.sum(axis=2)
        # sum over boxes
        p_oiled1 = pelagic_oiled1.sum(axis=1)
        p_oiled2 = pelagic_oiled2.sum(axis=1)
        p_oiled3 = pelagic_oiled3.sum(axis=1)
        fig, ax = plt.subplots(figsize = (14,3))
        ax.plot(time, p_oiled1, time, p_oiled2, time, p_oiled3, linewidth = 2)
        ax.set_title(species)
        ax.set_ylabel('mgPAH')
        ax.plot(event_start, 1, 'ro', alpha=0.5)
        ax.legend(['scenario 1', 'scenario 2', 'scenario 3']);

def plot_pelagic_pah_in_bio_box(group, scenario1, scenario2, scenario3, box_number, pah, time, start, end, event_start):

    for species in group:
        pelagic_oiled1 = scenario1.variables[group[species] + '_' + pah][start:end,box_number,:]
        pelagic_oiled2 = scenario2.variables[group[species] + '_' + pah][start:end,box_number,:]
        pelagic_oiled3 = scenario3.variables[group[species] + '_' + pah][start:end,box_number,:]
        p_oiled1 = pelagic_oiled1.sum(axis=1)
        p_oiled2 = pelagic_oiled2.sum(axis=1)
        p_oiled3 = pelagic_oiled3.sum(axis=1)
        fig, ax = plt.subplots(figsize = (14,3))
        ax.plot(time, p_oiled1, time, p_oiled2, time, p_oiled3, linewidth = 2)
        ax.set_title(species)
        ax.set_ylabel('mgPAH')
        ax.plot(event_start, 1, 'ro', alpha=0.5)
        ax.legend(['scenario 1', 'scenario 2', 'scenario 3']);

def boxplot_pelagic(group, scenario, control, days, df): #bacteria, plankton

    spp = []

    for species in group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][day,:,0:5], np.nan) # tonnes, take only water column layers
            p_control = np.ma.filled(control.variables[group[species] + '_N'][day,:,0:5], np.nan)
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
    fig, ax = plt.subplots(figsize=(15, 6))
    df1.plot.bar(ax=ax)  
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)  # to place the legend outside
    plt.ylabel('Percent (%) change', fontsize=12)
    plt.xlabel('Pelagic Groups', fontsize=12)
    plt.title('Results of simulation', fontsize=14);

def boxplot_benthic(group, scenario, control, days, df): 

    spp = []

    for species in group:
        results = list()
        for day in days:
            p_oiled = np.ma.filled(scenario.variables[group[species] + '_N'][day,:], np.nan) # tonnes, take only water column layers
            p_control = np.ma.filled(control.variables[group[species] + '_N'][day,:], np.nan)
            p_oiled = p_oiled.sum(axis=1)
            p_control = p_control.sum(axis=1)
            ratio = (p_oiled/p_control-1)*100
            results.append(ratio)
        spp.append(group[species])
        df.loc[len(df.index)] = results
    df['bio_group'] = spp
    df1 = df.set_index('bio_group')
    fig, ax = plt.subplots(figsize=(15, 6))
    df1.plot.bar(ax=ax)  
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', fontsize=12)  # to place the legend outside
    plt.ylabel('Percent (%) change', fontsize=12)
    plt.xlabel('Benthic Groups', fontsize=12)
    plt.title('Results of simulation', fontsize=14);