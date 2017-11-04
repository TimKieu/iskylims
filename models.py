import datetime

from django.db import models
from django import forms
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

class RunProcess(models.Model):
    runName = models.CharField(max_length=45)
    sampleSheet = models.FileField(upload_to='wetlab/SampleSheets')
    generatedat = models.DateTimeField(auto_now_add=True)
    runState = models.CharField(max_length=25)
    generatedBSFile = models.BooleanField(default=False)
    samples= models.CharField(max_length=45)
    useSpaceImgMb=models.CharField(max_length=10)
    useSpaceFastaMb=models.CharField(max_length=10)
    useSpaceOtherMb=models.CharField(max_length=10)
    requestedCenter= models.CharField(max_length=45)
    
    def __str__(self):
        return '%s' %(self.runName)
        
    def get_sample_file (self):
        return '%s' %(self.sampleSheet)
        
    def get_state(self):
        return '%s' %(self.runState)
        
    def get_info_process (self):
        str_date=self.generatedat.strftime("%I:%M%p on %B %d, %Y")
        if (self.runState == 'Completed'):
            return '%s;%s;%s;%s;%s;%s;%s'  %(self.runName, self.runState, 
                            self.requestedCenter, self.useSpaceImgMb, 
                            self.useSpaceFastaMb, self.useSpaceOtherMb, str_date)
        else:
            return '%s;%s;%s;%s;%s'  %(self.runName, self.runState, 
                            self.requestedCenter, self.sampleSheet, str_date )
    
    def get_run_name (self):
        return '%s' %(self.runName)
            
class Projects(models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    user_id= models.ForeignKey(User)
    projectName= models.CharField(max_length=45)
    procState=models.CharField(max_length=25, default='Not Started')
    libraryKit=models.CharField(max_length=45)
    baseSpaceFile = models.CharField(max_length=255)
    generatedat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.projectName)

    def get_state(self):
        return '%s' %(self.procState)
        
    def get_project_info (self):
        return '%s;%s;%s' %(self.projectName, self.libraryKit, self.baseSpaceFile)
        
    def get_user_name (self):
        user_name = self.user_id.username
        return '%s' %(user_name)
    
    def get_project_name (self):
        return '%s' %(self.projectName)
    
    def get_library_name (self):
        return '%s' %(self.libraryKit)

class RunningParameters (models.Model):
    runName_id = models.OneToOneField(
            RunProcess,
            on_delete=models.CASCADE,
            primary_key=True,
            )            
    RunID= models.CharField(max_length=255)
    ExperimentName= models.CharField(max_length=255)
    RTAVersion= models.CharField(max_length=255)
    SystemSuiteVersion= models.CharField(max_length=255)
    LibraryID= models.CharField(max_length=255)
    Chemistry= models.CharField(max_length=255)
    RunStartDate= models.CharField(max_length=255)
    AnalysisWorkflowType= models.CharField(max_length=255)
    RunManagementType= models.CharField(max_length=255)
    PlannedRead1Cycles= models.CharField(max_length=255)
    PlannedRead2Cycles= models.CharField(max_length=255)
    PlannedIndex1ReadCycles= models.CharField(max_length=255)
    PlannedIndex2ReadCycles= models.CharField(max_length=255)
    ApplicationVersion= models.CharField(max_length=255)
    NumTilesPerSwath= models.CharField(max_length=255)
    ImageChannel= models.CharField(max_length=255)
    Flowcell= models.CharField(max_length=255)
    ImageDimensions= models.CharField(max_length=255)
    FlowcellLayout= models.CharField(max_length=255)
    
    def __str__(self):
        return '%s' %(self.RunID)
        
    def get_run_parameters_info (self):
        #str_run_start_date=self.RunStartDate.strftime("%I:%M%p on %B %d, %Y")
        img_channel=self.ImageChannel.strip('[').strip(']').replace("'","")
        #import pdb; pdb.set_trace()
        return '%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' %(self.RunID, self.ExperimentName, self.RTAVersion,
            self.SystemSuiteVersion, self.LibraryID, self.Chemistry, self.RunStartDate,
            self.AnalysisWorkflowType, self.RunManagementType, self.PlannedRead1Cycles, self.PlannedRead2Cycles,
            self.PlannedIndex1ReadCycles, self.PlannedIndex2ReadCycles, self.ApplicationVersion, self.NumTilesPerSwath,
             img_channel, self.Flowcell, self.ImageDimensions, self.FlowcellLayout)
    




   
class NextSeqStatsBinRunSummary (models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    level= models.CharField(max_length=20)
    yieldTotal= models.CharField(max_length=10)
    projectedTotalYield = models.CharField(max_length=10)
    aligned= models.CharField(max_length=10)
    errorRate=models.CharField(max_length=10)
    intensityCycle= models.CharField(max_length=10)
    biggerQ30= models.CharField(max_length=10)
    generatedat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.level)

    def get_bin_run_summary(self):
        return '%s;%s;%s;%s;%s;%s' %( self.yieldTotal,
                self.projectedTotalYield, self.aligned, self.errorRate, 
                self.intensityCycle, self.biggerQ30)

class NextSeqStatsBinRunRead (models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    read= models.CharField(max_length=10)
    lane = models.CharField(max_length=10)
    tiles = models.CharField(max_length=10)
    density = models.CharField(max_length=40)
    cluster_PF = models.CharField(max_length=40)
    phas_prephas = models.CharField(max_length=40)
    reads = models.CharField(max_length=40)
    reads_PF = models.CharField(max_length=40)
    q30 = models.CharField(max_length=40)
    yields = models.CharField(max_length=40)
    cyclesErrRated = models.CharField(max_length=40)
    aligned = models.CharField(max_length=40)
    errorRate = models.CharField(max_length=40)
    errorRate35 = models.CharField(max_length=40)
    errorRate50 = models.CharField(max_length=40)
    errorRate75 = models.CharField(max_length=40)
    errorRate100 = models.CharField(max_length=40)
    intensityCycle = models.CharField(max_length=40)
    generatedat = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.read)
    
    def get_bin_run_read(self):
        return '%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' %( self.lane,self.tiles, self.density,
                self.cluster_PF, self.phas_prephas, self.reads, self.reads_PF,
                self.q30, self.yields, self.cyclesErrRated, self.aligned,
                self.errorRate, self.errorRate35, self.errorRate50, self.errorRate75,
                self.errorRate100, self.intensityCycle)


class RawStatisticsXml (models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,  null=True)
    defaultAll =models.CharField(max_length=40, null=True)
    rawYield = models.CharField(max_length=255)
    rawYieldQ30= models.CharField(max_length=255)
    rawQuality= models.CharField(max_length=255)
    PF_Yield= models.CharField(max_length=255)
    PF_YieldQ30= models.CharField(max_length=255)
    PF_QualityScore= models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.runprocess_id)
        
    def get_raw_xml_stats(self):
        return '%s;%s;%s;%s;%s;%s;%s;%s;%s;%s' %(self.project, self.barcodeCount,
                self.perfectBarcodeCount, self.rawYield, self.PF_Yield,
                self.rawYieldQ30, self.PF_YieldQ30, self.rawQuality,
                self.PF_Quality, self.sampleNumber)

class RawTopUnknowBarcodes (models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    lane_number= models.CharField(max_length=4)
    top_number = models.CharField(max_length=4)
    count= models.CharField(max_length=40)
    sequence = models.CharField(max_length=40)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return '%s' %(self.lane_number)
    
    def get_unknow_barcodes (self):
        return '%s;%s' %(self.count, self.sequence)


class NextSeqStatsFlSummary(models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,  null=True)
    defaultAll =models.CharField(max_length=40, null=True)  
    flowRawCluster = models.CharField(max_length=40)
    flowPfCluster= models.CharField(max_length=40)
    flowYieldMb= models.CharField(max_length=40)
    sampleNumber= models.CharField(max_length=40)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def get_fl_summary(self):
        return '%s;%s;%s;%s' %(self.flowRawCluster, self.flowPfCluster,
            self.flowYieldMb, self.sampleNumber)

class NextSeqStatsLaneSummary (models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    project_id = models.ForeignKey(Projects,  null=True)
    defaultAll =models.CharField(max_length=40, null=True)
    lane= models.CharField(max_length=10)
    pfCluster = models.CharField(max_length=64)
    percentLane = models.CharField(max_length=64)
    perfectBarcode = models.CharField(max_length=64)
    oneMismatch = models.CharField(max_length=64)
    yieldMb = models.CharField(max_length=64)
    biggerQ30 = models.CharField(max_length=64)
    meanQuality = models.CharField(max_length=64)
    generated_at = models.DateTimeField(auto_now_add=True)
        
    
    def __str__(self):
        return '%s' %(self.runprocess_id)
        
    def get_flow_cell_summary (self):
        return '%s' %(self.runprocess_id)
    
    def get_lane_summary(self):
        return '%s;%s;%s;%s;%s;%s;%s;%s' %(self.lane, self.pfCluster,
                self.percentLane, self.perfectBarcode, self.oneMismatch,
                self.yieldMb, self.biggerQ30, self.meanQuality)

    def get_stats_info (self):

        return'%s;%s;%s' %(self.biggerQ30, self.meanQuality, self.yieldMb)

class NextSeqGraphicsStats (models.Model):
    runprocess_id = models.ForeignKey(
            RunProcess,
            on_delete=models.CASCADE)
    folderRunGraphic= models.CharField(max_length=255)
    cluserCountGraph= models.CharField(max_length=255)
    flowCellGraph= models.CharField(max_length=255)
    intensityByCycleGraph= models.CharField(max_length=255)
    heatMapGraph= models.CharField(max_length=255)
    histogramGraph= models.CharField(max_length=255)
    sampleQcGraph= models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.folderRunGraphic)
        
    def get_graphics(self):
        return '%s;%s;%s;%s;%s;%s'%(self.cluserCountGraph,
                self.flowCellGraph, self.intensityByCycleGraph,
                self.heatMapGraph, self.histogramGraph,
                self.sampleQcGraph)

    def get_folder_graphic(self):
        return '%s' %(self.folderRunGraphic)
        
class SamplesInProject (models.Model):
    project_id = models.ForeignKey(
                Projects,
                on_delete= models.CASCADE)
    sampleName = models.CharField(max_length=255)
    barcodeName = models.CharField(max_length=255)
    pfClusters = models.CharField(max_length=55)
    percentInProject = models.CharField(max_length=25)
    yieldMb = models.CharField(max_length=55)
    qualityQ30 = models.CharField(max_length=55)
    meanQuality = models.CharField(max_length=55)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return '%s' %(self.sampleName)
    
    def get_sample_information(self):
        return '%s;%s;%s;%s;%s;%s;%s' %(self.sampleName , self.barcodeName,
                self.pfClusters ,self.percentInProject, self.yieldMb ,
                self.qualityQ30 , self.meanQuality )
    def get_sample_name(self):
        return '%s' %(self.sampleName)
   
    def get_project_name (self) :
       p_id = self.project_id
       project_name =Projects.objects.get(projectName=p_id).get_project_name()
       #Projects.objects.prefetch_related('user_id').filter(user_id = user_id)
       return '%s' %(project_name)
'''    
class MiSeqStatisticsBin (models.Model):
    document = models.OneToOneField(
            Document,
            on_delete=models.CASCADE,
            primary_key=True,
            )
    lane = models.CharField(max_length=10)
    singleRead = models.CharField(max_length=10)
    tiles = models.CharField(max_length=10)
    density = models.CharField(max_length=10)
    cluster_PF = models.CharField(max_length=10)
    phas_prephas = models.CharField(max_length=10)
    reads = models.CharField(max_length=10)
    reads_PF = models.CharField(max_length=10)
    q30 = models.CharField(max_length=10)
    yields = models.CharField(max_length=10)
    cyclesErrRated = models.CharField(max_length=10)
    aligned = models.CharField(max_length=10)
    errorRate = models.CharField(max_length=10)
    errorRate35 = models.CharField(max_length=10)
    errorRate75 = models.CharField(max_length=10)
    errorRate100 = models.CharField(max_length=10)
    intensityCycle = models.CharField(max_length=10)
    comments = models.CharField(max_length=10)
    status = models.CharField(max_length=10)
    
    def __str__(self):
        return '%s' %(self.document)

'''
'''    
class MiSeqStatisticsXml (models.Model):
    document = models.ForeignKey(
            Document,
            on_delete=models.CASCADE)
    rawYield = models.CharField(max_length=20)
    rawYieldQ30= models.CharField(max_length=20)
    rawQuality= models.CharField(max_length=20)
    PF_Yield= models.CharField(max_length=20)
    PF_YieldQ30= models.CharField(max_length=20)
    PF_Quality= models.CharField(max_length=20)
    barcodeCount= models.CharField(max_length=20)
    perfectBarcodeCount= models.CharField(max_length=20)
    project=models.CharField(max_length=30,default=False)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.document)
'''
'''
class MiSeqGraphicsStats (models.Model):
    document = models.ForeignKey(
            Document,
            on_delete=models.CASCADE)
    folderGraphic= models.CharField(max_length=255)
    cluserCountGraph= models.CharField(max_length=255)
    flowCellGraph= models.CharField(max_length=255)
    intensityByCycleGraph= models.CharField(max_length=255)
    heatMapGraph= models.CharField(max_length=255)
    histogramGraph= models.CharField(max_length=255)
    sampleQcGraph= models.CharField(max_length=255)
    
    
    def __str__(self):
        return '%s' %(self.document)
'''  

'''
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


'''
'''
class Document(models.Model):
    run_name = models.CharField(max_length=255, blank=True)
    project_name = models.CharField(max_length=255, blank=True) 
    description = models.CharField(max_length=255, blank=True)
    csv_file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=255, blank=True)
    user_id = models.CharField(max_length=50,blank=True)
    email = models.EmailField(max_length=255,blank=True)
    convert = models.BooleanField(default=False)
    
    
    def __str__(self):
        return '%s' %(self.run_name)
    
    def get_run_info (self):
        return '%s;%s;%s;%s;%s;%s;%s' %(self.run_name, self.project_name, 
                    self.user_id, self.description,  self.name, 
                    self.csv_file, self.uploaded_at)
''' 
'''       
class BaseSpaceFile (models.Model):
    document = models.OneToOneField(
            Document,
            on_delete=models.CASCADE,
            primary_key=True,
            )
    baseSpace_file = models.CharField(max_length=255)
    generated_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s' %(self.baseSpace_file)
'''
'''
class UserInfo(models.Model):
    userid=models.CharField(max_length=25)
    userFirstName=models.CharField(max_length=45)
    userLastName=models.CharField(max_length=45)
    userArea=models.CharField(max_length=25)
    userEmail=models.EmailField(max_length=45)
    
    def __str__ (self):
        return '%s' %(self.userid)
'''
'''
class BioInfo(models.Model):
    info1=models.CharField(max_length=45)
    info2=models.CharField(max_length=45, default='')
    serviceRegistration= models.CharField(max_length=45, default='not required')
    researcher =models.CharField(max_length=45, default='')
    department= models.CharField(max_length=45, default='not assigned')
    

    def __str__(self):
        return '%s' %(self.info1)
'''
    



	
