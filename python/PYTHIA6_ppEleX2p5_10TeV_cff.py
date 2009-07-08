import FWCore.ParameterSet.Config as cms

source = cms.Source("EmptySource")
from Configuration.GenProduction.PythiaUESettings_cfi import *
generator = cms.EDFilter("Pythia6GeneratorFilter",
    pythiaHepMCVerbosity = cms.untracked.bool(False),
    maxEventsToPrint = cms.untracked.int32(0),
    pythiaPylistVerbosity = cms.untracked.int32(1),
    filterEfficiency = cms.untracked.double(0.00106),
    crossSection = cms.untracked.double(51560000000.),
    comEnergy = cms.double(10000.0),
    PythiaParameters = cms.PSet(
        pythiaUESettingsBlock,
        processParameters = cms.vstring(
            'MSEL=0         ! User defined processes', 
            'MSUB(11)=1     ! Min bias process', 
            'MSUB(12)=1     ! Min bias process', 
            'MSUB(13)=1     ! Min bias process', 
            'MSUB(28)=1     ! Min bias process', 
            'MSUB(53)=1     ! Min bias process', 
            'MSUB(68)=1     ! Min bias process',
            'MSUB(95)=1     ! Min bias process'),
        # This is a vector of ParameterSet names to be read, in this order
        parameterSets = cms.vstring('pythiaUESettings', 
            'processParameters')
    )
)

elegenfilter = cms.EDFilter("MCSingleParticleFilter",
                             MinPt = cms.untracked.vdouble(2.5,2.5),
                             MinEta = cms.untracked.vdouble(-2.7,-2.7),
                             MaxEta = cms.untracked.vdouble(2.7,2.7),
                             ParticleID = cms.untracked.vint32(11,-11)
)

configurationMetadata = cms.untracked.PSet(
    version = cms.untracked.string('$Revision: 1.4 $'),
    name = cms.untracked.string('$Source: /local/projects/CMSSW/rep/CMSSW/Configuration/GenProduction/python/Attic/PYTHIA6_ppEleX2p5_10TeV_cff.py,v $'),
    annotation = cms.untracked.string('PYTHIA6-MinBias at 10TeV with Electron preselection (pt > 2.5)')
)

ProductionFilterSequence = cms.Sequence(generator*elegenfilter)
