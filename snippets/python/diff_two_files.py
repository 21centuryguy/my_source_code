###########################################################################  
############### diff and save result ###############
with open(trans_result_fullpath) as trans_result, open(expected_result_path + par_name+'_expected_result.txt') as expected_result:
diff = difflib.context_diff(trans_result.readlines(), expected_result.readlines())
			
diff_result_filename = testcase_name + "_" + par_name+'_diff_result_' + datetime + '.txt'
diff_result_fullpath = diff_result_file_path + diff_result_filename
with open(diff_result_fullpath, 'w') as diff_result:
	for line in diff:
		diff_result.write(line)

############### report diff result ###############

diff_result_size = os.path.getsize(diff_result_fullpath)

print "=====================[ diff 結果 ]======================="
print par_name+'_diff_result_size is',diff_result_size
print "\n"
assert diff_result_size == 0
print "期待翻訳結果と一致しました!"
print "======================================================"


########################################################################### 
import difflib

file1 = "myFile1.txt"
file2 = "myFile2.txt"

diff = difflib.ndiff(open(file1).readlines(),open(file2).readlines())
print ''.join(diff),

########################################################################### 
import difflib

diff=difflib.ndiff(open(testFile).readlines(), open(comparisonFile).readlines())

try:
    while 1:
        print diff.next(),
except:
    pass



