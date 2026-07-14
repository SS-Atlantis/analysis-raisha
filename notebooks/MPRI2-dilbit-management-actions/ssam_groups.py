cohorts = {
    'Benthopelagic':10, 'Small_Demersal_fish':10, 'Small_Flatfish':10, 'Small_pelagic_fish':7,
    'Chinook_salmon':5, 'Chum_salmon':5, 'Coho_salmon':5,'Pink_salmon':5, 'Sockeye_salmon':5, 
    'Other_salmonids':8,'Hatchery_Chinook_salmon':3,'Hatchery_Coho_salmon':3,'Hatchery_Sockeye_salmon':3,
    'Dogfish':10,'Ratfish':10,'Rockfish':10,'Sixgill':10,'Hake':10,
    'Harbor_porpoise':10, 'Harbor_seals':10,'Humpback_whales':10,
    'Large_Demersal_fish':10, 'Large_Flatfish' :10,'Lingcod' :10,
    'Orcas_resident':10, 'Orcas_transient':10,
    'Pacific_herring':10,'Pollock':10,'Sandlance':7, 
    'Seabird_gulls':10, 'Seabirds':10,'Sealions':10,'Skates':10,
}

sharks = {
    'dogfish':'Dogfish','ratfish':'Ratfish', 'sixgill':'Sixgill', 'skates':'Skates',
}

birds = {
    'seagulls':'Seabird_gulls', 'other seabirds':'Seabirds',
}

mammals = {
    'porpoises':'Harbor_porpoise', 'seals':'Harbor_seals', 'humpbacks':'Humpback_whales','sealions':'Sealions',
    'resident orcas':'Orcas_resident', 'transient orcas':'Orcas_transient',
}
    
other_fish = {
    'benthopelagic':'Benthopelagic', 'small pelagic':'Small_pelagic_fish', 'small demersal':'Small_Demersal_fish', 
    'large demersal':'Large_Demersal_fish', 'small flatfish':'Small_Flatfish', 'large flatfish':'Large_Flatfish',
}

named_fish = {
    'hake':'Hake','lingcod':'Lingcod', 'pollock':'Pollock', 'sandlance':'Sandlance', 
    'rockfish':'Rockfish', 'pacific herring':'Pacific_herring',
}

salmon = {
    'Chinook':'Chinook_salmon', 'Chum':'Chum_salmon', 'Coho':'Coho_salmon','Pink':'Pink_salmon', 'Sockeye':'Sockeye_salmon', 
    'Hatchery Chinook':'Hatchery_Chinook_salmon','Hatchery Coho':'Hatchery_Coho_salmon','Hatchery Sockeye':'Hatchery_Sockeye_salmon',
    'Other salmonids':'Other_salmonids'
}

wild_salmon = {
    'Chinook':'Chinook_salmon', 'Chum':'Chum_salmon', 'Coho':'Coho_salmon','Pink':'Pink_salmon', 'Sockeye':'Sockeye_salmon', 
    'Other salmonids':'Other_salmonids'
}

hatchery_salmon = {
    'Hatchery Chinook':'Hatchery_Chinook_salmon','Hatchery Coho':'Hatchery_Coho_salmon','Hatchery Sockeye':'Hatchery_Sockeye_salmon',
}

benthic_invertebrates = { #benthic, 1 depth
    'benthic grazers':'Benthic_grazer', 'other filter feeders': 'Filter_feeder', 'macrobenthos':'Macrobenthos',  
    'sponges':'Sponges', 'bivalves':'Bivalves', 'crabs':'Crabs', 'dungeness crabs':'Dungeness_crabs',
}

macroalgae = { #benthic, 1 depth
    'macroalgae':'Macroalgae', 'seagrass':'Seagrass', 
}

sediment_feeders = { #pelagic, i.e. have > 1 depth level but only exist in the sediment
    'benthic carnivores':'Benthic_Carniv', 'deposit feeders':'Deposit_Feeder', 'sedimentary bacteria': 'Sed_Bact',
}
    
shellfish = { #benthic, 1 depth
    'bivalves':'Bivalves', 'crabs':'Crabs', 'dungeness crabs':'Dungeness_crabs',
}

plankton = {
    'carnivorous zooplankton':'Carniv_Zoo', 'gelatinous zooplantkon':'Gelat_Zoo', 'microzooplankton':'MicroZoo',
    'mesozooplankton':'Zoo', 'diatoms':'Diatom', 'picophytoplankton':'PicoPhytopl', 'pelagic bacteria':'Pelag_Bact',
}

pelagic_invertebrates = {
    'squid':'Squid', #'prawn': 'Prawn', 
}

bacteria = {
    'pelagic labile detritus':'Lab_Det', 'pelagic refractory detritus':'Ref_Det', 'pelagic bacteria':'Pelag_Bact',
    'sedimentary labile detritus':'Lab_Det', 'sedimentary refractory detritus':'Ref_Det', 'sedimentary bacteria': 'Sed_Bact',
}

phytoplankton = {
   'diatoms':'Diatom', 'picophytoplankton':'PicoPhytopl',
}

zooplankton = {
    'microzooplankton':'MicroZoo', 'carnivorous zooplankton':'Carniv_Zoo', 'gelatinous zooplantkon':'Gelat_Zoo', 
    'mesozooplankton':'Zoo',
}

pahs = {
    'Naphthalene', 'Phenanthrene', 'Pyrene', 'Benzo'
}

benthos = { # all benthic groups with only 1 depth
    'benthic grazers':'Benthic_grazer', 'other filter feeders': 'Filter_feeder', 'macrobenthos':'Macrobenthos',  
    'sponges':'Sponges', 'bivalves':'Bivalves', 'crabs':'Crabs', 'dungeness crabs':'Dungeness_crabs',
    'macroalgae':'Macroalgae', 'seagrass':'Seagrass', 
}

primaryproducer = {
   'diatoms':'Diatom', 'picophytoplankton':'PicoPhytopl', 'macroalgae':'Macroalgae', 'seagrass':'Seagrass',
}

all_pelagic = {
    'pelagic bacteria':'Pelag_Bact','picophytoplankton':'PicoPhytopl', 'diatoms':'Diatom','microzooplankton':'MicroZoo', 
    'carnivorous zooplankton':'Carniv_Zoo', 'gelatinous zooplantkon':'Gelat_Zoo', 
    'mesozooplankton':'Zoo', 'squid':'Squid', 'prawn': 'Prawn', 
    'hake':'Hake','lingcod':'Lingcod', 'pollock':'Pollock', 'sandlance':'Sandlance', 
     'pacific herring':'Pacific_herring', 
    'Chinook':'Chinook_salmon', 'Chum':'Chum_salmon', 'Coho':'Coho_salmon','Pink':'Pink_salmon', 'Sockeye':'Sockeye_salmon', 
    'Hatchery Chinook':'Hatchery_Chinook_salmon','Hatchery Coho':'Hatchery_Coho_salmon','Hatchery Sockeye':'Hatchery_Sockeye_salmon', 
    'Other salmonids':'Other_salmonids',
    'small pelagic':'Small_pelagic_fish', 'rockfish':'Rockfish',
    'small demersal':'Small_Demersal_fish', 'small flatfish':'Small_Flatfish', 
    'benthopelagic':'Benthopelagic', 'large demersal':'Large_Demersal_fish', 'large flatfish':'Large_Flatfish',
    'dogfish':'Dogfish','ratfish':'Ratfish', 'sixgill':'Sixgill', 'skates':'Skates',
    'porpoises':'Harbor_porpoise', 'seals':'Harbor_seals', 'sealions':'Sealions',
    'resident orcas':'Orcas_resident', 'transient orcas':'Orcas_transient', 'humpbacks':'Humpback_whales',
    'seagulls':'Seabird_gulls', 'other seabirds':'Seabirds',
    
    'benthic carnivores':'Benthic_Carniv', 'deposit feeders':'Deposit_Feeder', 'sedimentary bacteria': 'Sed_Bact',
}

all_pelagic_verts = {
    'dogfish':'Dogfish','ratfish':'Ratfish', 'sixgill':'Sixgill', 'skates':'Skates',
    'seagulls':'Seabird_gulls', 'other seabirds':'Seabirds',
    'porpoises':'Harbor_porpoise', 'seals':'Harbor_seals', 'humpbacks':'Humpback_whales','sealions':'Sealions',
    'resident orcas':'Orcas_resident', 'transient orcas':'Orcas_transient',
    'benthopelagic':'Benthopelagic', 'small pelagic':'Small_pelagic_fish', 'small demersal':'Small_Demersal_fish', 
    'large demersal':'Large_Demersal_fish', 'small flatfish':'Small_Flatfish', 'large flatfish':'Large_Flatfish',
    'hake':'Hake','lingcod':'Lingcod', 'pollock':'Pollock', 'sandlance':'Sandlance', 
    'rockfish':'Rockfish', 'pacific herring':'Pacific_herring',
    'Chinook':'Chinook_salmon', 'Chum':'Chum_salmon', 'Coho':'Coho_salmon','Pink':'Pink_salmon', 'Sockeye':'Sockeye_salmon', 
    'Hatchery Chinook':'Hatchery_Chinook_salmon','Hatchery Coho':'Hatchery_Coho_salmon','Hatchery Sockeye':'Hatchery_Sockeye_salmon', 
    'Other salmonids':'Other_salmonids', 
}

large_verts = {
    'porpoises':'Harbor_porpoise', 'seals':'Harbor_seals', 'humpbacks':'Humpback_whales','sealions':'Sealions',
    'resident orcas':'Orcas_resident', 'transient orcas':'Orcas_transient',
    'dogfish':'Dogfish','ratfish':'Ratfish', 'sixgill':'Sixgill', 'skates':'Skates',
    'seagulls':'Seabird_gulls', 'other seabirds':'Seabirds',
}

nutrients = {
    'ammonia':'NH3', 'nitrate':'NO3', 'dissolved organic nitrogen':'DON', 'micronutrients': 'MicroNut', 
    'dissolved silica':'Si', 'detrital silica':'Det_Si',
}

planktonic = {
    'microzooplankton':'MicroZoo', #'carnivorous zooplankton':'Carniv_Zoo', 'gelatinous zooplantkon':'Gelat_Zoo', 
    'mesozooplankton':'Zoo', 'diatoms':'Diatom', 'picophytoplankton':'PicoPhytopl', 'pelagic bacteria':'Pelag_Bact',
    'squid':'Squid', #'prawn': 'Prawn', 
}

other_planktonic = {
    'pelagic bacteria':'Pelag_Bact',
    'squid':'Squid', #'prawn': 'Prawn', 
}

detritus = {
    'labile detritus':'Lab_Det','refractory detritus':'Ref_Det',
}

salish_sea = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 18, 19, 20, 21, 23, 26, 28, 31, 32, 33, 34, 35, 36, 37, 38, 39,
    40, 54, 55, 57, 58, 60, 62, 63, 64, 66, 68, 72, 73, 74, 75, 79, 80, 81, 82, 83, 84, 85, 86, 88, 90, 91,92, 94, 96, 98, 101, 
    102, 103, 104, 105, 106, 107, 108, 109, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124]
juan_de_fuca = [1,2,3,4,5,6,7,8,9,10,11]
haro_boundary = [60,33,34,35,36,]
strait_of_georgia = [54,64,68,79,80,81,82,83,84,85,88,92,98,101,102]
sog_south = [54,64,68,79]
sog_center = [80,81,82,83,84,85]
sog_north = [88,92.98,101,102]
puget_sound_main = [20,21,23,26]
fraser_river = [75,80,81]
active_pass = [62,63]


sensitivity_without_base = {'carnivorous zooplankton':9.0, 'gelatinous zooplantkon':0.7, 'microzooplankton':5.5,
    'mesozooplankton':0.2, 'Zooplankton':0.2, 'diatoms':0.1, 'picophytoplankton':0.3, 'Phytoplankton':0.3,
    'pelagic bacteria':0.1,
    'squid':0.1, 'prawn': 0.2, 'benthic grazers':9.6, 'other filter feeders': 0.1, 'macrobenthos':1.8,  
    'sponges':0.1, 'bivalves':0.1, 'crabs':0.6, 'dungeness crabs':0.2,
    'macroalgae':1.4, 'seagrass':6.1, 'benthic carnivores':0.1, 'deposit feeders':0.1, 'meiobenthos':0.1, 
    'sedimentary bacteria': 0.1,
    'dogfish':0.1,'ratfish':0.1, 'sixgill':0.1, 'skates':0.1,
    'seagulls':1.3, 'other seabirds':0.2,
    'porpoises':0.4, 'seals':0.1, 'humpbacks':0.1,'sealions':0.3,
    'resident orcas':0.1, 'transient orcas':0.1,
    'benthopelagic':0.2, 'small pelagic':1.1, 'small demersal':0.1, 
    'large demersal':0.3, 'small flatfish':0.6, 'large flatfish':0.1,
    'hake':0.4,'lingcod':0.1, 'pollock':0.1, 'sandlance':0.6, 
    'rockfish':1.2, 'pacific herring':0.2,
    'Chinook':0.4, 'Chum':0.4, 'Coho':0.1,'Pink':0.1, 'Sockeye':0.7, 
    'Hatchery Chinook':0.1,'Hatchery Coho':0.1,'Hatchery Sockeye':0.2, 
    'Other salmonids':0.1,

    'benthic_invertebrates':0.5,'vegetation':2, 'birds':1.2, 'cetaceans':0.4, 'salmon':0.6,
    'demersal_fish'	:0.2,'pelagic_fish'	:0.3,'pinnipeds':0.1,'plankton':0.1,'elasmobranchs':0.1,
}

sensitivity = {'Macroalgae':0.06, 'Seagrass':0.06, 'Pelag_Bact':0.002,'Phytoplankton':0.024, 'Diatom':0.09, 'PicoPhytopl':0.004, 'Zooplankton':0.001, 
    'MicroZoo':0.001, 'Zoo':0.003, 'Gelat_Zoo':0.004,'Squid':0.0, 
    
    'Small_pelagic_fish':0.06,  'Small_Demersal_fish':0.0, 'Small_Flatfish':0.0006, 
    'Benthopelagic':0.0, 'Large_Demersal_fish':0.0004, 'Large_Flatfish':0.0,'Rockfish':0.0003,
    'Hake':0.007,'Lingcod':0.0005, 'Pollock':0.0, 'Sandlance':0.0003,'Pacific_herring':0.08, 
    'Chinook_salmon':0.0005, 'Chum_salmon':0.0, 'Coho_salmon':0.0,'Pink_salmon':0.0,'Sockeye_salmon':0.02, 
    'Hatchery_Chinook_salmon':0.0,'Hatchery_Coho_salmon':0.0,'Hatchery_Sockeye_salmon':0.0,'Other_salmonids':0.0,
    
    'Benthic_grazer':0.4, 'Filter_feeder':0.0, 'Macrobenthos':0.09,  
    'Sponges':0.0, 'Bivalves':0.02, 'Crabs':0.02, 'Dungeness_crabs':0.004,
    
    'Dogfish':0.0,'Ratfish':0.0,'Sixgill':0.0,'Skates':0.0004,

    'Harbor_porpoise':0.003, 'Harbor_seals':0.0001, 'Sealions':0.0,
    'Orcas_resident':0.0, 'Orcas_transient':0.0,'Humpback_whales':0.0,
    
    'Seabird_gulls':0.0,'Seabirds':0.0,

    'benthic_invertebrates':0.4,'vegetation':0.06, 'birds':0.0, 'cetaceans':0.003, 'salmon':0.02,
    'demersal_fish'	:0.0006,'pelagic_fish':0.06,'pinnipeds':0.003,'plankton':0.09,'elasmobranchs':0.0004,
}

locations = {
    '5b': 'Turn Point', '4a': 'Active Pass', '6a': 'English Bay', '7a': 'Juan de Fuca'
}

base_biomass = {'Pelag_Bact':10000,'PicoPhytopl': 10000, 'Diatom':10000,'MicroZoo':700, 
    'Carniv_Zoo':10000, 'Gelat_Zoo':10000, 
    'Zoo':10000, 'Squid':100, 'Prawn':100, 
    'Benthic_grazer':1000, 'Filter_feeder':100, 'Macrobenthos':10000,  
    'Sponges':100, 'Bivalves':5000, 'Crabs':10000, 'Dungeness_crabs':4000,
    'Macroalgae':10000, 'Seagrass':10000, 
    
    'Benthic_Carniv':10000, 'Deposit_Feeder':10000, 'Sed_Bact':10000,
    
    'Dogfish': 1000, 'Ratfish': 1000, 'Sixgill': 1000, 'Skates': 1000, 'Seabird_gulls': 1000, 'Seabirds': 1000,
    'Harbor_porpoise': 1000, 'Harbor_seals': 1000, 'Humpback_whales': 1000, 'Sealions': 1000,
    'Orcas_resident': 1000, 'Orcas_transient': 1000,
    'Benthopelagic': 1000, 'Small_pelagic_fish': 1000, 'Small_Demersal_fish': 1000, 
    'Large_Demersal_fish': 1000, 'Small_Flatfish': 1000, 'Large_Flatfish': 1000,
    'Hake': 1000, 'Lingcod': 1000, 'Pollock': 1000, 'Sandlance': 1000, 
    'Rockfish': 1000, 'Pacific_herring': 1000,
    'Chinook_salmon': 1000, 'Chum_salmon': 1000, 'Coho_salmon': 1000, 'Pink_salmon': 1000, 'Sockeye_salmon': 1000, 
    'Hatchery_Chinook_salmon': 1000, 'Hatchery_Coho_salmon': 1000, 'Hatchery_Sockeye_salmon': 1000, 
    'Other_salmonids': 1000, 
}

scenarios = {  
    0:'no_PAH', 
    1:'free_PAH',
    2:'30d_closure',
    3:'60d_closure',
    4:'48h_contain',
    5:'48h_contain_30d_closure',
    6:'48h_conatin_90d_closure',
}

conditions = {
    '2019-01-20':'WD_S', '2019-04-12':'CD_strong_N',
    '2020-01-24':'WD_N', '2020-04-11':'CD_medium_S', 
    '2019-10-20':'WD_N_currents_S', '2019-07-03':'FRD_low',
    '2020-10-20':'CD_strong_S', '2020-07-05':'FRD_high'
}