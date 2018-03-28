# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: HLT2 --step=HLT:Effcy --era=Run2_2017 --data --conditions 100X_dataRun2_relval_ForTSG_v1 --filein /store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/0EF64D35-5CB0-E711-9056-02163E0142F3.root, /store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/1E5146A6-69B0-E711-BE27-02163E0133A4.root, /store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/3C0373C5-B1B0-E711-A901-02163E014206.root --secondfilein /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/043B4718-E8AD-E711-A493-02163E0140E9.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/0484A040-CDAD-E711-9027-02163E0135D2.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/1447E9C4-D7AD-E711-BCBA-02163E013899.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/22053136-E4AD-E711-8F4D-02163E0135D2.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/34F18270-E1AD-E711-A0A8-02163E014266.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/36C7A44C-CFAD-E711-A51C-02163E01A76D.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/3E59DD56-CAAD-E711-84CA-02163E01A38D.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/4C14E706-D9AD-E711-9F00-02163E014334.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/5A2D4747-CBAD-E711-893B-02163E01A481.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/6626B3F9-D4AD-E711-8D0C-02163E014623.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/68DC1EA7-D1AD-E711-868B-02163E01228F.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/927047A3-D0AD-E711-9146-02163E0143E4.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/94DBEBBB-E2AD-E711-9634-02163E01A552.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/9EFB5E6A-C4AD-E711-AB99-02163E01A46C.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/B6D7BB9F-C0AD-E711-9D9E-02163E014621.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/C0FAF58F-BEAD-E711-9C0B-02163E013647.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/EA7B938D-BEAD-E711-9763-02163E0123F1.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/EAEBAA14-C4AD-E711-8E43-02163E014621.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/EEF4F73B-CAAD-E711-AFC7-02163E011E61.root, /store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/F00DAE89-E7AD-E711-BF64-02163E011AD9.root --processName=HLT2 -n 100 --no_exec
import FWCore.ParameterSet.Config as cms

from Configuration.StandardSequences.Eras import eras

process = cms.Process('HLT2',eras.Run2_2017)

#from MuonAnalysis.TagAndProbe.tp_from_aod_simple_Data import *
import sys
sys.path.append('/afs/cern.ch/work/s/slezki/HLTandL1Studies/CMSSW_1004_EffStudy/src/MuonAnalysis/TagAndProbe/test/jpsi')
#print 'before import'
#from tp_from_aod_simple_Data import tagAndProbe_
from tp_from_aod_simple_Data import process as processTnP
#import tp_from_aod_simple_Data
#print 'after import'
#process.tagAndProbe = processTnP.tagAndProbe
process.extend(processTnP)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.options   = cms.untracked.PSet( wantSummary = cms.untracked.bool(True) )
process.MessageLogger.cerr.FwkReport.reportEvery = 100
process.load('Configuration.EventContent.EventContent_cff')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_AutoFromDBCurrent_cff')
process.load('HLTrigger.Configuration.HLT_Effcy_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')


process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(10000)
)

# Input source
process.source = cms.Source("PoolSource",
    #fileNames = cms.untracked.vstring(),
    fileNames = cms.untracked.vstring(
        '/store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/0EF64D35-5CB0-E711-9056-02163E0142F3.root',
        '/store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/1E5146A6-69B0-E711-BE27-02163E0133A4.root',
        '/store/data/Run2017E/HLTPhysics/MINIAOD/PromptReco-v1/000/304/777/00000/3C0373C5-B1B0-E711-A901-02163E014206.root',
    ),
    secondaryFileNames = cms.untracked.vstring(
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/C0FAF58F-BEAD-E711-9C0B-02163E013647.root', 
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/043B4718-E8AD-E711-A493-02163E0140E9.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/0484A040-CDAD-E711-9027-02163E0135D2.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/1447E9C4-D7AD-E711-BCBA-02163E013899.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/22053136-E4AD-E711-8F4D-02163E0135D2.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/34F18270-E1AD-E711-A0A8-02163E014266.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/36C7A44C-CFAD-E711-A51C-02163E01A76D.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/3E59DD56-CAAD-E711-84CA-02163E01A38D.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/4C14E706-D9AD-E711-9F00-02163E014334.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/5A2D4747-CBAD-E711-893B-02163E01A481.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/6626B3F9-D4AD-E711-8D0C-02163E014623.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/68DC1EA7-D1AD-E711-868B-02163E01228F.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/927047A3-D0AD-E711-9146-02163E0143E4.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/94DBEBBB-E2AD-E711-9634-02163E01A552.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/9EFB5E6A-C4AD-E711-AB99-02163E01A46C.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/B6D7BB9F-C0AD-E711-9D9E-02163E014621.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/EA7B938D-BEAD-E711-9763-02163E0123F1.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/EAEBAA14-C4AD-E711-8E43-02163E014621.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/EEF4F73B-CAAD-E711-AFC7-02163E011E61.root',
        '/store/data/Run2017E/HLTPhysics/RAW/v1/000/304/777/00000/F00DAE89-E7AD-E711-BF64-02163E011AD9.root',
    )
)

process.options = cms.untracked.PSet(
    SkipEvent = cms.untracked.vstring('ProductNotFound')
)

# Production Info
'''
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('HLT2 nevts:100'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)
'''
# Output definition
process.RECOSIMoutput = cms.OutputModule("PoolOutputModule",
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string(''),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('HLT2_HLT.root'),
    outputCommands = process.RECOSIMEventContent.outputCommands,
    splitLevel = cms.untracked.int32(0)
)

# Additional output definition

# Other statements
from HLTrigger.Configuration.CustomConfigs import ProcessName
process = ProcessName(process)

from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '100X_dataRun2_relval_ForTSG_v1', '')

# Path and EndPath definitions
process.endjob_step = cms.EndPath(process.endOfProcess)
process.RECOSIMoutput_step = cms.EndPath(process.RECOSIMoutput)
#process.tagAndProbe_step = cms.EndPath(process.tagAndProbe)

#process.demo = cms.EDAnalyzer('TagProbeFitTreeProducer')
#process.TFileService = cms.Service("TFileService",
#                                   fileName = cms.string( "out.root" )
#                                   )
#process.demo_step = cms.EndPath(process.demo)



# Schedule definition
process.schedule = cms.Schedule()
process.schedule.extend(process.HLTSchedule)
#process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step])
#process.schedule.extend([process.endjob_step,process.demo_step])
process.schedule.extend([process.endjob_step,process.tagAndProbe])
#process.schedule.extend([process.endjob_step,process.RECOSIMoutput_step,process.tagAndProbe])

from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)


# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
