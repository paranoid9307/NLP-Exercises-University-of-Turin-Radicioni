import utils as ut
import summarization as sm

#importing documents
document1 = ut.importDocument('./txtFiles/Napoleon-wiki.txt')
document2 = ut.importDocument('./txtFiles/Ebola-virus-disease.txt')
document3 = ut.importDocument('./txtFiles/Life-indoors.txt')
nasari = ut.importNasari('./txtFiles/dd-small-nasari-15.txt')
procNasari = ut.processNasari(nasari)
#First document summarization (10%, 20%, 30%)
summ1_30 = sm.summarize(document1, procNasari, 30)
summ1_20 = sm.summarize(document1, procNasari, 20)
summ1_10 = sm.summarize(document1, procNasari, 10)
#write summarizations on files
ut.writeSummarization(summ1_10, './Output/document1 10% Summarization.txt')
ut.writeSummarization(summ1_20, './Output/document1 20% Summarization.txt')
ut.writeSummarization(summ1_30, './Output/document1 30% Summarization.txt')
#Second document summarization (10%, 20%, 30%)
summ2_30 = sm.summarize(document2, procNasari, 30)
summ2_20 = sm.summarize(document2, procNasari, 20)
summ2_10 = sm.summarize(document2, procNasari, 10)
#write summarizations on files
ut.writeSummarization(summ2_10, './Output/document2 10% Summarization.txt')
ut.writeSummarization(summ2_20, './Output/document2 20% Summarization.txt')
ut.writeSummarization(summ2_30, './Output/document2 30% Summarization.txt')
#Third document summarization (10%, 20%, 30%)
summ3_30 = sm.summarize(document3, procNasari, 30)
summ3_20 = sm.summarize(document3, procNasari, 20)
summ3_10 = sm.summarize(document3, procNasari, 10)
#write summarizations on files
ut.writeSummarization(summ3_10, './Output/document3 10% Summarization.txt')
ut.writeSummarization(summ3_20, './Output/document3 20% Summarization.txt')
ut.writeSummarization(summ3_30, './Output/document3 30% Summarization.txt')


    
         
            