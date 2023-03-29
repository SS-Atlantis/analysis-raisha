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

benthic_invertebrates = { #benthic, 1 depth
    'benthic grazers':'Benthic_grazer', 'other filter feeders': 'Filter_feeder', 'macrobenthos':'Macrobenthos',  
    'sponges':'Sponges', 'bivalves':'Bivalves', 'crabs':'Crabs', 'dungeness crabs':'Dungeness_crabs',
}

macroalgae = { #benthic, 1 depth
    'macroalgae':'Macroalgae', 'seagrass':'Seagrass', 
}

sediment_feeders = { #pelagic, i.e. have > 1 depth level but only exist in the sediment
    'benthic carnivores':'Benthic_Carniv', 'deposit feeders':'Deposit_Feeder', 'meiobenthos':'Meiobenth', 'sedimentary bacteria': 'Sed_Bact',
}
    
shellfish = { #benthic, 1 depth
    'bivalves':'Bivalves', 'crabs':'Crabs', 'dungeness crabs':'Dungeness_crabs',
}

plankton = {
    'carnivorous zooplankton':'Carniv_Zoo', 'gelatinous zooplantkon':'Gelat_Zoo', 'microzooplankton':'MicroZoo',
    'mesozooplankton':'Zoo', 'diatoms':'Diatom', 'picophytoplankton':'PicoPhytopl', 'pelagic bacteria':'Pelag_Bact',
}

pelagic_invertebrates = {
    'squid':'Squid', 'prawn': 'Prawn', 
}

bacteria = {
    'pelagic labile detritus':'Lab_Det', 'pelagic refractory detritus':'Ref_Det', 'pelagic bacteria':'Pelag_Bact',
    'sedimentary labile detritus':'Lab_Det', 'sedimentary refractory detritus':'Ref_Det', 'sedimentary bacteria': 'Sed_Bact',
}

phytoplankton = {
   'diatoms':'Diatom', 'picophytoplankton':'PicoPhytopl',
}

zooplankton = {
    'carnivorous zooplankton':'Carniv_Zoo', 'gelatinous zooplantkon':'Gelat_Zoo', 'microzooplankton':'MicroZoo',
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