# bigDataHw1
read dataset and find impotant/unimportant feature
## 1. 哪些屬性對惡意程式分類有效? 
1. section_names_header
2. ent_q_diffs_var
3. ent_p_8
4. ent_q_diff_diffs_2_min
5. Img4
6. ent_q_diffs_0
7. dc_por
8. GetEnvironmentStrings
9. IsValidCodePage
10. .text_por
## 2. 哪些屬性對惡意程式分類無效? 
1. _vbaVarCat
2. _vbaErase
3. fstcwimul
4. ProcCallEngine
5. _vbaVarTstNe
6. GetFileTitleA
7. PCCTL_CONTEXT
8. misc_market
9. _vbaRecUniToAnsi
10. *invalid*
## 3. 用什麼方法可以幫助我決定上述的結論? 
* Random Forest Feature Importance
## 4. 透過Python哪些套件及方法可以幫助我完成上述工作? 
* pandas
* numpy
* sklearn
## 5. 課程迄今有無建議? 
